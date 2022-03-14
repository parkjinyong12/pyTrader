from module.db.postgresql_db import PostgresqlDB

class KiwoomOpt10045Repository(PostgresqlDB):

    def __init__(self):
        super().__init__()

    def save_opt10045(self, code, market_nm, data):
        
        try :
            for row in data:
                sql = ("INSERT INTO kiwoom_opt10045(stock_cd, date, closing_price, contrast_sign, " 
        + "day_to_day, fluctuation_rate, trading_volume, accumulation_of_agency_period," 
        + " agency_net_trading_volume, accumulation_of_foreign_period, " 
        + " foreign_net_trading_volume, limit_exhaustion_rate, market_nm) VALUES " 
        + "('{}', TO_TIMESTAMP('{}','YYYYMMDD'), {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, '{}')").format(code, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], market_nm)
                # print("sql", sql)
                self.cursor.execute(sql)
            
            self.db.commit()
        except Exception as e :
            print("insert DB err ",e)

    def read_opt100045(self, code, start, end, search_columns):
        result = None
        try:
            # stock_cd, date, closing_price, contrast_sign, day_to_day, fluctuation_rate, 
            # trading_volume, accumulation_of_agency_period, agency_net_trading_volume, accumulation_of_foreign_period,
            # foreign_net_trading_volume, limit_exhaustion_rate, market_nm
            sql = ("SELECT {} FROM kiwoom_opt10045" 
            + " WHERE 1 = 1"
            + " AND stock_cd = '{}' AND date >= TO_TIMESTAMP('{}','YYYYMMDD') AND date <= TO_TIMESTAMP('{}','YYYYMMDD')" 
            + " ORDER BY date ASC").format(','.join(search_columns), code, start, end)
            # print("sql", sql)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            print("read DB err",e)
        
        return result

    def read_opt100045_all(self, code, search_columns):
        result = None
        try:
            sql = ("SELECT {} FROM kiwoom_opt10045" 
            + " WHERE 1 = 1"
            + " AND stock_cd = '{}'").format(','.join(search_columns), code)
            # print("sql", sql)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            print("read DB err",e)
        
        return result

    def update_opt10045_by_pk(self, set_map, where_map):
        try:
            sql = "UPDATE kiwoom_opt10045"
            
            if(type(where_map) == dict and len(where_map) > 0):
                sql = sql + " SET"
                set_list = []
                for key, value in set_map.items():
                    set_list.append(" " + str(key) + "=" + str(value) + " ")
    
                set_str = ",".join(set_list)
                sql = sql + set_str
                sql = sql + " WHERE"
                where_list = []
                for key, value in where_map.items():
                    where_list.append(" " + str(key) + "='" + str(value) + "' ")
    
                where_str = "AND".join(where_list)
                sql = sql + where_str
                
                # print("sql", sql)
                self.cursor.execute(sql)
            
            self.db.commit()
        except Exception as e:
            print("update DB err ",e)