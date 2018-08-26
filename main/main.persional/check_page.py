# _*_encoding:utf-8_*_
import re
import sys
import time
from func_tools import CreditFunc
from elems_select import Elems
tool = CreditFunc()
elem = Elems()


def khxx(driver, elem, person_info):
    """ 贷款开户信息 """
    if driver.find_element_by_css_selector(elem.tab_1_css).text == u"贷款开户信息":
        data_ffr = driver.find_element_by_id(elem.ffr_id).text
        data_dqr_input = driver.find_element_by_id(elem.dqr_id)
        # data_dqr_style = data_dqr_input.get_attribute("style")   #width: 100%; -moz-user-select: text;
        # data_is_find = re.findall("\d{4}\-\d{2}\-\d{2}", data_dqr_input)
        data_dqr = data_dqr_input.get_attribute("value")
        # print data_ffr
        # print person_info.ffr
        # print data_dqr
        # print person_info.dqr
        # if len(data_is_find) == 1:
        if data_dqr != person_info.dqr or data_ffr != person_info.ffr:
            print u"账号：" + person_info.hth + u",姓名：" + person_info.jkrmc + u"，开户日和到期日不匹配！"
            # TODO 直接下一次循环
        # 点击下一步
        time.sleep(5)
        driver.find_element_by_css_selector(elem.page_1).find_element_by_css_selector(elem.next_btn_css).click()

    else:
        print u"未找到个人贷款开户信息"
    print u"贷款开户信息结束"
def dbxx(driver, person_info, div_css):
    """ 担保信息 """

    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_css).click()
def jkrxx(driver, person_info, div_css):
    """ 借款人信息 """



    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_jkrxx_css).click()
def zhxx(driver, person_info, div_css):
    """ 账户信息 """

    driver.find_element_by_css_selector(elem.khr_scc).send_keys(tool.current_date)  # 还款日
    driver.find_element_by_css_selector(elem.ye_css).send_keys(int(round(person_info.dkye)))  # 贷款余额 TODO
    driver.find_element_by_css_selector(elem.wjfl).click()  # 点击五级分类
    time.sleep(2)
    divs = driver.find_elements_by_css_selector(elem.flag_divs_css)
    divs_index = len(divs) - 1
    divs[divs_index].find_element_by_css_selector("div>ul>li:nth-child(1)").click()         # 不好定位，所以定位到div最后一个  “”
    # driver.find_element_by_css_selector(elem.wjfl_option_css).click()
    # if tool.data_is_refresh(driver, elem.wjfl_option_div_css):
    #     driver.find_element_by_css_selector(elem.zhzt).click()
    # if tool.data_is_refresh(driver, elem.zhzt_option_div_css):
    #     driver.find_element_by_css_selector(elem.zhzt_option_css).click()
    time.sleep(1)
    driver.find_element_by_css_selector(elem.zhzt).click()
    time.sleep(1)
    divs = driver.find_elements_by_css_selector(elem.flag_divs_css)
    divs_index = len(divs) - 1
    divs[divs_index].find_element_by_css_selector("div>ul>li:nth-child(1)").click()
    # driver.find_element_by_css_selector(elem.zhzt_option_css).click()
    time.sleep(1)
    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_css).click()
def hkxx(driver, person_info, div_css):
    """ 还款信息 """

    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_css).click()
def hklsxx(driver, person_info, div_css):
    """ 还款流水信息 """

    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_css).click()
def tsxx(driver, person_info, div_css):
    """ 特殊信息 """

    driver.find_element_by_css_selector(div_css).find_element_by_css_selector(elem.next_btn_css).click()

def byjs(driver):
    """ 本月结算 """
    time.sleep(2)
    divs = driver.find_elements_by_css_selector(elem.flag_divs_css)
    for div in divs:
        if div.get_attribute("id").find("window") > -1:
            # print div.find_element_by_css_selector(elem.byjs_btn_css).find_element_by_css_selector("span:nth-child(1)").text
            break


    # divs_index = len(divs) - 1
    # print divs[divs_index].get_attribute("id")
    # if divs[divs_index].get_attribute("id").find("window") > 0:
    #     print divs[divs_index].find_element_by_css_selectot(elem.byjs_btn_css).\
    #         find_element_by_css_selector("span:nth-child(2)").text
