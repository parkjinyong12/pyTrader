import sys
import time
from datetime import datetime, timedelta
import pandas as pd
from PyQt5.QtWidgets import *
import exchange_calendars as xcals

from handler.findStocksHandler import FindStocksHandler
from router.saveHistoryRouter import SaveHistoryRouter
from router.searchHistoryRouter import SearchHistoryRouter

class PyMon:
    def __init__(self):
        print("hello PyMon..")

if __name__ == '__main__':
    sys_argv = sys.argv
    app = QApplication(sys_argv)

    save_hist = "/save/hist"
    search_hist = "/search/hist"

    # URL 라우팅
    if(len(sys_argv) > 1):
        path = sys_argv[1]
        if(path.startswith(save_hist)):
            SaveHistoryRouter().do_route(path[(len(save_hist)):])
            pass
        elif(path.startswith(search_hist)):
            SearchHistoryRouter().do_route(path[(len(search_hist)):])
            pass
        else:
            pass
    else:
        pass

    # findStock = FindStocksHandler()
    # findStock.check_price_market_trend("KOSPI", 0, 20)
    # findStock.check_price_market_trend("KOSPI", 1, 20)
    # findStock.check_price_market_trend("KOSDAQ", 0, 20)
    # findStock.check_price_market_trend("KOSDAQ", 1, 20)
    # cal = CalculateService()
    # cal.get_start_end_day("20220128",10)
    print("test completed..")   