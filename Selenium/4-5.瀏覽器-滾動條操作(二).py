from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.google.com/"
driver.get(url)

sleep(1)
# 使用三個單引號時機，
driver.find_element(By.CSS_SELECTOR, "#APjFqb").send_keys("selenium")
driver.find_element(By.CLASS_NAME, "gNO89b").click()

# 將滾動條拖到最底部
sleep(3)
js = "var action=document.documentElement.scrollTop = 10000"
driver.execute_script(js)


# 將滾動條拖到最頂部
sleep(3)
js = "var action=document.documentElement.scrollTop = 0"
driver.execute_script(js)

# 將滾動條拖到任意位置
sleep(3)
js = "var action=document.documentElement.scrollTop = 50"
driver.execute_script(js)

sleep(3)
driver.close()