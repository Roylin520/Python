
from time import sleep
from selenium import webdriver


driver = webdriver.Edge()
driver.maximize_window()

url = "https://tw.yahoo.com/"
driver.get(url)

# 將滾動條拖到最底部
sleep(3)
js = "var action=document.documentElement.scrollTop = 10000"
driver.execute_script(js)

sleep(3)
js = "var action=document.documentElement.scrollTop = 20000"
driver.execute_script(js)

# 將滾動條拖到最頂部
sleep(3)
js = "var action=document.documentElement.scrollTop = 0"
driver.execute_script(js)

sleep(3)
driver.quit()
print("移動成功")