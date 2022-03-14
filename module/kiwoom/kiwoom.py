import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

import time
import pandas as pd
import sqlite3

TR_REQ_TIME_INTERVAL = 0.2

class Kiwoom(QAxWidget):
    def __init__(self):
        super().__init__()
        self._create_kiwoom_instance()
        self._set_signal_slots()

    ##########################
    # 로그인, 상태확인, 초기화
    ##########################
    def _create_kiwoom_instance(self):
        self.setControl('KHOPENAPI.KHOpenAPICtrl.1')

    def _set_signal_slots(self):        
        self.OnEventConnect.connect(self._event_connect)
        self.OnReceiveTrData.connect(self._receive_tr_data)
        self.OnReceiveChejanData.connect(self._receive_chejan_data)

    def comm_connect(self):
        self.dynamicCall('CommConnect()')
        self.login_event_loop = QEventLoop()
        self.login_event_loop.exec_()

    def _event_connect(self, err_code):
        if err_code ==0:
            print('connected')
        else:
            print('disconnected')

        self.login_event_loop.exit()

    def get_login_info(self, tag):
        ret = self.dynamicCall('GetLoginInfo(QString)', tag)
        return ret

    #############
    # 조회
    #############
    # 시장 코드 리스트 조회
    def get_code_list_by_market(self, market):
        code_list = self.dynamicCall('GetCodeListByMarket(QString)',market)
        code_list = code_list.split(';')
        return code_list[:-1]

    # 코드에 해당하는 종목명 조회
    def get_master_code_name(self, code):
        code_name = self.dynamicCall('GetMasterCodeName(QString)', code)
        return code_name

    # 접속 상태 조회
    def get_connect_state(self):
        ret = self.dynamicCall('GetConnectState()')
        return ret
    
    # 변수 입력
    def set_input_value(self, id, value):
        self.dynamicCall('SetInputValue(QString, QString)', id, value)

    # 서버로 명령을 송신하는 기능
    def comm_rq_data(self, rqname, trcode, next, screen_no):
        self.dynamicCall('CommRqData(QString, QString, int, QString)', rqname, trcode, next, screen_no)
        self.tr_event_loop = QEventLoop()
        self.tr_event_loop.exec_()

    # 실제 데이터 수신을 담당함.
    def _comm_get_data(self, code, real_type, field_name, index, item_name):
        ret = self.dynamicCall('CommGetData(QString, QString, QString, int, QString)', code, real_type, field_name, index, item_name)
        return ret.strip()

    def _get_repeat_cnt(self, trcode, rqname):
        ret = self.dynamicCall('GetRepeatCnt(QString, QString)', trcode, rqname)
        return ret

    # 서버로 결과를 수신하는 리스너
    def _receive_tr_data(self, screen_no, rqname, trcode, record_name, next, unused1, unused2, unused3, unused4):
        if next == '2':
            self.remained_data = True
        else:
            self.remained_data = False

        # 수신결과 분기 처리
        # 1.주식일봉차트조회(opt10081)
        if rqname == 'opt10081_req':
            self._opt10081(rqname, trcode)
        # 2.예수금상세현황요청(opw00001)    
        elif rqname == 'opw00001_req':
            self._opw00001(rqname, trcode)
        # 3.계좌평가잔고내역요청(opw00018)
        elif rqname == 'opw00018_req':
            self._opw00018(rqname, trcode)
        # 4.종목별기관매매추이요청(opt10045)
        elif rqname == 'opt10045_req':
            self._opt10045(rqname, trcode) 
        # 5.주식기본정보요청(opt10001)
        elif rqname == 'opt10001_req':
            self._opt10001(rqname, trcode)   

        try:
            self.tr_event_loop.exit()
        except AttributeError:
            pass

    #############
    # 수신결과 처리
    #############

    # 1.주식일봉차트조회(opt10081)
    def _opt10081(self, rqname, trcode):
        rows = self._get_repeat_cnt(trcode, rqname)

        for i in range(rows):            
            date = self._comm_get_data(trcode, '', rqname, i, '일자')
            open = self._comm_get_data(trcode, '', rqname, i, '시가')
            high = self._comm_get_data(trcode, '', rqname, i, '고가')
            low = self._comm_get_data(trcode, '', rqname, i, '저가')
            close = self._comm_get_data(trcode, '', rqname, i, '현재가')
            volume = self._comm_get_data(trcode, '', rqname, i, '거래량')

            self.ohlcv['date'].append(date)
            self.ohlcv['open'].append(int(open))
            self.ohlcv['high'].append(int(high))
            self.ohlcv['low'].append(int(low))
            self.ohlcv['close'].append(int(close))
            self.ohlcv['volume'].append(int(volume))

    # 2.예수금상세현황요청(opw00001)
    def _opw00001(self, rqname, trcode):
        d2_deposit = self._comm_get_data(trcode, "", rqname, 0, 'd+2추정예수금')
        self.d2_deposit = Kiwoom.change_format_comma(d2_deposit)

    # 3.계좌평가잔고내역요청(opw00018)
    def _opw00018(self, rqname, trcode):

        # single data
        total_purchase_price = self._comm_get_data(trcode, '', rqname, 0, "총매입금액")
        total_eval_price = self._comm_get_data(trcode, '', rqname, 0, '총평가금액')
        total_eval_profit_loss_price = self._comm_get_data(trcode, '', rqname, 0, '총평가손익금액')
        total_earning_rate = self._comm_get_data(trcode, '', rqname, 0, '총수익률(%)')
        total_earning_rate = float(total_earning_rate) / 100
        total_earning_rate = str(total_earning_rate)

        estimated_deposit = self._comm_get_data(trcode, '', rqname, 0, '추정예탁자산')
        
        self.opw00018_output['single'].append(Kiwoom.change_format_comma(total_purchase_price))
        self.opw00018_output['single'].append(Kiwoom.change_format_comma(total_eval_price))
        self.opw00018_output['single'].append(Kiwoom.change_format_comma(total_eval_profit_loss_price))
        self.opw00018_output['single'].append(Kiwoom.change_format_comma(total_earning_rate))
        self.opw00018_output['single'].append(Kiwoom.change_format_comma(estimated_deposit))

        # multi data
        rows = self._get_repeat_cnt(trcode, rqname)
        for i in range(rows):             
            name = self._comm_get_data(trcode, '', rqname, i, '종목명')
            quantity = self._comm_get_data(trcode, '', rqname, i, '보유수량')
            purchase_price = self._comm_get_data(trcode, '', rqname, i, '매입가')
            current_price = self._comm_get_data(trcode, '', rqname, i, '현재가')
            eval_profit_loss_price = self._comm_get_data(trcode, '', rqname, i, '평가손익')
            earning_rate = self._comm_get_data(trcode, '', rqname, i, '수익률(%)')            
            earning_rate = float(earning_rate) / 100
            earning_rate = str(earning_rate)

            quantity = Kiwoom.change_format_comma(quantity)
            purchase_price = Kiwoom.change_format_comma(purchase_price)
            current_price = Kiwoom.change_format_comma(current_price)
            eval_profit_loss_price = Kiwoom.change_format_comma(eval_profit_loss_price)
            earning_rate = Kiwoom.change_format_percent(earning_rate)

            self.opw00018_output['multi'].append([name, quantity, purchase_price, current_price, eval_profit_loss_price, earning_rate])

    # 3-1.데이터 초기화(계좌평가잔고내역요청(opw00018))
    def reset_opw00018_output(self):
        self.opw00018_output = {'single': [], 'multi': []}

    # 4.종목별기관매매추이요청(opt10045)
    def _opt10045(self, rqname, trcode):

        # single data
        agency_prediction_price = self._comm_get_data(trcode, '', rqname, 0, "기관추정평균가")
        foreign_prediction_price = self._comm_get_data(trcode, '', rqname, 0, '외인추정평균가')
        
        self.opt10045_output['single'].append(agency_prediction_price)
        self.opt10045_output['single'].append(foreign_prediction_price)

        # multi data
        rows = self._get_repeat_cnt(trcode, rqname)
        for i in range(rows):             
            date = self._comm_get_data(trcode, '', rqname, i, '일자')
            closing_price = self._comm_get_data(trcode, '', rqname, i, '종가')
            contrast_sign = self._comm_get_data(trcode, '', rqname, i, '대비기호')
            day_to_day = self._comm_get_data(trcode, '', rqname, i, '전일대비')
            fluctuation_rate = self._comm_get_data(trcode, '', rqname, i, '등략율')
            trading_volume = self._comm_get_data(trcode, '', rqname, i, '거래량')            
            accumulation_of_agency_period = self._comm_get_data(trcode, '', rqname, i, '기관기간누적')
            agency_net_trading_volume = self._comm_get_data(trcode, '', rqname, i, '기관일순매매수량')
            accumulation_of_foreign_period = self._comm_get_data(trcode, '', rqname, i, '외인기간누적')
            foreign_net_trading_volume = self._comm_get_data(trcode, '', rqname, i, '외인일순매매수량')
            limit_exhaustion_rate = self._comm_get_data(trcode, '', rqname, i, '한도소진율')

            self.opt10045_output['multi'].append([date, closing_price, contrast_sign, day_to_day, fluctuation_rate, 
                trading_volume, accumulation_of_agency_period, agency_net_trading_volume,accumulation_of_foreign_period,
                foreign_net_trading_volume,limit_exhaustion_rate])

    # 4-1.데이터 초기화(종목별기관매매추이요청(opt10045))
    def reset_opt10045_output(self):
        self.opt10045_output = {'single': [], 'multi': []}            

    # 5.주식기본정보요청(opt10001)
    def _opt10001(self, rqname, trcode):
        # single data
        stock_code = self._comm_get_data(trcode, '', rqname, 0, "종목코드")
        stock_name = self._comm_get_data(trcode, '', rqname, 0, '종목명')
        stock_market_cap = self._comm_get_data(trcode, '', rqname, 0, '시가총액')
        sales = self._comm_get_data(trcode, '', rqname, 0, '매출액')
        operating_profit = self._comm_get_data(trcode, '', rqname, 0, '영업이익')
        net_income = self._comm_get_data(trcode, '', rqname, 0, '당기순이익')

        self.opt10001_output['stock_code'].append(stock_code)
        self.opt10001_output['stock_name'].append(stock_name)
        self.opt10001_output['stock_market_cap'].append(stock_market_cap)
        self.opt10001_output['sales'].append(sales)
        self.opt10001_output['operating_profit'].append(operating_profit)
        self.opt10001_output['net_income'].append(net_income)

    #############
    # 거래
    #############
    def send_order(self, rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no):
        self.dynamicCall('SendOrder(QString, QString, QString, int, QString, int, int, QString, QString)', 
        [rqname, screen_no, acc_no, order_type, code, quantity, price, hoga, order_no])

    def get_chejan_data(self, fid):
        ret = self.dynamicCall('GetChejanData(int)', fid)
        return ret

    def _receive_chejan_data(self, gubun, item_cnt, fid_list):
        print(gubun)
        print(self.get_chejan_data(9203))
        print(self.get_chejan_data(302))
        print(self.get_chejan_data(900))
        print(self.get_chejan_data(901))  

    #############
    # 기타
    #############    
    @staticmethod
    def change_format_comma(data):
        strip_data = data.lstrip('-0')
        if strip_data == '':
            strip_data = '0'
        
        try:
            format_data = format(int(strip_data), ',d')
        except:
            format_data = format(float(strip_data))

        if data.startswith('-'):
            format_data = '-' + format_data

        return format_data

    @staticmethod
    def change_format_percent(data):
        strip_data = data.lstrip('-0')
        if strip_data == '':
            strip_data = '0'

        if strip_data.startswith('.'):
            strip_data = '0' + strip_data

        if data.startswith('-'):
            strip_data = '-' + strip_data

        return strip_data

    # 모의투자 / 실투자 구분
    def get_server_gubun(self):
        ret = self.dynamicCall("KOA_Functions(QString, QString)", "GetServerGubun", "")
        return ret

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     kiwoom = Kiwoom()
#     kiwoom.comm_connect()

#     account_number = kiwoom.get_login_info("ACCNO")
#     account_number = account_number.split(';')[3]
#     print(account_number)

#     kiwoom.set_input_value("계좌번호", account_number)
#     kiwoom.comm_rq_data("opw00018_req", "opw00018", 0, "2000")
    

