# 匯入相關套件
from time import sleep
from selenium import webdriver

# 建立瀏覽器物件
driver = webdriver.Edge()

# 開啟特定網站
driver.get("https://tw.yahoo.com/")

sleep(3)
url = "https://www.google.com/"
driver.get(url)

#3秒後，關閉瀏覽器 
sleep(3)
driver.quit() 
# quit() 為呼叫dispose()函數關閉所有開啟的瀏覽器，安全結束交談期間
# close() 為閉關目前的瀏覽器S