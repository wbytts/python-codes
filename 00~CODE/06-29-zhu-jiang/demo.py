from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = 'D:\\web_drivers\\chromedriver.exe')

# https://doctor.fangcunyisheng.com/#/login   登录网址
driver.get(r'http://doctor.fangcunyisheng.com/#/login')
driver.implicitly_wait(8)

# 用户名：lifei
# 密码：lf321%

driver.find_element_by_css_selector(r'[name="username"]').send_keys('lifei')
driver.find_element_by_css_selector(r'[name="password"]').send_keys('lf321%')
driver.find_element_by_css_selector(r'.btn.btn-success').click()

time.sleep(3)
driver.close()
driver.quit()






