from module.kiwoom.tr_option.base import KWTR
from copy import deepcopy

# [ opt20003 : 전업종지수요청 ]
class Opt20003(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt20003'

        self.record_name_multiple = '전업종지수'
        self.header_multiple = [
            '종목코드', '종목명', '현재가', '전일대비기호', '전일대비', '등락률', '거래량', '비중', '거래대금', '상한', '상승', '보합', '하락', '하한', '상장종목수',
        ]


    def tr_opt(self, input0, prev_next, screen_no):
	    # 업종코드 = 001:종합(KOSPI), 002:대형주, 003:중형주, 004:소형주 101:종합(KOSDAQ), 201:KOSPI200, 302:KOSTAR, 701: KRX100 나머지 ※ 업종코드 참고

        self.core.set_input_value('업종코드', input0)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
