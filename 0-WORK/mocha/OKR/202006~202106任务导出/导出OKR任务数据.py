from selenium import webdriver
import time
import openpyxl
import pickle

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
# 设置办结时间筛选条件为最近一年
browser.find_element_by_css_selector("#dtimeScope").click()
time.sleep(5)
browser.find_element_by_css_selector('#dtimeScope dd ul li:nth-child(6)').click()
time.sleep(5)

with open("work_id.pickle", "rb") as f:
    workid_list = pickle.load(f)

for page_num in [91, 115]:#range(1, 129 + 1):  # 456
    try:
        # 查找当前页面的任务的 workid
        task_openbutton_list = browser.find_elements_by_link_text("打开")
        # 将workid加入到统计列表中
        for link in task_openbutton_list:
            workid_list.append(link.get_attribute("workid"))
            print(link.get_attribute("workid"), end=", ")
        # print(f"第{page_num}页workid读取成功")
    except:
        print(f"第{page_num}页workid读取失败！！！！！！！！！！！！！！！！！！！！！！！！")

    if page_num != 1 and page_num <= 465:
        browser.find_element_by_id("search_input").send_keys(str(page_num))
        time.sleep(1)
        browser.find_element_by_id("search_button").click()
        time.sleep(3)
    page_num += 1

# 关闭当前列表页面x
# browser.close()

print("workid获取完毕，持久化workid")
with open("work_id.pickle", "wb") as f:
    pickle.dump(workid_list, f)

print("导出完成！")
browser.execute_script("alert('导出完成！！！')")
time.sleep(30000)
browser.close()
