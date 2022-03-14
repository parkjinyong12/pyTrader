

class sampleRepository:

    def __init__(self):
        print("StockDaliyRepository init")
  
    def readDB(self,sql):
        print("sql", sql)
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
        except Exception as e :
            print("read DB err",e)
        
        return result

    def executeDB(self,sql,action):
        print("sql", sql)
        try :            
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e :
            if action == "UPDATE":
                print("update DB err",e)
            elif action == "DELETE":
                print("delete DB err", e)
            elif action == "INSERT":
                print("insert DB err ",e)