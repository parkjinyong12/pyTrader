from service.stockSearchService import StockSearchService
from service.kiwoomSimpleService import KiwoomSimpleService
from service.calculateService import CalculateService
from module.kiwoom.trader import KWTrader

import time

class StockSearchHandler:

    def __init__(self):
        self.stock_search = StockSearchService()
        self.calculate = CalculateService()

    def search_agency_trading_trend(self, end_day):
        print("search_agency_trading_trend - handler")

        tarket_date = self.calculate.get_today_yyyymmdd()
        tarket_date = end_day
        code_list = []
        korea_market = ["KOSPI", "KOSDAQ"]
        for market_nm in korea_market:
            code_list = self.stock_search.get_stock_code_list_by_market(market_nm)
            cnt = 0
            for row in code_list:
                stock_cd = row[0]
                stock_nm = row[1]
                
                start_day = None
                # 5일
                trend_5_data = self.get_avg_rate_of_rise_from_to_period(stock_cd, tarket_date, 5)
                
                # 20일
                trend_20_data = self.get_avg_rate_of_rise_from_to_period(stock_cd, tarket_date, 20)
                
                # 20일
                trend_60_data = self.get_avg_rate_of_rise_from_to_period(stock_cd, tarket_date, 60)

                if(trend_5_data['agency_er'] > trend_20_data['agency_er'] 
                and trend_5_data['agency_er'] > 0 
                and trend_20_data['agency_er'] > 0
                and trend_60_data['agency_er'] > 0
                and trend_5_data['agency_er'] > (float(trend_20_data['agency_er']) * 2)
                and trend_60_data['price_er'] < 0
                ):
                    print(stock_cd, stock_nm, "agency buying trend reversal")
                    print("start_day",trend_5_data['start_day'],"end_day",tarket_date,"index",5,"agency_er",trend_5_data['agency_er'],"price_er",trend_5_data['price_er'])
                    print("start_day",trend_20_data['start_day'],"end_day",tarket_date,"index",20,"agency_er",trend_20_data['agency_er'],"price_er",trend_20_data['price_er'])
                    
                if(trend_5_data['foreign_er'] > trend_20_data['foreign_er'] 
                and trend_5_data['foreign_er'] > 0 
                and trend_20_data['foreign_er'] > 0
                and trend_60_data['foreign_er'] > 0
                and trend_5_data['foreign_er'] > (float(trend_20_data['foreign_er']) * 2)
                and trend_60_data['price_er'] < 0
                ):
                    print(stock_cd, stock_nm, "foreign buying trend reversal")
                    print("start_day",trend_5_data['start_day'],"end_day",tarket_date,"index",5,"foreign_er",trend_5_data['foreign_er'],"price_er",trend_5_data['price_er'])
                    print("start_day",trend_20_data['start_day'],"end_day",tarket_date,"index",20,"foreign_er",trend_20_data['foreign_er'],"price_er",trend_20_data['price_er'])
                
                    

                # self.stock_search.print_accumulation_of_agency_period_graph_by_code(stock_cd, start_day, tarket_date)
                # self.stock_search.print_accumulation_of_foreign_period_graph_by_code(stock_cd, start_day, tarket_date)
                # self.stock_search.print_closing_price_graph_by_code(stock_cd, start_day, tarket_date)

                # start_day = calculate.get_start_business_day_before_days(tarket_date, 9)
                # agency_er_10 = self.stock_search.get_agency_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # foreign_er_10 = self.stock_search.get_foreign_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # price_er_10 = self.stock_search.get_price_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # print("10", start_day, tarket_date, agency_er_10, foreign_er_10, price_er_10)

                # start_day = calculate.get_start_business_day_before_days(tarket_date, 19)
                # agency_er_20 = self.stock_search.get_agency_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # foreign_er_20 = self.stock_search.get_foreign_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # price_er_20 = self.stock_search.get_price_trading_trend_from_to_period(stock_cd, start_day, tarket_date)

                # print("20", start_day, tarket_date, agency_er_20, foreign_er_20, price_er_20)
                # start_day = calculate.get_start_business_day_before_days(tarket_date, 59)
                # agency_er_60 = self.stock_search.get_agency_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # foreign_er_60 = self.stock_search.get_foreign_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                # price_er_60 = self.stock_search.get_price_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
                
                # print("60", start_day, tarket_date, agency_er_60, foreign_er_60, price_er_60)
                # self.stock_search.print_graph_by_code(stock_cd, start_day, tarket_date)

                cnt = cnt + 1
                print(cnt) 

            # print(cnt)

            # time.sleep(1)
            # print(code)
            # -0.293103 -0.695952
            # -0.251224 -0.063656
            # -0.309494 0.102537
            # -0.213935 0.179007

    def get_agency_trading_trend_by_the_day(self, stock_cd, tarket_date, period):
        result_map = {}
        start_day = self.calculate.get_start_business_day_before_days(tarket_date, period)
        result_map['agency_er'] = self.stock_search.get_agency_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
        result_map['foreign_er'] = self.stock_search.get_foreign_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
        result_map['price_er'] = self.stock_search.get_price_trading_trend_from_to_period(stock_cd, start_day, tarket_date)
        result_map['start_day'] = start_day
        return result_map

    def get_avg_rate_of_rise_from_to_period(self, stock_cd, tarket_date, period):
        result_map = {}
        start_day = self.calculate.get_start_business_day_before_days(tarket_date, period)
        result_map['agency_er'] = self.stock_search.get_avg_agency_rate_of_rise_from_to_period(stock_cd, start_day, tarket_date)
        result_map['foreign_er'] = self.stock_search.get_avg_foreign_rate_of_rise_from_to_period(stock_cd, start_day, tarket_date)
        result_map['price_er'] = self.stock_search.get_avg_price_rate_of_rise_from_to_period(stock_cd, start_day, tarket_date)
        result_map['start_day'] = start_day
        return result_map

    def adjust_accumulation(self):

        print("search_agency_trading_trend - handler")

        code_list = []
        korea_market = ["KOSPI", "KOSDAQ"]
        for market_nm in korea_market:
            code_list = self.stock_search.get_stock_code_list_by_market(market_nm)

            cnt = 0
            for row in code_list:
                code = row[0]
                name = row[1]
                
                self.stock_search.adjust_agency_accumulation(code)
                self.stock_search.adjust_foreign_accumulation(code)
                cnt = cnt + 1
                print(cnt, code, name)

    def test(self):
        stock_search = StockSearchService()
        stock_search.test()
        
        


        
