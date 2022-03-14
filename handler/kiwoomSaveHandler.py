from service.kiwoomSaveService import KiwoomSaveService
from service.kiwoomSimpleService import KiwoomSimpleService
from service.calculateService import CalculateService
from service.stockSearchService import StockSearchService
from module.kiwoom.trader import KWTrader

import time

class KiwoomSaveHandler:

    def __init__(self):
        self.tr = KWTrader()
        self.tr.initialize()
        self.tr.connection()
        self.kiwoom_save = KiwoomSaveService(self.tr)
        self.kiwoom_simple = KiwoomSimpleService(self.tr)
        self.calculate = CalculateService()
        self.stock_search = StockSearchService()

    '''
        기관/외국인 거래 추세정보 저장(opt10045)
    '''
    def save_agency_trading_trend(self):
        code_list = []
        market_nm = "KOSPI"
        if(market_nm == "KOSPI"):
            code_list = self.kiwoom_simple.get_code_list_by_market(0)
        elif(market_nm == "KOSDAQ"):    
            code_list = self.kiwoom_simple.get_code_list_by_market(10)

        # kiwoom_save.save_opt10045("300120", "20191101", "20191126")
        last_day = "20220218"
        # print(len(code_list))
        # 20210910 ~ 20220209
        # 20210420 ~ 20210909
        # 20201123 ~ 20210419

        first_day = self.calculate.get_start_business_day_before_days(last_day, 1)
        print(first_day, last_day)
        search_index = 1
        start_index = 0 + (search_index * 900)
        end_index = 899 + (search_index * 900)

        cnt = start_index
        for code in code_list[start_index:end_index]:
            self.kiwoom_save.save_opt10045(code, market_nm, first_day, last_day)
            cnt = cnt + 1
            print(cnt)
            time.sleep(1)
            # print(code)
            
        print("command completed.........")

    '''
        시장 종목 코드 저장(opt10045)
    '''
    def save_stock_code_list(self):
        # KOSPI
        code_list = self.kiwoom_simple.get_code_list_by_market(0) 
        self.kiwoom_save.save_stock_code_by_market("KOSPI", code_list)
        # KOSDAQ
        code_list = self.kiwoom_simple.get_code_list_by_market(10)
        self.kiwoom_save.save_stock_code_by_market("KOSDAQ", code_list)
                

    def save_bagic_stock_info(self):

        # KOSPI
        stock_list = self.stock_search.get_stock_code_list_by_market("KOSPI")
        for stock in stock_list:
            code = stock[0] 
            name = stock[1]
            print(name)
            self.kiwoom_save.save_bagic_stock_info(code)
            time.sleep(1)

        # KOSDAQ
        code_list = self.kiwoom_simple.get_code_list_by_market(10)
        for code in code_list:
            self.kiwoom_save.save_stock_code_by_market("KOSDAQ", code)