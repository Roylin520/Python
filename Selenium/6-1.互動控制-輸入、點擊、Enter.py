from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 載入按鍵模組 selenium.webdriver.common.keys
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)

# 定位搜尋框
element = driver.find_element(By.CLASS_NAME, "gLFyf")

# 輸入字串
sleep(3)
element.send_keys("Python")

# 清除搜尋框的字串
sleep(3)
element.clear()

# 輸入新的字串
sleep(3)
element.send_keys("selenium")

# 按下鍵盤"Enter"鍵
sleep(1)
element.send_keys(Keys.ENTER)

sleep(5)
driver.quit()