import sys, os
from flask import Flask
from flask_restx import Api, Resource, reqparse

from router.saveHistoryRouter import SaveHist
from router.searchHistoryRouter import SearchHist


from PyQt5.QtWidgets import *

app = Flask(__name__)
api = Api(app, version='0.0.1', title='PyTrader', description='주식 분석 서비스')

if __name__ == '__main__':
    api.add_namespace(SearchHist, path="/search/hist")
    api.add_namespace(SaveHist, path="/save/hist")
    
    qt_app = QApplication(sys.argv)
    app.run(debug=True, host='0.0.0.0', port=5000)