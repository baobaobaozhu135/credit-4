# encoding:utf-8
# file : func_tools.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# xlrd excel读模块   xlwt:excel 写模块
import xlrd
import time
import threading
import sys


class CreditFunc:
    def __init__(self):
        # 登录参数
        self.user_name = "shy-jphshczhyh-lyw"
        self.password = "czyh2017"
        self.url = "https://msi.pbccrc.org.cn/html/login.html"
        self.time_out = 30
        #表格参数
        self.file_path = ur"F:\征信自动录入\正常录入贷款.xlsx"

    # 登录网址
    def login(self):
        # 配置文件地址
        profile_directory = r"C:\Users\LJY\AppData\Roaming\Mozilla\Firefox\Profiles\rhp7jus5.default"
        #加载配置文件
        profile = webdriver.FirefoxProfile(profile_directory)
        driver = webdriver.Firefox(profile)
        driver.implicitly_wait(self.time_out)
        driver.get(self.url)
        driver.implicitly_wait(self.time_out)
        driver.find_element_by_id("susername").clear()
        driver.find_element_by_id("spassword").clear()
        driver.find_element_by_id("susername").send_keys(self.user_name)
        driver.find_element_by_id("spassword").send_keys(self.password)
        # 验证码输入，暂不能自动实现
        # vcode = input("对控件进行允许并输入验证码：")
        # driver.find_element_by_id("vcode").send_keys(vcode)
        # 点击登录
        # driver.find_element_by_id("btn1").click()
        # d river.implicitly_wait(30)
        # 输入usbkey密码，暂时不能实现
        # t = driver.switch_to.alert().send_keys("654321")
        # t.accept()
        return driver

    def excel_read(self):
        try:
            # workbook = xlrd.open_workbook(r"F:\征信自动录入\正常录入贷款.xlsx")
            workbook = xlrd.open_workbook(self.file_path)
            if workbook._all_sheets_count > 3:
                print("sheet1数量大于1，请检查！")
                # 不需要关闭文件对象，workfile文件对象没有close()方法
            return workbook.sheet_by_index(0)
        except IOError:
            print("未能打开excel,请检查文件路径。")
        else:
            print("文件打开正常")
        return workbook

    # args:driver = driver  id:css_selector id   max_seconds:最多查找多少秒，默认20秒
    def data_is_refresh(self, driver, css_id, max_seconds=20):
        is_display = driver.find_element_by_id(css_id).get_attribute("style")
        if (is_display + "").find("display: none") < 0:  # display属性是none  找不到一直找 index找不到会报错
            time.sleep(1)
            max_seconds = max_seconds - 1
            if max_seconds < 0:
                return False
            else:
                return self.data_is_refresh(driver, css_id, max_seconds)
        else:
            return True


    """
    def data_is_refresh(self, driver, tool):
        is_display = driver.find_element_by_id("loadmask-1902").get_attribute("style")
        print is_display
        print type(is_display)
        if (is_display + "").find("display: none") < 0:  # display属性是none  找不到一直找 index找不到会报错
            threading.Timer(3, tool.data_is_refresh(driver, tool)).start()
        else:
            return True
    """



