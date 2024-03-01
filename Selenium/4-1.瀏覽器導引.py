from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()

# get()，前往指定網址，並印出網站名稱及網址
url = "https://tw.yahoo.com/"
driver.get(url)
print(f"網站名稱：{driver.title},網址：{driver.current_url}\n")

sleep(3)
# 前往另一個網址，並印出網站名稱及網址
url = "https://www.google.com/"
driver.get(url)
print(f"網站名稱：{driver.title},網址：{driver.current_url}\n")

sleep(3)
# 回上一頁，使用back()方法，並印出網站名稱及網址
driver.back()
print(f"使用back()方法，回到上一頁，網站名稱：{driver.title},網址：{driver.current_url}\n")

sleep(3)
# 回下一頁，使用forward()方法，並印出網站名稱及網址
driver.forward()
print(f"使用forward()方法，回到下一頁，網站名稱：{driver.title},網址：{driver.current_url}\n")

sleep(3)
# 重新整理，使用refresh()方法，並印出網站名稱及網址
driver.refresh()
print(f"使用refresh()方法，重新整理頁面，網站名稱：{driver.title},網址：{driver.current_url}\n")


sleep(3)
driver.quit()