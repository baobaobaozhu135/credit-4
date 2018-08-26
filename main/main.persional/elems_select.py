# _*_encoding:utf-8_*_

# 说明：互联网征信系统页面各元素集合
# 互联网征信系统中很多元素是由js动态添加
# 每次关闭再打开个人贷款管理页面时，frame页面有些div是动态添加的，id中有编号，是不固定的
# 所以很多元素打开以第一次打开为准，tab关闭再打开时，id选择器可能不准，后期维护时，选择元素尽量通用


class Elems(object):
    def __init__(self):
        # 登录界面
        self.login_name_id = "susername"  # 登录用户名
        self.login_pass_id = "spassword"  # 登录密码
        # 主页面
        self.person_manage_select_id = "button-1040-btnEl"  # 个人贷款上报按钮select
        self.person_manage_select_option_id = "menuitem-1037-textEl"  # 个人贷款上报按钮option
        # 个人贷款管理主页面
        self.name_input_id = "textfield-1553-inputEl"  # 姓名输入
        self.hth_input_id = "textfield-1556-inputEl"  # 账号输入
        self.query_btn_id = "button-1570-btnEl"  # 查询按钮
        # 切换到 iframe
        self.iframe_css = "#panel-1058>#panel-1058-body>iframe"
        self.loading_css = "#loadmask-1902"  # loading幕布，点击查询后才有 display属性是在style里
        # 数据行
        self.data_tr_css = "#gridview-1848>table>tbody>tr"  # 数据行
        self.data_tr_hth_css = "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(5)>div"  # 数据行中业务号
        self.data_tr_name_css = "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(2)>div"  # 数据行中名字
        self.data_checkbox_css = "#gridview-1848>table>tbody>tr:nth-child(2)>td:nth-child(1)>div"  # checkbox div
        self.check_is_select_by_class_css = "#gridview-1848>table>tbody>tr:nth-child(2)"  # checkbox上上层tr,判断是否选中
        # 按钮
        self.begin_fill_btn_id = "updatePersonInfoBtn-btnEl"  # 上报贷款业务按钮

        # 贷款业务信息页面中的tab 共七个
        # 贷款开户信息，担保信息，借款人基本信息，账户信息，还款信息，还款流水信息，特殊交易信息
        self.tab_1_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(1)>em>button>span:nth-child(1)"
        self.tab_2_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(2)>em>button>span:nth-child(1)"
        self.tab_3_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(3)>em>button>span:nth-child(1)"
        self.tab_4_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(4)>em>button>span:nth-child(1)"
        self.tab_5_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(5)>em>button>span:nth-child(1)"
        self.tab_6_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(6)>em>button>span:nth-child(1)"
        self.tab_7_css = "#p2-body>div>div:nth-child(2)>div:nth-child(1)>div:nth-child(2)>div>" \
                         "div:nth-child(7)>em>button>span:nth-child(1)"

        # 贷款业务信息页面中的page 共七个
        self.page_parent = "#p2-body>div>div:nth-child(3)>div"  # 用来判断几个div加载
        self.page_1 = "#p2-body>div>div:nth-child(3)>div:nth-child(1)"
        self.page_2 = "#p2-body>div>div:nth-child(3)>div:nth-child(2)"
        self.page_3 = "#p2-body>div>div:nth-child(3)>div:nth-child(3)"
        self.page_4 = "#p2-body>div>div:nth-child(3)>div:nth-child(4)"
        self.page_5 = "#p2-body>div>div:nth-child(3)>div:nth-child(5)"
        self.page_6 = "#p2-body>div>div:nth-child(3)>div:nth-child(6)"
        self.page_7 = "#p2-body>div>div:nth-child(3)>div:nth-child(7)"

        # 基于page1234567下查找各自页面下一步
        self.next_btn_css = "div>div>div:nth-child(2)>div>div>div:nth-child(2)>em>button"    # 其他下一步
        self.next_btn_jkrxx_css = "div>div>div:nth-child(2)>div>div>div:nth-child(3)>em>button"  # 借款人信息下一步  多了一个重置
        # 开户信息页面
        # self.ffr = "#p2-body>div>div:nth-child(3)>div>div>div>div:nth-child(1)>table>tbody:nth-child(3)" \
        #            ">tr>td>div>div>div:nth-child(1)>div:nth-child(1)>div>table>tbody>tr>td:nth-child(2)>div"
        self.ffr_id = "displayfield-1632-inputEl"  # 直接text
        self.dqr_id = "datefield-1633-inputEl"  # getAtrribute得到style,再切片

        self.khr_scc = "#accountModifyForm-formTable>tbody:nth-child(1)>tr>td>div>div>div:nth-child(1)>" \
                       "div:nth-child(1)>div>table>tbody>tr>td:nth-child(2)>table>" \
                       "tbody>tr>td:nth-child(1)>input"    # 结算应还款日
        self.ye_css = "#accountModifyForm-formTable>tbody:nth-child(1)>tr>td>div>div>div:nth-child(1)>" \
                      "div:nth-child(2)>div>table>tbody>tr>td>div>div>table>tbody:nth-child(1)" \
                      ">tr>td>div>div>div:nth-child(1)>div>div>table>tbody>tr>td:nth-child(2)>input"  # 余额

        self.wjfl = "#accountModifyForm-formTable>tbody:nth-child(2)>tr>td>div>div>div:nth-child(1)>div:nth-child(1)>div>table>tbody>tr>td:nth-child(2)>table>tbody>tr>td:nth-child(1)>input"  # 五级分类

        self.zhzt = "#accountModifyForm-formTable>tbody:nth-child(2)>tr>td>div>div>div:nth-child(1)>div:nth-child(2)>div>table>tbody>tr>td:nth-child(2)>table>tbody>tr>td:nth-child(1)>input"  # 账户状态

        self.flag_divs_css = "html>body>div"
        self.wjfl_option_div_css = "html>body>div:nth-child(12)"
        self.zhzt_option_div_css = "html>body>div:nth-child(13)"
        self.byjs_btn_css = "div:nth-child(2)>div>div>div>div:nth-child(2)>div>div>div:nth-child(3)>em>button"  # 本月结算   相对于flag_option_div_css

        self.return_btn_css = "#p2>div:nth-child(1)>div>div>div>em>button"

