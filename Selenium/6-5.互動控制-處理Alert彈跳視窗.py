from time import sleep
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://www.google.com/"
driver.get(url)

sleep(3)
driver.execute_script("window.alert('這是一個測試Alert彈跳視窗')")

print(driver.switch_to.alert.text)

sleep(3)
driver.switch_to.alert.accept()  # 確認/接授

'''
彈跳視窗有3種：
alert 警告訊息
confirm 確認訊息
prompt 題示輸入

出現彈跳視窗後，Selenium提供下列方法：
accept() 接受
dismiss() 取消
text 獲取顯示本文
send_keys() 輸入內容
'''


sleep(3)
driver.close()





