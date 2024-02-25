import time
from selenium import webdriver

driver = webdriver.Edge()

# get()，前往指定網址，並印出網站名稱及網址
url = "https://tw.yahoo.com/"
driver.get(url)
print(f"網站名稱：{driver.title},網址：{driver.current_url}\n")

time.sleep(3)
# 前往另一個網址，並印出網站名稱及網址
url = "https://www.google.com/"
driver.get(url)
print(f"網站名稱：{driver.title},網址：{driver.current_url}\n")

time.sleep(3)
# 回上一頁，使用back()方法，並印出網站名稱及網址
driver.back()
print(f"使用back()方法，回到上一頁，網站名稱：{driver.title},網址：{driver.current_url}\n")

time.sleep(3)