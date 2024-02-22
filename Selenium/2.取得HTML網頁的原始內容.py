from time import sleep
from selenium import webdriver

# 建立瀏覽器物件
driver = webdriver.Edge()

# 開啟特定網站
driver.get("https://example.com")

sleep(3)
print(driver.title)  # 輸出網站title資訊

sleep(3)
print(driver.page_source)  # 輸出網站原始碼

sleep(3)
driver.close() 
