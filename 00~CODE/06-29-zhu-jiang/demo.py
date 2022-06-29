from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')



driver.close()
driver.quit()






