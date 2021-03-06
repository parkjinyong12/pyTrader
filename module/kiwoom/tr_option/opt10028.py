from module.kiwoom.tr_option.base import KWTR
from copy import deepcopy

# [ opt10028 : 시가대비등락률요청 ]
class Opt10028(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10028'

        self.record_name_multiple = '시가대비등락률'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '시가', '고가', '저가', '시가대비', '현재거래량', '체결강도',
        ]


    def tr_opt(self, input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        # 정렬구분 = 1:시가, 2:고가, 3:저가, 4:기준가
        # 거래량조건 = 0000:전체조회, 0010:만주이상, 0050:5만주이상, 0100:10만주이상, 0500:50만주이상, 1000:백만주이상
        # 시장구분 = 000:전체, 001:코스피, 101:코스닥
        # 상하한포함 = 0:불 포함, 1:포함
        # 종목조건 = 0:전체조회, 1:관리종목제외, 4:우선주+관리주제외, 3:우선주제외, 5:증100제외, 6:증100만보기, 7:증40만보기, 8:증30만보기, 9:증20만보기
        # 신용조건 = 0:전체조회, 1:신용융자A군, 2:신용융자B군, 3:신용융자C군, 4:신용융자D군, 9:신용융자전체
        # 거래대금조건 = 0:전체조회, 3:3천만원이상, 5:5천만원이상, 10:1억원이상, 30:3억원이상, 50:5억원이상, 100:10억원이상, 300:30억원이상, 500:50억원이상, 1000:100억원이상, 3000:300억원이상, 5000:500억원이상
        # 등락조건 = 1:상위, 2:하위

        self.core.set_input_value('정렬구분', input0)
        self.core.set_input_value('거래량조건', input1)
        self.core.set_input_value('시장구분', input2)
        self.core.set_input_value('상하한포함', input3)
        self.core.set_input_value('종목조건', input4)
        self.core.set_input_value('신용조건', input5)
        self.core.set_input_value('거래대금조건', input6)
        self.core.set_input_value('등락조건', input7)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
