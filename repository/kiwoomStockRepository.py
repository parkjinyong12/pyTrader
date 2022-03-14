from module.db.postgresql_db import PostgresqlDB

class KiwoomStockRepository(PostgresqlDB):

    def __init__(self):
        super().__init__()

    def save_stock_code(self, market_nm, reg_date, code_full_list):
        try :
            for row in code_full_list:
                sql = ("INSERT INTO kiwoom_stock_cd(stock_cd, stock_nm, market_nm, reg_date) VALUES " 
        + "('{}','{}', '{}', TO_TIMESTAMP('{}','YYYYMMDD'))").format(row[0], row[1], market_nm, reg_date)
                print("sql", sql)
                self.cursor.execute(sql)
            
            self.db.commit()
        except Exception as e :
            print("insert DB err ",e)

    def read_stock_code(self, market_nm, search_columns):
        result = None
        try:
            # stock_cd, market_nm, reg_date
            sql = ("SELECT {} FROM kiwoom_stock_cd" 
            + " WHERE 1 = 1"
            + " AND market_nm = '{}'").format(','.join(search_columns), market_nm)
            # print("sql", sql)
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            print("read DB err",e)
        
        return result