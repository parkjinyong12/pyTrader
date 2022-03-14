from service.kiwoomService import KiwoomService
from service.calculateService import CalculateService
from service.commonService import CommonService

class FindStocksHandler:

    def __init__(self):
        self.kiwoom = KiwoomService()
        self.calculate = CalculateService()
        self.common = CommonService()
        self.logger = []
        print("hello FindStocksHandler..")

    def check_price_market_trend(self, market_nm, search_index, search_days):

        market_codes = []
        if(market_nm == "KOSPI"):
            market_codes = self.kiwoom.get_code_list(market_nm)
        elif(market_nm == "KOSDAQ"):
            market_codes = self.kiwoom.get_code_list(market_nm)

        start_end_days = self.calculate.get_start_day_from_today_for_weeks(52)
        start_day = start_end_days["start"]
        end_day = start_end_days["end"]

        print("from:",start_day,"to:",end_day)
        print('--------------------')

        start_index = 0 + (search_index * 900)
        end_index = 899 + (search_index * 900)

        # 코스닥 종목 내 필터링
        print(market_nm)
        cnt=0
        print("list size",len(market_codes))
        for stock_code in market_codes[start_index:end_index]:
            self.check_price_trend(stock_code, start_day, end_day, search_days)
            cnt=cnt+1
            print("count",cnt)

        print("process completed..")


    def check_price_trend(self, code, start, end, period):

        print_list = []
        foreign_message = []
        agency_message = []

        stock_nm = self.kiwoom.get_master_code_name(code)
        # 내림차순 정렬(최신순)
        df = self.kiwoom.get_agency_trading_trend_descending_by_item(code, start, end)

        closing_price = df.loc[:,'closing_price']
        print(closing_price)
        contrast_sign = df.loc[:,'contrast_sign']
        print(contrast_sign)
        day_to_day = df.loc[:,'day_to_day']
        print(day_to_day)
        trading_volume = df.loc[:,'trading_volume']
        print(trading_volume)
        accumulation_of_agency_period = df.loc[:,'accumulation_of_agency_period']
        print(accumulation_of_agency_period)
        accumulation_of_foreign_period = df.loc[:,'accumulation_of_foreign_period']
        print(accumulation_of_foreign_period)
        limit_exhaustion_rate = df.loc[:,'limit_exhaustion_rate']
        print(limit_exhaustion_rate)

        # 가격
        prc_series = df.loc[:,'closing_price'].astype(float).abs()
        prc_er = self.calculate.get_efficiency_ratio_from_descending_data(prc_series, period)

        # 외국인 누적 순매수
        foreign_acc_series = df.loc[:,'accumulation_of_foreign_period'].astype(float)
        foreign_acc_er = self.calculate.get_efficiency_ratio_from_descending_data(foreign_acc_series, period)
        
        # 기관 누적 순매수
        agency_acc_series = df.loc[:,'accumulation_of_agency_period'].astype(float)
        agency_acc_er = self.calculate.get_efficiency_ratio_from_descending_data(agency_acc_series, period)

        # 조건
        if(foreign_acc_er > 0.2 and prc_er < 0.2):
            foreign_message = " ".join([str(foreign_acc_er)])

        # 조건
        if(agency_acc_er > 0.2 and prc_er < 0.2):
            agency_message = " ".join([str(agency_acc_er)])

        # 로그 저장 조건(외국인, 기관 모두 만족시)
        if len(foreign_message) > 0 and len(agency_message) > 0:
            #if(foreign_acc_er > 3 or agency_acc_er > 3):
            stock_info = self.kiwoom.get_stock_info(code)
            price_message = " ".join([str(prc_er)])
            income_message = " ".join(["cap",stock_info["stock_market_cap"][0],"sales",stock_info["sales"][0],"profit",stock_info["operating_profit"][0],"net",stock_info["net_income"][0]])
            if(int(stock_info["stock_market_cap"][0]) > 4999):
                print(stock_nm, "외국인", foreign_message, "기관", agency_message, "가격", price_message, "실적", income_message)
                self.logger.append(stock_nm + " 외국인 " + foreign_message + ", 기관 " + agency_message + ", 가격 " + price_message + ", 실적 " + income_message + "\n")
                self.common.update_logger(self.logger)
                self.logger = []
            else:
                print(stock_nm, "외국인", foreign_message, "기관", agency_message, "가격", price_message, "실적", income_message)
            
            


        



