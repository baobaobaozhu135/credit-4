# _*_encoding:utf-8_*_
# excel中单行个人数据信息
class PersonInfo(object):
    def __init__(self, sheet1, i):
        self.hth = sheet1.cell(i, 0).value
        self.dkye = sheet1.cell(i, 1).value
        self.ydje = sheet1.cell(i, 2).value
        self.jkrmc = sheet1.cell(i, 3).value
        self.zjhm = sheet1.cell(i, 4).value
        self.ffr = sheet1.cell(i, 5).value
        self.dqr = sheet1.cell(i, 6).value
        self.dkll = sheet1.cell(i, 7).value
        self.xb = sheet1.cell(i, 8).value
        self.dz = sheet1.cell(i, 9).value
        self.poxm = sheet1.cell(i, 10).value
        self.pozjhm = sheet1.cell(i, 11).value
        self.hybm = sheet1.cell(i, 12).value
        self.dbrmc = sheet1.cell(i, 13).value
        self.dbrzjh = sheet1.cell(i, 14).value
        self.wjflxt = sheet1.cell(i, 15).value