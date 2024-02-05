from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class HomePage:
    '''首页'''
    name = '首页'
    #定位信息放到类属性中
    logout_but_loc=('xpath','//a[@title="退出"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def get_logout_btn(self):
        '''获取退出按钮'''
        #返回退出按钮的元素，若无返回则报错
        try:
            return WebDriverWait(self.driver,timeout=5).until(
                EC.visibility_of_element_located(self.logout_but_loc)
            )
        except Exception as e:
            return None


    def logout(self):
        WebDriverWait(self.driver,timeout=5).until(
            EC.visibility_of_element_located(self.logout_but_loc)
        ).click()
