# 載入time模組的sleep()方法
from time import sleep
from selenium import webdriver

# 載入elenium.webdriver.common.by 函數來找網頁元素
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://tw.yahoo.com/")

# 強制等待3秒
sleep(3)
# By.ID來找網頁元素 ID，找到後並使用send_keys方法來輸入文字
driver.find_element(By.ID,'header-search-input').send_keys("python")  
# 退出
sleep(3)
driver.quit()