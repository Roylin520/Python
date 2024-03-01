from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
html_path = os.path.abspath("SeleniumTest.html")
driver.implicitly_wait(5)
driver.get(html_path)
content = driver.find_element(By.CSS_SELECTOR, "h3")
print(content.text)
p = driver.find_element(By.CSS_SELECTOR, "p")
print(p.text)
driver.quit()

# Selenium共有8種定位元素選擇器，可以參考：6-2.互動控制-針對指定元素呼叫.py