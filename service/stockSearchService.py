import imp
import matplotlib.pyplot as plt


from repository.kiwoomOpt10045Repository import KiwoomOpt10045Repository
from repository.kiwoomStockRepository import KiwoomStockRepository
from service.calculateService import CalculateService

class StockSearchService:

    def __init__(self):
        self.kiwoomRepo = KiwoomOpt10045Repository()
        self.kiwoomStockCdRepo = KiwoomStockRepository()
        self.calculate = CalculateService()
        pass

    def get_agency_trading_trend(self, code, end, before_weeks):
        trading_trend = {}

        start_day = self.calculate.get_start_day_from_end_day_for_weeks(end,4)
        if(before_weeks == 4 or before_weeks == 8 or before_weeks == 12):
            accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start_day, end, ["accumulation_of_agency_period"]) 
            trading_trend[4] = self.calculate.get_efficiency_ratio(accumulation_of_agency)


        start_day = self.calculate.get_start_day_from_end_day_for_weeks(end,8)
        if(before_weeks == 8 or before_weeks == 12):
            accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start_day, end, ["accumulation_of_agency_period"])
            trading_trend[8] = self.calculate.get_efficiency_ratio(accumulation_of_agency)

        start_day = self.calculate.get_start_day_from_end_day_for_weeks(end,12)
        if(before_weeks == 12):
            accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start_day, end, ["accumulation_of_agency_period"])
            trading_trend[12] = self.calculate.get_efficiency_ratio(accumulation_of_agency)
    
        return trading_trend
    
    '''
        efficiency_ratio에 따른 trading_trend   
    '''
    def get_agency_trading_trend_from_to_period(self, code, start, end):
        accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start, end, ["accumulation_of_agency_period"]) 
        return self.calculate.get_efficiency_ratio(accumulation_of_agency)

    def get_foreign_trading_trend_from_to_period(self, code, start, end):
        accumulation_of_foreign = self.kiwoomRepo.read_opt100045(code, start, end, ["accumulation_of_foreign_period"])    
        return self.calculate.get_efficiency_ratio(accumulation_of_foreign)

    def get_price_trading_trend_from_to_period(self, code, start, end):
        accumulation_of_price = self.kiwoomRepo.read_opt100045(code, start, end, ["closing_price"])    
        return self.calculate.get_efficiency_ratio(accumulation_of_price)

    '''
        일 평균 상승률
    '''
    def get_avg_agency_rate_of_rise_from_to_period(self, code, start, end):
        accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start, end, ["accumulation_of_agency_period"]) 
        return self.calculate.get_avg_rate_of_rise_by_days(accumulation_of_agency)

    def get_avg_foreign_rate_of_rise_from_to_period(self, code, start, end):
        accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start, end, ["accumulation_of_foreign_period"]) 
        return self.calculate.get_avg_rate_of_rise_by_days(accumulation_of_agency)

    def get_avg_price_rate_of_rise_from_to_period(self, code, start, end):
        accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start, end, ["closing_price"]) 
        return self.calculate.get_avg_rate_of_rise_by_days(accumulation_of_agency)

    def get_foreign_trading_trend(self, code, end, before_weeks):
        trading_trend = {}
    
        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,4)
        if(before_weeks == 4 or before_weeks == 8 or before_weeks == 12):
            accumulation_of_foreign = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["accumulation_of_foreign_period"])    
            trading_trend[4] = self.calculate.get_efficiency_ratio(accumulation_of_foreign)

        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,8)
        if(before_weeks == 8 or before_weeks == 12):
            accumulation_of_foreign = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["accumulation_of_foreign_period"])    
            trading_trend[8] = self.calculate.get_efficiency_ratio(accumulation_of_foreign)

        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,12)
        if(before_weeks == 12):
            accumulation_of_foreign = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["accumulation_of_foreign_period"])    
            trading_trend[12] = self.calculate.get_efficiency_ratio(accumulation_of_foreign)

        return trading_trend

    def get_price_trading_trend(self, code, end, before_weeks):

        trading_trend = {}
    
        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,4)
        if(before_weeks == 4 or before_weeks == 8 or before_weeks == 12):
            accumulation_of_price = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["closing_price"])    
            trading_trend[4] = self.calculate.get_efficiency_ratio(accumulation_of_price)

        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,8)
        if(before_weeks == 8 or before_weeks == 12):
            accumulation_of_price = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["closing_price"])    
            trading_trend[8] = self.calculate.get_efficiency_ratio(accumulation_of_price)

        before_weeks_day = self.calculate.get_start_day_from_end_day_for_weeks(end,12)
        if(before_weeks == 12):
            accumulation_of_price = self.kiwoomRepo.read_opt100045(code, before_weeks_day, end, ["closing_price"])    
            trading_trend[12] = self.calculate.get_efficiency_ratio(accumulation_of_price)

        return trading_trend

    def adjust_agency_accumulation(self, code):
        date_map = self.get_opt100045_min_maxdate_by_code(code)
        if(len(date_map) == 0):
            return 
        else:
            agency_data_list = self.kiwoomRepo.read_opt100045(code, date_map["min"], date_map["max"], ['kiwoom_opt10045_pk','agency_net_trading_volume'])
            index = 0
            accumulation_sum = 0
            # print(agency_data_list)
            for row in agency_data_list:
                accumulation_sum = accumulation_sum + row[1]
                index = index + 1
                set_map = {}
                where_map = {}
                where_map['stock_cd'] = code
                where_map['kiwoom_opt10045_pk'] = row[0]
                set_map['accumulation_of_agency_period'] = accumulation_sum
                self.kiwoomRepo.update_opt10045_by_pk(set_map, where_map)

    def adjust_foreign_accumulation(self, code):
        date_map = self.get_opt100045_min_maxdate_by_code(code)
        if(len(date_map) == 0):
            return 
        else:
            foreign_data_list = self.kiwoomRepo.read_opt100045(code, date_map["min"], date_map["max"], ['kiwoom_opt10045_pk','foreign_net_trading_volume'])
            index = 0
            accumulation_sum = 0
            # print(foreign_data_list)
            for row in foreign_data_list:
                accumulation_sum = accumulation_sum + row[1]
                index = index + 1
                set_map = {}
                where_map = {}
                where_map['stock_cd'] = code
                where_map['kiwoom_opt10045_pk'] = row[0]
                set_map['accumulation_of_foreign_period'] = accumulation_sum
                self.kiwoomRepo.update_opt10045_by_pk(set_map, where_map)

    def get_opt100045_min_maxdate_by_code(self, code):
        date_map = {}
        date_list = self.kiwoomRepo.read_opt100045_all(code,["MIN(date)","MAX(date)"])
        if(date_list[0][0] is None):
            print("data_list is None. code", code)
            return date_map
        else:
            date_map["min"] = date_list[0][0].strftime('%Y%m%d')
            date_map["max"] = date_list[0][1].strftime('%Y%m%d')
            return date_map

    def print_accumulation_of_agency_period_graph_by_code(self, code, start, end):
        accumulation_of_agency = self.kiwoomRepo.read_opt100045(code, start, end, ["date","accumulation_of_agency_period"]) 

        accumulation_of_agency_list = []
        date_list = []
        for data in accumulation_of_agency:
            date_list.append(data[0])
            accumulation_of_agency_list.append(data[1])

        plt.plot(date_list, accumulation_of_agency_list, color = 'green', marker = 'o', linestyle = 'solid')
        plt.show()

    def print_accumulation_of_foreign_period_graph_by_code(self, code, start, end):
        accumulation_of_foreign = self.kiwoomRepo.read_opt100045(code, start, end, ["date","accumulation_of_foreign_period"]) 

        accumulation_of_foreign_list = []
        date_list = []
        for data in accumulation_of_foreign:
            date_list.append(data[0])
            accumulation_of_foreign_list.append(data[1])

        plt.plot(date_list, accumulation_of_foreign_list, color = 'green', marker = 'o', linestyle = 'solid')
        plt.show()

    def print_closing_price_graph_by_code(self, code, start, end):
        closing_price = self.kiwoomRepo.read_opt100045(code, start, end, ["date","closing_price"]) 

        closing_price_list = []
        date_list = []
        for data in closing_price:
            date_list.append(data[0])
            closing_price_list.append(data[1])

        plt.plot(date_list, closing_price_list, color = 'green', marker = 'o', linestyle = 'solid')
        plt.show()

    def get_stock_code_list_by_market(self, market_nm):
        return self.kiwoomStockCdRepo.read_stock_code(market_nm, ["stock_cd","stock_nm"])

    def test(self):
        result = self.kiwoomRepo.read_opt100045_all("000020",["MIN(date)","MAX(date)"])
        
        print(result[0][0].strftime('%Y%m%d'))
        


        