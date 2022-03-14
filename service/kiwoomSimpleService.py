from module.kiwoom.trader import KWTrader

class KiwoomSimpleService:
    def __init__(self, tr):
        assert(isinstance(tr, KWTrader))
        self.tr = tr
        print("KiwoomSimpleService init")
    
    def get_code_list_by_market(self, market):
        code_list = self.tr.get_code_list_by_market(market)
        code_list = code_list.split(';')
        return code_list[:-1]

    def get_master_code_name(self, code):
        return self.tr.get_master_code_name(code)