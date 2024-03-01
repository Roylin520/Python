from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get('https://bit.ly/3Ig1Asb')
# 試範8種的選擇器
a = driver.find_element(By.ID, 'a')   # ID 選擇器
b = driver.find_element(By.CLASS_NAME, 'btn')  # CLASS_NAME 選擇器
c = driver.find_element(By.CSS_SELECTOR, '.test')  # CSS_SELECTOR 選擇器
d = driver.find_element(By.NAME, 'dog')  # NAME 選擇器
h1 = driver.find_element(By.TAG_NAME, 'h1')  # TAG_NAME 選擇器
select = Select(driver.find_element(By.XPATH, '//*[@id="select"]'))  # XPATH 選擇器
link1 = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')  # LINK_TEXT 選擇器
link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google')  # PARTIAL_LINK_TEXT 選擇器

# 測試點擊增加數字btn
add = driver.find_element(By.ID, "add")

a.click()
print(a.text)
sleep(2)

b.click()
print(b.text)
sleep(2)

c.click()
print(c.text)
sleep(2)

d.click()
print(d.text)
sleep(2)

add.click()
sleep(1)

add.click()
sleep(1)

add.click()
sleep(1)

add.click()
sleep(1)

h1.click()
print(h1.text)
sleep(2)

select.select_by_index(2)  # 下拉式選單第三個(第一個為 0 )
sleep(2)


link1.click()
print(link1.text)
sleep(2)

link2.click()
print(link2.text)


sleep(2)
driver.close()
driver.quit()




