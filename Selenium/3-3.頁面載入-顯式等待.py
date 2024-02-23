from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 新增載入
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#新增事入按鍵模組
from selenium.webdriver.common.keys import Keys


driver = webdriver.Edge()
driver.get("https://tw.yahoo.com/")
"""
Explicit Waits(明確等待)：
語法說明如下：
until()：符合指定的等待條件
  WebDriverWait(driver, 等待的最長時間, 檢查條件的頻率, 忽略的例外類別).until(expected_conditions條件, 超時例外的錯誤訊息)
until_not()：不符合指定的等待條件。
 WebDriverWait(driver, 等待的最長時間, 檢查條件的頻率, 忽略的例外類別).until_not(expected_conditions條件, 超時例外的錯誤訊息)
"""

# 明確等待
# WebDriverWait(driver, 等待的最長時間, 檢查條件的頻率, 忽略的例外類別).until(expected_conditions條件, 超時例外的錯誤訊息)
locator = (By.ID, "header-search-input")  # 定位器
search_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(locator),
    "找不到指定的元素"
)
 
search_input.send_keys("藍芽耳機")  # 輸入文字
search_input.send_keys(Keys.ENTER)

sleep(5)
driver.quit()