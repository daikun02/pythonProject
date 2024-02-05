#共享夹具
import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def driver():
    with webdriver.Chrome() as wd:
        # 最大化游览器
        wd.maximize_window()
        # 返回游览器对象，不能使用return，return返回之后会关闭游览器，无法进行后续操作
        yield wd