import imp
import time
import pandas as pd

from module.kiwoom.trader import KWTrader
from module.kiwoom.constants import KWErrorCode

from repository.kiwoomOpt10045Repository import KiwoomOpt10045Repository
from repository.kiwoomStockRepository import KiwoomStockRepository

from service.calculateService import CalculateService
from service.stockSearchService import StockSearchService
from service.kiwoomService import KiwoomService

class KiwoomSaveService:

    def __init__(self, tr):
        assert(isinstance(tr, KWTrader))
        self.tr = tr
        self.kiwoomRepo = KiwoomOpt10045Repository()
        self.kiwoom_stock_code_repo = KiwoomStockRepository()
        self.calculate = CalculateService()
        self.stockSearch = StockSearchService()
        self.kiwoom = KiwoomService()
        print("KiwoomSaveService init")

    # 시장코드 조회
    def save_opt10045(self, code, market_nm, start_day, end_day):
        
        tr_data = self.tr.opt10045(code, start_day, end_day, "1", "1", "_", "_", 0, "0145")
        tr_mutiple_rows = tr_data['comm_data']['multiple']['rows']
        cleaning_rows = []

        # 현재 존재하는 종목코드이나 과거에 상장되지 있지 않은 시기, 조회한 경우.
        if(tr_mutiple_rows is None):
            print(code ,tr_data['comm_data']['multiple']['rows']) 
            return

        for row in tr_mutiple_rows:
            row[0] = str(row[0])
            row[1] = str(abs(int(row[1])))
            row[2] = str(row[2])
            row[3] = str(row[3])
            row[4] = str(row[4])
            row[5] = str(row[5])
            row[6] = str(row[6])
            row[7] = str(row[7])
            row[8] = str(row[8])
            row[9] = str(row[9])
            row[10] = str(row[10])
            cleaning_rows.append(row)

        self.kiwoomRepo.save_opt10045(code, market_nm, cleaning_rows)

        print("data count",len(tr_mutiple_rows))

    def save_stock_code_by_market(self, market_nm, code_list):
        reg_date = self.calculate.get_today_yyyymmdd()
        code_full_list = []
        for code in code_list:
            row = []
            row.append(code)
            row.append(self.tr.get_master_code_name(code))
            code_full_list.append(row)

        self.kiwoom_stock_code_repo.save_stock_code(market_nm, reg_date, code_full_list)


    def save_bagic_stock_info(self, code):
        tr_data = self.tr.opt10001(code, 0, "0101")
        tr_mutiple_rows = tr_data['comm_data']['single']['rows']
        # self.kiwoom_stock_code_repo.save_stock_info(market_nm, reg_date, code_full_list)
        print(code ,tr_mutiple_rows) 

            

            
            
        

        

        