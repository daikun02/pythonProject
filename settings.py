import os

# 项目根目录
BASE_DIR=os.path.dirname(os.path.abspath(__file__))

# 测试用例路径
TEST_CASE_DIR=os.path.join(BASE_DIR,'test_cases')

# 项目域名
PROJECT_HOST='https://portal-sit.leapmotor.com/'

# url信息
INTERFACE={
    'login':'#/login'
}

# 日志配置
LOG_CONFIG={
    'name':'test123',
    'filename':os.path.join(BASE_DIR,'logs/test123.log'),
    'mode':'a',
    'encoding':'utf-8',
    'debug':True
}

# 测试账户信息
TEST_NORMAL_USERNAME = '19999999999'
TEST_NORMAL_PASSWORD = '123456'