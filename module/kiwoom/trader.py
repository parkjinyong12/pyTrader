from module.kiwoom.core import KWCore
from module.kiwoom.constants import KWErrorCode

from module.kiwoom.importer import *

class KWTrader(KWCore):

    def initialize(self):
        self.tr_list['opt10001'] = Opt10001(self)
        self.tr_list['opt10002'] = Opt10002(self)
        self.tr_list['opt10003'] = Opt10003(self)
        self.tr_list['opt10004'] = Opt10004(self)
        self.tr_list['opt10005'] = Opt10005(self)
        self.tr_list['opt10006'] = Opt10006(self)
        self.tr_list['opt10007'] = Opt10007(self)
        self.tr_list['opt10008'] = Opt10008(self)
        self.tr_list['opt10009'] = Opt10009(self)
        self.tr_list['opt10010'] = Opt10010(self)
        # self.tr_list['opt10011'] = Opt10011(self)     # opt10011 : Does not exist.
        self.tr_list['opt10012'] = Opt10012(self)
        self.tr_list['opt10013'] = Opt10013(self)
        self.tr_list['opt10014'] = Opt10014(self)
        self.tr_list['opt10015'] = Opt10015(self)
        self.tr_list['opt10016'] = Opt10016(self)
        self.tr_list['opt10017'] = Opt10017(self)
        self.tr_list['opt10018'] = Opt10018(self)
        self.tr_list['opt10019'] = Opt10019(self)
        self.tr_list['opt10020'] = Opt10020(self)
        self.tr_list['opt10021'] = Opt10021(self)
        self.tr_list['opt10022'] = Opt10022(self)
        self.tr_list['opt10023'] = Opt10023(self)
        self.tr_list['opt10024'] = Opt10024(self)
        self.tr_list['opt10025'] = Opt10025(self)
        self.tr_list['opt10026'] = Opt10026(self)
        self.tr_list['opt10027'] = Opt10027(self)
        self.tr_list['opt10028'] = Opt10028(self)
        self.tr_list['opt10029'] = Opt10029(self)
        self.tr_list['opt10030'] = Opt10030(self)
        self.tr_list['opt10031'] = Opt10031(self)
        self.tr_list['opt10032'] = Opt10032(self)
        self.tr_list['opt10033'] = Opt10033(self)
        self.tr_list['opt10034'] = Opt10034(self)
        self.tr_list['opt10035'] = Opt10035(self)
        self.tr_list['opt10036'] = Opt10036(self)
        self.tr_list['opt10037'] = Opt10037(self)
        self.tr_list['opt10038'] = Opt10038(self)
        self.tr_list['opt10039'] = Opt10039(self)
        self.tr_list['opt10040'] = Opt10040(self)
        self.tr_list['opt10041'] = Opt10041(self)
        self.tr_list['opt10042'] = Opt10042(self)
        self.tr_list['opt10043'] = Opt10043(self)
        self.tr_list['opt10044'] = Opt10044(self)
        self.tr_list['opt10045'] = Opt10045(self)
        self.tr_list['opt10046'] = Opt10046(self)
        self.tr_list['opt10047'] = Opt10047(self)
        self.tr_list['opt10048'] = Opt10048(self)
        self.tr_list['opt10049'] = Opt10049(self)
        self.tr_list['opt10050'] = Opt10050(self)
        self.tr_list['opt10051'] = Opt10051(self)
        self.tr_list['opt10052'] = Opt10052(self)
        self.tr_list['opt10053'] = Opt10053(self)
        # self.tr_list['opt10054'] = Opt10054(self)     # opt10054 : Does not exist.
        self.tr_list['opt10055'] = Opt10055(self)
        # self.tr_list['opt10056'] = Opt10056(self)     # opt10056 : Does not exist.
        # self.tr_list['opt10057'] = Opt10057(self)     # opt10057 : Does not exist.
        self.tr_list['opt10058'] = Opt10058(self)
        self.tr_list['opt10059'] = Opt10059(self)
        self.tr_list['opt10060'] = Opt10060(self)
        self.tr_list['opt10061'] = Opt10061(self)
        self.tr_list['opt10062'] = Opt10062(self)
        self.tr_list['opt10063'] = Opt10063(self)
        self.tr_list['opt10064'] = Opt10064(self)
        self.tr_list['opt10065'] = Opt10065(self)
        self.tr_list['opt10066'] = Opt10066(self)
        self.tr_list['opt10067'] = Opt10067(self)
        self.tr_list['opt10068'] = Opt10068(self)
        self.tr_list['opt10069'] = Opt10069(self)
        self.tr_list['opt10070'] = Opt10070(self)
        self.tr_list['opt10071'] = Opt10071(self)
        self.tr_list['opt10072'] = Opt10072(self)
        self.tr_list['opt10073'] = Opt10073(self)
        self.tr_list['opt10074'] = Opt10074(self)
        self.tr_list['opt10075'] = Opt10075(self)
        self.tr_list['opt10076'] = Opt10076(self)
        self.tr_list['opt10077'] = Opt10077(self)
        self.tr_list['opt10078'] = Opt10078(self)
        self.tr_list['opt10079'] = Opt10079(self)
        self.tr_list['opt10080'] = Opt10080(self)
        self.tr_list['opt10081'] = Opt10081(self)
        self.tr_list['opt10082'] = Opt10082(self)
        self.tr_list['opt10083'] = Opt10083(self)
        self.tr_list['opt10084'] = Opt10084(self)
        self.tr_list['opt10085'] = Opt10085(self)
        self.tr_list['opt10086'] = Opt10086(self)
        self.tr_list['opt10087'] = Opt10087(self)
        # self.tr_list['opt10088'] = Opt10088(self)     # opt10088 : Does not exist.
        # self.tr_list['opt10089'] = Opt10089(self)     # opt10089 : Does not exist.
        # self.tr_list['opt10090'] = Opt10090(self)     # opt10090 : Does not exist.
        # self.tr_list['opt10091'] = Opt10091(self)     # opt10091 : Does not exist.
        # self.tr_list['opt10092'] = Opt10092(self)     # opt10092 : Does not exist.
        # self.tr_list['opt10093'] = Opt10093(self)     # opt10093 : Does not exist.
        self.tr_list['opt10094'] = Opt10094(self)

        self.tr_list['opt20001'] = Opt20001(self)
        self.tr_list['opt20002'] = Opt20002(self)
        self.tr_list['opt20003'] = Opt20003(self)
        self.tr_list['opt20004'] = Opt20004(self)
        self.tr_list['opt20005'] = Opt20005(self)
        self.tr_list['opt20006'] = Opt20006(self)
        self.tr_list['opt20007'] = Opt20007(self)
        self.tr_list['opt20008'] = Opt20008(self)
        self.tr_list['opt20009'] = Opt20009(self)
        # self.tr_list['opt20010'] = Opt20010(self)     # opt10010 : Does not exist.
        # ...
        # self.tr_list['opt20018'] = Opt20018(self)     # opt10018 : Does not exist.
        self.tr_list['opt20019'] = Opt20019(self)
        # self.tr_list['opt20020'] = Opt20020(self)     # opt10020 : Does not exist.
        # ...
        # self.tr_list['opt20067'] = Opt20067(self)     # opt10067 : Does not exist.
        self.tr_list['opt20068'] = Opt20068(self)

        self.tr_list['opt30001'] = Opt30001(self)
        self.tr_list['opt30002'] = Opt30002(self)
        self.tr_list['opt30003'] = Opt30003(self)
        self.tr_list['opt30004'] = Opt30004(self)


    def connection(self):
        self.comm_connect()
        return self.response_connect_status


    # [ opt10001 : ???????????????????????? ]
    def opt10001(self, code, prev_next, screen_no):
        return self.tr_list['opt10001'].tr_opt(code, prev_next, screen_no)


    #  [ opt10002 : ????????????????????? ]
    def opt10002(self, code, prev_next, screen_no):
        return self.tr_list['opt10002'].tr_opt(code, prev_next, screen_no)


    #  [ opt10003 : ?????????????????? ]
    def opt10003(self, code, prev_next, screen_no):
        return self.tr_list['opt10003'].tr_opt(code, prev_next, screen_no)


    # [ opt10004 : ?????????????????? ]
    def opt10004(self, code, prev_next, screen_no):
        return self.tr_list['opt10004'].tr_opt(code, prev_next, screen_no)


    # [ opt10005 : ??????????????????????????? ]
    def opt10005(self, code, prev_next, screen_no):
        return self.tr_list['opt10005'].tr_opt(code, prev_next, screen_no)


    # [ OPT10006 : ?????????????????? ]
    def opt10006(self, code, prev_next, screen_no):
        return self.tr_list['opt10006'].tr_opt(code, prev_next, screen_no)


    # [ opt10007 : ???????????????????????? ]
    def opt10007(self, code, prev_next, screen_no):
        return self.tr_list['opt10007'].tr_opt(code, prev_next, screen_no)


    # [ opt10008 : ???????????????????????? ]
    def opt10008(self, code, prev_next, screen_no):
        return self.tr_list['opt10008'].tr_opt(code, prev_next, screen_no)


    # [ OPT10009 : ?????????????????? ]
    def opt10009(self, code, prev_next, screen_no):
        return self.tr_list['opt10009'].tr_opt(code, prev_next, screen_no)


    # [ OPT10010 : ???????????????????????? ]
    def opt10010(self, code, prev_next, screen_no):
        return self.tr_list['opt10010'].tr_opt(code, prev_next, screen_no)


    # [ opt10012 : ?????????????????? ]
    def opt10012(self, code, prev_next, screen_no):
        return self.tr_list['opt10012'].tr_opt(code, prev_next, screen_no)


    # [ opt10013 : ???????????????????????? ]
    def opt10013(self, code, date, type_flag, prev_next, screen_no):
        return self.tr_list['opt10013'].tr_opt(code, date, type_flag, prev_next, screen_no)


    # [ opt10014 : ????????????????????? ]
    def opt10014(self, code, date_type, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10014'].tr_opt(code, date_type, date_from, date_to, prev_next, screen_no)


    # [ opt10015 : ???????????????????????? ]
    def opt10015(self, code, date, prev_next, screen_no):
        return self.tr_list['opt10015'].tr_opt(code, date, prev_next, screen_no)


    # [ OPT10016 : ?????????????????? ]
    def opt10016(self, market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no):
        return self.tr_list['opt10016'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, date, prev_next, screen_no)


    # [ opt10017 : ?????????????????? ]
    def opt10017(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10017'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10018 : ????????????????????? ]
    def opt10018(self, input0, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10018'].tr_opt(input0, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ opt10019 : ????????????????????? ]
    def opt10019(self, market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no):
        return self.tr_list['opt10019'].tr_opt(market_type, input1, date_type, date, input4, input5, input6, input7, input8, prev_next, screen_no)


    # [ OPT10020 : ???????????????????????? ]
    def opt10020(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10020'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10021 : ???????????????????????? ]
    def opt10021(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10021'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10022 : ????????????????????? ]
    def opt10022(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10022'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10023 : ????????????????????? ]
    def opt10023(self, market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10023'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ OPT10024 : ????????????????????? ]
    def opt10024(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10024'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10025 : ????????????????????? ]
    def opt10025(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10025'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10026 : ??????PER?????? ]
    def opt10026(self, per_type, prev_next, screen_no):
        return self.tr_list['opt10026'].tr_opt(per_type, prev_next, screen_no)


    # [ opt10027 : ????????????????????????????????? ]
    def opt10027(self, market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10027'].tr_opt(market_type, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ opt10028 : ??????????????????????????? ]
    def opt10028(self, input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10028'].tr_opt(input0, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ OPT10029 : ????????????????????????????????? ]
    def opt10029(self, market_type, input1, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10029'].tr_opt(market_type, input1, input2, input3, input4, input5, prev_next, screen_no)


    # [ OPT10030 : ??????????????????????????? ]
    def opt10030(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10030'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10031 : ??????????????????????????? ]
    def opt10031(self, market_type, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10031'].tr_opt(market_type, input1, input2, input3, prev_next, screen_no)


    # [ OPT10032 : ???????????????????????? ]
    def opt10032(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10032'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10033 : ???????????????????????? ]
    def opt10033(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10033'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10034 : ????????????????????????????????? ]
    def opt10034(self,  market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10034'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10035 : ????????????????????????????????? ]
    def opt10035(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10035'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ OPT10036 : ?????????????????? ]
    def opt10036(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt10036'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt10037 : ????????????????????????????????? ]
    def opt10037(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10037'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10038 : ?????????????????????????????? ]
    def opt10038(self, code, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10038'].tr_opt(code, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT10039 : ?????????????????????????????? ]
    def opt10039(self, input0, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10039'].tr_opt(input0, input1, input2, input3, prev_next, screen_no)


    # [ opt10040 : ??????????????????????????? ]
    def opt10040(self, code, prev_next, screen_no):
        return self.tr_list['opt10040'].tr_opt(code, prev_next, screen_no)


    # [ opt10041 : ?????????????????????????????? ]
    def opt10041(self, code, input1, prev_next, screen_no):
        return self.tr_list['opt10041'].tr_opt(code, input1, prev_next, screen_no)


    # [ opt10042 : ?????????????????????????????? ]
    def opt10042(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10042'].tr_opt(code, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ opt10043 : ?????????????????????????????? ]
    def opt10043(self, code, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no):
        return self.tr_list['opt10043'].tr_opt(code, input1, input2, input3, input4, input5, input6, input7, prev_next, screen_no)


    # [ OPT10044 : ?????????????????????????????? ]
    def opt10044(self, input0, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10044'].tr_opt(input0, input1, input2, input3, prev_next, screen_no)


    # [ opt10045 : ????????????????????????????????? ]
    def opt10045(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10045'].tr_opt(code, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ opt10046 : ????????????????????????????????? ]
    def opt10046(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10046'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ opt10047 : ?????????????????????????????? ]
    def opt10047(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10047'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ OPT10048 : ELW??????????????????????????? ]
    def opt10048(self, code, prev_next, screen_no):
        return self.tr_list['opt10048'].tr_opt(code, prev_next, screen_no)


    # [ OPT10049 : ELW?????????????????? ]
    def opt10049(self, input0, input1, code, prev_next, screen_no):
        return self.tr_list['opt10049'].tr_opt(input0, input1, code, prev_next, screen_no)


    # [ OPT10050 : ELW????????????????????? ]
    def opt10050(self, code, prev_next, screen_no):
        return self.tr_list['opt10050'].tr_opt(code, prev_next, screen_no)


    # [ OPT10051 : ????????????????????????????????? ]
    def opt10051(self, market_type, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10051'].tr_opt(market_type, input1, input2, prev_next, screen_no)


    # [ opt10052 : ?????????????????????????????? ]
    def opt10052(self, input0, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10052'].tr_opt(input0, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10053 : ??????????????????????????? ]
    def opt10053(self, code, prev_next, screen_no):
        return self.tr_list['opt10053'].tr_opt(code, prev_next, screen_no)


    # [ opt10055 : ?????????????????????????????? ]
    def opt10055(self, code, input1, prev_next, screen_no):
        return self.tr_list['opt10055'].tr_opt(code, input1, prev_next, screen_no)


    # [ OPT10058 : ???????????????????????????????????? ]
    def opt10058(self, from_date, to_date, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10058'].tr_opt(from_date, to_date, input2, input3, input4, prev_next, screen_no)


    # [ opt10059 : ????????????????????????????????? ]
    def opt10059(self, date, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10059'].tr_opt(date, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10060 : ??????????????????????????????????????? ]
    def opt10060(self, date, code, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10060'].tr_opt(date, code, input2, input3, input4, prev_next, screen_no)


    # [ opt10061 : ??????????????????????????????????????? ]
    def opt10061(self, code, date_from, date_to, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10061'].tr_opt(code, date_from, date_to, input3, input4, input5, prev_next, screen_no)


    # [ opt10062 : ??????????????????????????? ]
    def opt10062(self, date_from, date_to, input2, input3, input4, input5, prev_next, screen_no):
        return self.tr_list['opt10062'].tr_opt(date_from, date_to, input2, input3, input4, input5, prev_next, screen_no)


    # [ opt10063 : ?????????????????????????????? ]
    def opt10063(self, market_type, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt10063'].tr_opt(market_type, input1, input2, input3, input4, prev_next, screen_no)


    # [ opt10064 : ???????????????????????????????????? ]
    def opt10064(self, market_type, input1, input2, code, prev_next, screen_no):
        return self.tr_list['opt10064'].tr_opt(market_type, input1, input2, code, prev_next, screen_no)


    # [ OPT10065 : ???????????????????????????????????? ]
    def opt10065(self, input0, market_type, input2, prev_next, screen_no):
        return self.tr_list['opt10065'].tr_opt(input0, market_type, input2, prev_next, screen_no)


    # [ opt10066 : ???????????????????????????????????? ]
    def opt10066(self, market_type, input1, input2, code, prev_next, screen_no):
        return self.tr_list['opt10066'].tr_opt(market_type, input1, input2, code, prev_next, screen_no)


    # [ OPT10067 : ???????????????????????? ]
    def opt10067(self, date, market_type, prev_next, screen_no):
        return self.tr_list['opt10067'].tr_opt(date, market_type, prev_next, screen_no)


    # [ OPT10068 : ???????????????????????? ]
    def opt10068(self, date_from, date_to, input2, code, prev_next, screen_no):
        return self.tr_list['opt10068'].tr_opt(date_from, date_to, input2, code, prev_next, screen_no)


    # [ OPT10069 : ??????????????????10???????????? ]
    def opt10069(self, date_from, date_to, market_type, prev_next, screen_no):
        return self.tr_list['opt10069'].tr_opt(date_from, date_to, market_type, prev_next, screen_no)


    # [ opt10070 : ??????????????????????????? ]
    def opt10070(self, code, prev_next, screen_no):
        return self.tr_list['opt10070'].tr_opt(code, prev_next, screen_no)


    # [ OPT10071 : ??????????????????????????????????????? ]
    def opt10071(self, code, date_type, prev_next, screen_no):
        return self.tr_list['opt10071'].tr_opt(code, date_type, prev_next, screen_no)


    # [ OPT10072 : ???????????????????????????????????? ]
    def opt10072(self, input0, code, date_from, prev_next, screen_no):
        return self.tr_list['opt10072'].tr_opt(input0, code, date_from, prev_next, screen_no)


    # [ opt10073 : ???????????????????????????????????? ]
    def opt10073(self, input0, code, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10073'].tr_opt(input0, code, date_from, date_to, prev_next, screen_no)


    # [ opt10074 : ??????????????????????????? ]
    def opt10074(self, input0, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10074'].tr_opt(input0, date_from, date_to, prev_next, screen_no)


    # [ opt10075 : ???????????????????????? ]
    def opt10075(self, input0, input1, input2, code, input4, prev_next, screen_no):
        return self.tr_list['opt10075'].tr_opt(input0, input1, input2, code, input4, prev_next, screen_no)


    # [ opt10076 : ????????????????????? ]
    def opt10076(self, code, input1, input2, input3, input4, input5, input6, prev_next, screen_no):
        return self.tr_list['opt10076'].tr_opt(code, input1, input2, input3, input4, input5, input6, prev_next, screen_no)


    # [ opt10077 : ?????????????????????????????? ]
    def opt10077(self, input0, input1, code, prev_next, screen_no):
        return self.tr_list['opt10077'].tr_opt(input0, input1, code, prev_next, screen_no)


    # [ OPT10078 : ???????????????????????????????????? ]
    def opt10078(self, input0, code, date_from, date_to, prev_next, screen_no):
        return self.tr_list['opt10078'].tr_opt(input0, code, date_from, date_to, prev_next, screen_no)


    # [ opt10079 : ??????????????????????????? ]
    def opt10079(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10079'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ opt10080 : ?????????????????????????????? ]
    def opt10080(self, code, tick_range, input2, prev_next, screen_no):
        return self.tr_list['opt10080'].tr_opt(code, tick_range, input2, prev_next, screen_no)


    # [ opt10081 : ?????????????????????????????? ]
    def opt10081(self, code, date_from, input2, prev_next, screen_no):
        return self.tr_list['opt10081'].tr_opt(code, date_from, input2, prev_next, screen_no)


    # [ opt10082 : ?????????????????????????????? ]
    def opt10082(self, code, date_from, date_to, input3, prev_next, screen_no):
        return self.tr_list['opt10082'].tr_opt(code, date_from, date_to, input3, prev_next, screen_no)


    # [ opt10083 : ?????????????????????????????? ]
    def opt10083(self, code, date_from, date_to, input3, prev_next, screen_no):
        return self.tr_list['opt10083'].tr_opt(code, date_from, date_to, input3, prev_next, screen_no)


    # [ opt10084 : ???????????????????????? ]
    def opt10084(self, code, input1, input2, input3, prev_next, screen_no):
        return self.tr_list['opt10084'].tr_opt(code, input1, input2, input3, prev_next, screen_no)


    # [ opt10085 : ????????????????????? ]
    def opt10085(self, input0, prev_next, screen_no):
        return self.tr_list['opt10085'].tr_opt(input0, prev_next, screen_no)


    # [ opt10086 : ?????????????????? ]
    def opt10086(self, code, input1, input2, prev_next, screen_no):
        return self.tr_list['opt10086'].tr_opt(code, input1, input2, prev_next, screen_no)


    # [ opt10087 : ???????????????????????? ]
    def opt10087(self, code, prev_next, screen_no):
        return self.tr_list['opt10087'].tr_opt(code, prev_next, screen_no)


    # [ opt10094 : ?????????????????????????????? ]
    def opt10094(self, code, date_from, date_to, input3, prev_next, screen_no):
        return self.tr_list['opt10094'].tr_opt(code, date_from, date_to, input3, prev_next, screen_no)


    # [ opt20001 : ????????????????????? ]
    def opt20001(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt20001'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ OPT20002 : ????????????????????? ]
    def opt20002(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt20002'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt20003 : ????????????????????? ]
    def opt20003(self, input0, prev_next, screen_no):
        return self.tr_list['opt20003'].tr_opt(input0, prev_next, screen_no)


    # [ opt20004 : ??????????????????????????? ]
    def opt20004(self, input0, tick_range, prev_next, screen_no):
        return self.tr_list['opt20004'].tr_opt(input0, tick_range, prev_next, screen_no)


    # [ opt20005 : ???????????????????????? ]
    def opt20005(self, input0, tick_range, prev_next, screen_no):
        return self.tr_list['opt20005'].tr_opt(input0, tick_range, prev_next, screen_no)


    # [ opt20006 : ???????????????????????? ]
    def opt20006(self, input0, input1, prev_next, screen_no):
        return self.tr_list['opt20006'].tr_opt(input0, input1, prev_next, screen_no)


    # [ opt20007 : ???????????????????????? ]
    def opt20007(self, input0, tick_range, prev_next, screen_no):
        return self.tr_list['opt20007'].tr_opt(input0, tick_range, prev_next, screen_no)


    # [ opt20008 : ???????????????????????? ]
    def opt20008(self, input0, input1, prev_next, screen_no):
        return self.tr_list['opt20008'].tr_opt(input0, input1, prev_next, screen_no)


    # [ opt20009 : ??????????????????????????? ]
    def opt20009(self, market_type, input1, prev_next, screen_no):
        return self.tr_list['opt20009'].tr_opt(market_type, input1, prev_next, screen_no)


    # [ opt20019 : ???????????????????????? ]
    def opt20019(self, input0, input1, prev_next, screen_no):
        return self.tr_list['opt20019'].tr_opt(input0, input1, prev_next, screen_no)


    # [ opt20068 : ????????????????????????(?????????) ]
    def opt20068(self, date_from, date_to, input2, code, prev_next, screen_no):
        return self.tr_list['opt20068'].tr_opt(date_from, date_to, input2, code, prev_next, screen_no)


    # [ OPT30001 : ELW????????????????????? ]
    def opt30001(self, input0, input1, input2, input3, input4, input5, input6, input7, input8, prev_next, screen_no):
        return self.tr_list['opt30001'].tr_opt(input0, input1, input2, input3, input4, input5, input6, input7, input8, prev_next, screen_no)


    # [ OPT30002 : ????????????ELW????????????????????? ]
    def opt30002(self, input0, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt30002'].tr_opt(input0, input1, input2, input3, input4, prev_next, screen_no)


    # [ OPT30003 : ELWLP???????????????????????? ]
    def opt30003(self, input0, input1, prev_next, screen_no):
        return self.tr_list['opt30003'].tr_opt(input0, input1, prev_next, screen_no)


    # [ OPT30004 : ELW??????????????? ]
    def opt30004(self, input0, input1, input2, input3, input4, prev_next, screen_no):
        return self.tr_list['opt30004'].tr_opt(input0, input1, input2, input3, input4, prev_next, screen_no)
