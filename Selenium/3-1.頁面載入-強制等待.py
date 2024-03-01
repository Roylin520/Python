# 載入time模組的sleep()方法
from time import sleep
from selenium import webdriver

# 載入elenium.webdriver.common.by 函數來找網頁元素
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://tw.yahoo.com/")

# 強制等待3秒後，再往下執行程式碼
# 實用性不高，缺點：
# 1.設定時間太短，上一個網頁未載入完全，會找不到元素
# 2.時間設定太長，網頁元素早已找到，會空等時間，執行效率變差

# 網站完全載入後，才會往下執行，sleep()
sleep(0.1)

# By.ID來找網頁元素 ID，找到後並使用send_keys方法來輸入文字
driver.find_element(By.ID,'header-search-input').send_keys("python")
# 退出
sleep(3)
driver.quit()