from module.kiwoom.kiwoom import Kiwoom
import time
import pandas as pd

class KiwoomService:

    def __init__(self):
        print("hello KiwoomService..")
        self.kiwoom = Kiwoom()
        # 서버 접속
        self.kiwoom.comm_connect()

    # 시장코드 조회
    def get_code_list(self,market_name):
        if market_name == "KOSPI":
            return self.kiwoom.get_code_list_by_market(0)
        elif market_name == "KOSDAQ":
            return self.kiwoom.get_code_list_by_market(10)

    # 현재는 내림차순(최신순)으로 출력된다.
    def get_agency_trading_trend_descending_by_item(self, code, start, end):

        # 변수 초기화
        self.kiwoom.reset_opt10045_output()

        # opt10045 호출
        self.kiwoom.set_input_value('종목코드', code)
        self.kiwoom.set_input_value('시작일자', start)
        self.kiwoom.set_input_value('종료일자', end)
        self.kiwoom.set_input_value('기관추정단가구분', 1)
        self.kiwoom.set_input_value('외인추정단가구분', 1)
        self.kiwoom.comm_rq_data('opt10045_req','opt10045',0,'0004')
        time.sleep(1)

        df = pd.DataFrame(self.kiwoom.opt10045_output.get('multi'), 
        columns=[
            'date','closing_price','contrast_sign','day_to_day','fluctuation_rate','trading_volume','accumulation_of_agency_period',
            'agency_net_trading_volume','accumulation_of_foreign_period','foreign_net_trading_volume',
            'limit_exhaustion_rate'
        ])
        df.set_index('date',inplace=True)
        return df

    def get_master_code_name(self, code):
        return self.kiwoom.get_master_code_name(code)

    def get_stock_info(self, code):
        self.kiwoom.opt10001_output = {'stock_code': [], 'stock_name': [], 'stock_market_cap': [], 'sales': [], 'operating_profit': [], 'net_income': []}
        
        # opt10001 호출
        self.kiwoom.set_input_value('종목코드', code)
        self.kiwoom.comm_rq_data('opt10001_req','opt10001',0,'0005')
        time.sleep(1)

        return self.kiwoom.opt10001_output
        