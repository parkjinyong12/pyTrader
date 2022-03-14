

class StockDaliyRepository:

    def __init__(self):
        print("StockDaliyRepository init")
  
    def read_opt100045(self,sql):
        try:
            sql = ("INSERT INTO kiwoom_opt10045(stock_cd, date, closing_price, contrast_sign, " 
            + "day_to_day, fluctuation_rate, trading_volume, accumulation_of_agency_period," 
            + " agency_net_trading_volume, accumulation_of_foreign_period, " 
            + " foreign_net_trading_volume, limit_exhaustion_rate, market_nm) VALUES " 
            + "('{}', TO_TIMESTAMP('{}','YYYYMMDD'), {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')").format(code, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], market_nm)
            print("sql", sql)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            print("read DB err",e)
        
        return result