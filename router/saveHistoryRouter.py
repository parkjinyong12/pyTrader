from handler.kiwoomSaveHandler import KiwoomSaveHandler

from flask_restx import Namespace, Resource
from flask import request

SaveHist = Namespace(name='save_hist',description="이력 저장 서비스")

@SaveHist.route("/stock/daliy")
class StockDaliy(Resource):
    def get(self):
        """ 기관 순매수 추이 저장 """
        KiwoomSaveHandler().save_agency_trading_trend()
        KiwoomSaveHandler().save_bagic_stock_info()
        return "success"

@SaveHist.route("/stock/bagicinfo")
class StockDaliy(Resource):
    def get(self):
        """ 종목기초정보 저장 """
        KiwoomSaveHandler().save_bagic_stock_info()
        return "success"

@SaveHist.route("/stock/code")
class StockCode(Resource):
    def get(self):
        """ 종목코드정보 저장 """
        KiwoomSaveHandler().save_stock_code_list()
        return "success"