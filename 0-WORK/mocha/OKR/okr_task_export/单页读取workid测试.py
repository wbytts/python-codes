from selenium import webdriver
import time
import openpyxl

workid_list = []
download_url = "http://xxhapp.js.cmcc:30002/tokr-web/fileresource/download?resourceId="

browser = webdriver.Chrome()
browser.get("http://xxhapp.js.cmcc:30002/tokr-web/getuser?userid=822cdeeac1f3dd5294dc0c289a4ea0df")

# 浏览器最大化
browser.maximize_window()
time.sleep(2)
# 填入用户名和密码
browser.find_element_by_name("userName").send_keys("okradmin")
time.sleep(1)
browser.find_element_by_name("password").send_keys("OKR@2018_admin")
time.sleep(1)
# 点击登录按钮
browser.find_element_by_name("submit").click()
time.sleep(6)
# 点击清空筛选
browser.find_element_by_id("cleanCurFilter").click()
time.sleep(6)

page_num = 61

browser.find_element_by_id("search_input").send_keys(str(page_num))
time.sleep(1)
browser.find_element_by_id("search_button").click()
time.sleep(3)
# 查找当前页面的任务的 workid
task_openbutton_list = browser.find_elements_by_link_text("打开")
# 将workid加入到统计列表中
for link in task_openbutton_list:
    workid_list.append(link.get_attribute("workid"))


print(workid_list)




