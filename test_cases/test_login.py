from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from test_cases.base_case import BaseCase

class TestLogin(BaseCase):
    name = '登录功能'

    # 调用名为driver的夹具
    def test_login(self,driver):
        '''测试登录成功'''
        # 1.实例化登录界面
        lp = LoginPage(driver)
        #调用登录方法
        lp.login(self.settings.TEST_NORMAL_USERNAME,self.settings.TEST_NORMAL_PASSWORD)
        #断言
        hp = HomePage(driver)

        assert hp.get_logout_btn()