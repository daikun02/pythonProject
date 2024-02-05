from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings

class LoginPage:
    '''把一个页面抽象成一个类，所有这个页面的功能封装成方法'''
    #页面名称
    name='登录页面'

    #定位信息放到类属性中
    #用户输入框定位
    username_input_locator = ('xpath','//input[@placeholder="请输入账号"]')
    #密码输入框定位
    password_input_locator = ('xpath','//input[@placeholder="请输入密码"]')
    #登录按钮定位
    login_btn_locator =  ('xpath','//button[@class="el-button login el-button--primary"]')

    def __init__(self,driver:WebDriver):
        self.driver = driver

    def login(self,username,password):
        '''登录页面的登录功能'''
        #1.访问登录页面

        self.driver.get(settings.PROJECT_HOST+settings.INTERFACE['login'])
        #2.输入用户名密码
        wait=WebDriverWait(self.driver,timeout=5)
        #2.1定位用户名输入框
        username_input = wait.until(EC.visibility_of_element_located(self.username_input_locator))
        #2.2输入用户名
        username_input.send_keys(username)
        #2.3定位密码输入框
        password_input=wait.until(EC.visibility_of_element_located(self.password_input_locator))
        #2.4输入密码
        password_input.send_keys(password)
        sleep(3)
        #3.点击登录
        wait.until(EC.visibility_of_element_located(self.login_btn_locator)).click()
