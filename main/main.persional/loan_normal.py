# _*_coding:utf-8_*_

import xlrd
import xlwt
from selenium import webdriver
import time
import sys
from func_tools import CreditFunc
from elems_select import Elems
from excel_info import PersonInfo
import re
import check_page


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
    refresh_result = tool.data_is_refresh(driver, elem.loading_css)  # 循环查询数据行是否刷新
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
                    # time.sleep(5)
            else:
                print u"账号：" + person_info.hth + u",姓名：" + person_info.jkrmc + u"，互联网数据和五级分类不匹配！"
        else:
            print u"账号：" + person_info.hth + u",姓名：" + person_info.jkrmc + u"，未找到！"
    else:
        print u"程序故障，请检查循环查找数据好"
        sys.exit()
    """ 贷款开户信息 """
    check_page.khxx(driver, elem, person_info)
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 担保信息 """
    has_db = True  # 是否有担保信息
    div_index = 1  # 用于统计page个数
    if tool.find_page_count(driver, elem.page_parent, 2):  # 等待出来两个div时，页面已经刷新
        tab2_text = driver.find_element_by_css_selector(elem.tab_2_css).text
        if tab2_text != u"担保信息":
            has_db = False
            print has_db
    page_dict = tool.page_dict_set(has_db, elem)
    if has_db:
        div_index += 1
        check_page.dbxx(driver, person_info, page_dict.get("dbxx_div"))
        time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 借款人信息 """
    div_index += 1
    if tool.find_page_count(driver, elem.page_parent, div_index):
        tab_text = driver.find_element_by_css_selector(page_dict.get("jkrxx_tab")).text
        if tab_text == u"借款人基本信息":
            check_page.jkrxx(driver, person_info, page_dict.get("jkrxx_div"))
        else:
            print u"找不到借款人信息"
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息

    """ 账户信息 """
    div_index += 1
    if tool.find_page_count(driver, elem.page_parent, div_index):
        tab_text = driver.find_element_by_css_selector(page_dict.get("zhxx_tab")).text
        if tab_text == u"账户信息":
            check_page.zhxx(driver, person_info, page_dict.get("zhxx_div"))
        else:
            print u"找不到账户信息"
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 还款信息 """
    div_index += 1
    if tool.find_page_count(driver, elem.page_parent, div_index):
        tab_text = driver.find_element_by_css_selector(page_dict.get("hkxx_tab")).text
        if tab_text == u"还款信息":
            check_page.hkxx(driver, person_info, page_dict.get("hkxx_div"))
        else:
            print u"找不到还款信息"
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 还款流水信息 """
    div_index += 1
    if tool.find_page_count(driver, elem.page_parent, div_index):
        tab_text = driver.find_element_by_css_selector(page_dict.get("hklsxx_tab")).text
        if tab_text == u"还款流水信息":
            check_page.hklsxx(driver, person_info, page_dict.get("hklsxx_div"))
        else:
            print u"找不到还款流水信息"
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 特殊信息 """
    div_index += 1
    if tool.find_page_count(driver, elem.page_parent, div_index):
        tab_text = driver.find_element_by_css_selector(page_dict.get("tsxx_tab")).text
        if tab_text == u"特殊交易信息":
            check_page.tsxx(driver, person_info, page_dict.get("tsxx_div"))
        else:
            print u"找不到特殊信息"
    time.sleep(2)  # 等待系统缓冲  有时会出现页面出现上一个借款人信息
    """ 本月结算 """
    check_page.byjs(driver)