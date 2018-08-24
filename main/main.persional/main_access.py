# _*_encoding:utf-8 _*_
import xlrd
import tools
if __name__ == "__main__":
    tool = CreditFunc()
    sheet1 = tool.excel_read()
    rowCount = sheet1.nrows
    if rowCount > 1:
        # 登录网址
        driver = tool.login()
        # 进入个人贷款录入界面
        driver.implicitly_wait(tool.time_out)
        # WebDriverWait(driver, 10).until(  # 个人贷款页面可以被点击时（不好用）
            # EC.element_to_be_clickable(By.ID, "button-1040-btnEl")
        # )
        driver.find_element_by_id("button-1040-btnEl").click()
        driver.implicitly_wait(1)
        driver.find_element_by_id("menuitem-1037-textEl").click()  # 点击上报贷款业务
        driver.implicitly_wait(tool.time_out)

        # 切换到frame# 这种方式找到两个以上iframe，不知道原因
        # WebDriverWait(driver, 10).until(  # 找到个人贷款业务frame，等到frame可以被切换时切换
            # EC.frame_to_be_available_and_switch_to_it(By.CSS_SELECTOR, "#panel-1058>#panel-1058-body>iframe")
        # )
        i_frame = driver.find_element_by_css_selector("#panel-1058>#panel-1058-body>iframe")
        driver.switch_to.frame(i_frame)
        # 先点击下查询，把loading提示div网页js加载出来
        driver.find_element_by_id("button-1570-btnEl").click()
        # 等待数据列加载完毕
        # if tool.data_is_refresh(driver) is True:
            # print u"加载完毕......"
        time.sleep(3)
        # 数据录入
        tmp_hth = sheet1.cell(0, 0).value
        tmp_name = sheet1.cell(0, 3).value
        driver.find_element_by_id("textfield-1556-inputEl").clear()
        driver.find_element_by_id("textfield-1553-inputEl").clear()
        driver.find_element_by_id("textfield-1556-inputEl").send_keys(tmp_hth)  # 账号赋值
        driver.find_element_by_id("textfield-1553-inputEl").send_keys(tmp_name)  # 借款人赋值
        driver.find_element_by_id("button-1570-btnEl").click()
        # driver.implicitly_wait(tool.time_out)
        # 加入定时器，定期查找页面是否刷新
        refresh_result = data_is_refresh(driver, "loadmask-1902")
        print refresh_result
        if refresh_result is True:
            # 数据行
            data = driver.find_elements_by_css_selector("#gridview-1848>table>tbody>tr")
            if len(data) == 2:  # 第一行是<tbody>中<th>的标题行，一直为空
                data_hth = driver.find_element_by_css_selector(
                    "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(5)>div").text
                data_name = driver.find_element_by_css_selector(
                    "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(2)>div").text
                print data_hth
                print tmp_hth
                print data_name
                print tmp_name
                print data_hth == tmp_hth
                print data_name == tmp_name
                if data_hth == tmp_hth and data_name == tmp_name:
                    driver.find_element_by_css_selector(
                        "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(1)>div").click()
                    time.sleep(1)
                    is_selected = driver.find_element_by_css_selector(
                        "#gridview-1848>table>tbody>tr:nth-child(2)").get_attribute("class")
                    print is_selected
                    if "x-grid-row-selected" in is_selected:
                        driver.find_element_by_id("updatePersonInfoBtn-btnEl").click()  # 上报贷款业务按钮

                    else:
                        print u"未能点击上报按钮"
                else:
                    print u"未能点击"
            else:
                print u"未查询出来或查询出多个结果"
        # 贷款开户信息页面
        person_db = False  # 是否自然人担保
        if data_is_refresh(driver, "p2"):  # 判断贷款业务信息页面是否出来
            if driver.find_element_by_id("combobox-1648-inputEl").get_attribute("value") == "自然人担保":
                person_db = True
            driver.find_element_by_id("button-1670-btnEl").click()
        if person_db:
            driver.find_element_by_id()



        # for i in range(0,rowCount):
         # tmp_hth = sheet1.cell(i,0).value
          # tmp_name = sheet1.cell(i,3).value
           # dirver.find_element_by_id("susername").send_keys(tmp_hth)#账号赋值
            #dirver.find_element_by_id("susername").send_keys(tmp_name)#借款人赋值
            #print(tmp_hth,tmp_name)
