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
element.send_keys("Pythonab")

# 刪除多輸入的2個字
sleep(2)
element.send_keys(Keys.BACK_SPACE)

sleep(2)
element.send_keys(Keys.BACK_SPACE)

# 按下Enter執行
sleep(3)
element.send_keys(Keys.ENTER)

sleep(3)
driver.quit()





