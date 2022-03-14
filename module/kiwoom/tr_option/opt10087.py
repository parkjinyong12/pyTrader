from module.kiwoom.tr_option.base import KWTR
from copy import deepcopy

# [ opt10087 : 시간외단일가요청 ]
class Opt10087(KWTR):

    def __init__(self, core):
        super().__init__(core)

        self.rq_name = self.tr_code = 'opt10087'

        self.record_name_multiple = '시간외단일가'
        self.header_multiple = [
            '호가잔량기준시간',
            '시간외단일가_매도호가직전대비5', '시간외단일가_매도호가직전대비4', '시간외단일가_매도호가직전대비3', '시간외단일가_매도호가직전대비2', '시간외단일가_매도호가직전대비1',
            '시간외단일가_매도호가수량5', '시간외단일가_매도호가수량4', '시간외단일가_매도호가수량3', '시간외단일가_매도호가수량2', '시간외단일가_매도호가수량1',
            '시간외단일가_매도호가5', '시간외단일가_매도호가4', '시간외단일가_매도호가3', '시간외단일가_매도호가2', '시간외단일가_매도호가1',
            '시간외단일가_매수호가1', '시간외단일가_매수호가2', '시간외단일가_매수호가3', '시간외단일가_매수호가4', '시간외단일가_매수호가5',
            '시간외단일가_매수호가수량1', '시간외단일가_매수호가수량2', '시간외단일가_매수호가수량3', '시간외단일가_매수호가수량4', '시간외단일가_매수호가수량5',
            '시간외단일가_매수호가직전대비1', '시간외단일가_매수호가직전대비2', '시간외단일가_매수호가직전대비3', '시간외단일가_매수호가직전대비4', '시간외단일가_매수호가직전대비5',
            '시간외단일가_매도호가총잔량', '시간외단일가_매수호가총잔량',
            '매도호가총잔량직전대비', '매도호가총잔량', '매수호가총잔량', '매수호가총잔량직전대비',
            '시간외매도호가총잔량직전대비', '시간외매도호가총잔량', '시간외매수호가총잔량', '시간외매수호가총잔량직전대비',
            '시간외단일가_현재가', '시간외단일가_전일대비기호', '시간외단일가_전일대비', '시간외단일가_등락율', '시간외단일가_누적거래량',
        ]


    def tr_opt(self, code, prev_next, screen_no):
	    # SetInputValue("종목코드"	,  "입력값 1");

        self.core.set_input_value('종목코드', code)
        self.core.comm_rq_data(self.rq_name, self.tr_code, prev_next, screen_no)

        self.tr_data = deepcopy(self.core.receive_tr_data_handler[self.tr_code][screen_no])

        return self.tr_data
