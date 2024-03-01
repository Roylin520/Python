from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
url = "https://www.google.com/"
driver.get(url)


# 定位搜尋框
search = driver.find_element(By.NAME, "q")
action = webdriver.ActionChains(driver)

action.key_down(Keys.SHIFT).send_keys_to_element(search, "aaa ")
sleep(2)
action.key_up(Keys.SHIFT).send_keys("aaA")
action.perform()
sleep(5)


# 清除search box 元素中所有文字
search.clear()

# 輸入中文字串"自動化測試"，並按下ENTER。
# send_keys要輸入中文時，雙引號前要加上「u」
search.send_keys(u"自動化測試" + Keys.ENTER)

sleep(3)
driver.close()





