# _*_coding:utf-8_*_

import time
import sys
from func_tools import CreditFunc
from elems_select import Elems
from excel_info import PersonInfo
import re
import check_page

elem = Elems()
tool = CreditFunc()
print tool.page_dict_set(False, elem)["zhxx_div"]

sheet1 = tool.excel_read()
person_info = PersonInfo(sheet1, 0)
print int(person_info.dkye)
print round(person_info.dkye, 2)

print "window-1505".find("win", 0)
print "window" in "window-1505"