from handler.stockSearchHandler import StockSearchHandler
from handler.kiwoomSaveHandler import KiwoomSaveHandler

from flask_restx import Namespace, Resource
from flask import request

SearchHist = Namespace(name='search_hist',description="이력 조회 서비스")

@SearchHist.route("/stock/daliy")
class StockDaliy(Resource):
    @SearchHist.param("end_day")
    def get(self):
        """ 기관매매추이 분석 """
        end_day = request.args.get("end_day")
        StockSearchHandler().search_agency_trading_trend(end_day)
        return "success"

@SearchHist.route("/adjust")
class Adjust(Resource):
    def get(self):
        """ 기간 순매수 누적합계 조정 """
        StockSearchHandler().adjust_accumulation()
        return "success"
