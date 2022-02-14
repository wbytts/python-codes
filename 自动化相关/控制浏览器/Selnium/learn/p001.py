from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys("美女")

driver.find_element_by_css_selector(r"")

handles = driver.window_handles
for i in range(1000):
    driver.switch_to.window(handles[0])
    driver.find_element_by_id('su').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="1"]/div/h3/a').click()
    time.sleep(1)
    handles = driver.window_handles
    driver.switch_to.window(handles[1])
    time.sleep(1)
    driver.close()


driver.close()
driver.quit()






