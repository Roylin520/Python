from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://tw.yahoo.com/")
"""
implicitly_wait()隱式等待：
隱式等待是一個全局設置，設置後所有的元素定位都會等待給定的時間，直到元素出現為止，等待規定時間元素沒出現就報錯。


"""

driver.implicitly_wait(20) 
driver.find_element(By.ID,'header-search-input').send_keys("python")  

# sleep(3) 「強制等待」不可以與「隱式等待」同時使用
driver.quit()