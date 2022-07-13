from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys("vue")




driver.close()
driver.quit()









