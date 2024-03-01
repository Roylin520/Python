from selenium import webdriver
from selenium.webdriver.common.by import By

# 載入selenium.elenium.common.exceptions
from selenium.common.exceptions import NoSuchElementException
# Selenium常用的例外物件之一，NoSuchElementException = 選取的元件不存在
import os

driver = webdriver.Chrome()
html_path = os.path.abspath("SeleniumTest.html")
driver.implicitly_wait(5)
driver.get(html_path)

try:
    content = driver.find_element(By.CSS_SELECTOR, "h31")
    print(content.text)
except NoSuchElementException:
    print("選取元素不存在")

driver.quit()

'''
Selenium例外物件
名稱	 說明
ElementNotSelectableException	選取的該元素不允許被選取
ElementNotVisibleException	元素存在，但是不可見
ErrorInResponseException	伺服器端回應錯誤
NoSuchElementException	選取的元素不存在
TimeoutException	超過時間限制
'''