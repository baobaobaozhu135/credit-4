# _*_coding:utf-8_*_

import xlrd
import xlwt
from selenium import webdriver
import time
import sys
from func_tools import CreditFunc
from elems_select import Elems
from excel_info import PersonInfo


if __name__ == "__main__":
    tool = CreditFunc()
    elem = Elems()  # 实例化Elems
    """ 打开excel做准备 """
    sheet1 = tool.excel_read()
    if sheet1.nrows < 2:
        print u"文件内容为空，请检查"
        sys.exit()
    """ 登录 （验证码、登录点击、usb-key需手动），进入个人贷款页面 """
    driver = tool.login()
    driver.implicitly_wait(tool.time_out)
    """ 个人贷款上报第一个页面 """
    driver.find_element_by_id(elem.person_manage_select_id).click()  # 个人上报按钮select
    driver.implicitly_wait(1)
    driver.find_element_by_id(elem.person_manage_select_option_id).click()  # 个人上报按钮option
    driver.implicitly_wait(tool.time_out)
    iframe = driver.find_element_by_css_selector(elem.iframe_css)
    driver.switch_to.frame(iframe)  # 切换到frame
    time.sleep(3)  # 等待3秒钟，数据刷新
    i = 0
    person_info = PersonInfo(sheet1, i)  # 实例化一个借款人信息
    driver.find_element_by_id(elem.hth_input_id).clear()
    driver.find_element_by_id(elem.name_input_id).clear()
    driver.find_element_by_id(elem.hth_input_id).send_keys(person_info.hth)  # 账号输入待查询
    driver.find_element_by_id(elem.name_input_id).send_keys(person_info.jkrmc)  # 姓名输入待查询
    driver.find_element_by_id(elem.query_btn_id).click()  # 点击查询
    refresh_result = tool.data_is_refresh(driver, elem.loading_id)  # 循环查询数据行是否刷新
    if refresh_result:
        if len(driver.find_elements_by_css_selector(elem.data_tr_css)) == 2:  # 数据行至少有一个空
            data_hth = driver.find_element_by_css_selector(elem.data_tr_hth_css).text  # 数据行业务号
            data_name = driver.find_element_by_css_selector(elem.data_tr_name_css).text  # 数据行姓名
            if data_hth == person_info.hth and data_name == person_info.jkrmc:
                driver.find_element_by_css_selector(elem.data_checkbox_css).click()  # 点击checkbox
                # tr  class属性判断是否已经选中
                is_select = driver.find_element_by_css_selector(elem.check_is_select_by_class_css).get_attribute("class")
                if "x-grid-row-selected" in is_select:
                    driver.find_element_by_id(elem.begin_fill_btn_id).click()
                    time.sleep(2)
            else:
                print u"账号：" + person_info.hth + u",姓名：" + person_info.jkrmc + u"，互联网数据和五级分类不匹配！"
        else:
            print u"账号：" + person_info.hth + u",姓名：" + person_info.jkrmc + u"，未找到！"
    else:
        print u"程序故障，请检查循环查找数据好"
        sys.exit()
    """ 贷款开户信息 """




