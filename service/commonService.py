import sys

class CommonService:

    def __init__(self):
        self.setFilePath()
        print("hello CommonService..")

    def update_logger(self, logger):
        f = open(self.filePath["log"], 'a+', encoding='utf-8')
        for log in logger:
            f.writelines(log)

        f.close()

    # 파일 경로 지정
    def setFilePath(self):
        self.filePath = {}
        self.filePath["buyList"] = 'C:\\Trading\\doc\\buy_list.txt'
        self.filePath["sellList"] = 'C:\\Trading\\doc\\sell_list.txt'
        self.filePath["log"] = 'C:\\Trading\\doc\\trading.log'