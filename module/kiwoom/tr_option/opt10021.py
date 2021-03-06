from module.kiwoom.tr_option.base import KWTR
from copy import deepcopy

# [ OPT10021 : 호가잔량급증요청 ]
class Opt10021(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10021'

        self.record_name_multiple = '호가잔량급증'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '기준률', '현재', '급증수량', '급증률', '총매수량',
        ]


    def tr_opt(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        # 시장구분 = 001:코스피, 101:코스닥
        # 매매구분 = 1:매수잔량, 2:매도잔량
        # 정렬구분 = 1:급증량, 2:급증률
        # 시간구분 = 분 입력
        # 거래량구분 = 1:천주이상, 5:5천주이상, 10:만주이상, 50:5만주이상, 100:10만주이상
        # 종목조건 = 0:전체조회, 1:관리종목제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기

        self.core.set_input_value('시장구분', market_type)
        self.core.set_input_value('매매구분', input1)
        self.core.set_input_value('정렬구분', input2)
        self.core.set_input_value('시간구분', input3)
        self.core.set_input_value('거래량구분', input4)
        self.core.set_input_value('종목조건', input5)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
