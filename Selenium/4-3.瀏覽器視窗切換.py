# 主要分成：所有視窗、當前視窗、視窗切換、退出瀏覽器
# 在瀏覽器要操作分頁動作時，需執行「視窗切換」指令
# 每個瀏覽器視窗都有獨立的ID，若沒有執行「視窗切換」的指令，將會判定為原來的分頁
from time import sleep
from selenium import webdriver
# from selenium.webdriver.common.by import By


driver = webdriver.Edge()

url = "https://tw.yahoo.com/"
driver.get(url)

# 當前視窗：獲取當前視窗的ID，driver.current_window_handle
print(f"當前視窗第一個Yahoo，ID：{driver.current_window_handle}")
sleep(3)

# 確認目前視窗分頁為一個
assert len(driver.window_handles) == 1

# 新開分頁視窗，獲取當前第二個分頁視窗的ID，
url = "https://www.google.com/"
driver.execute_script("window.open('');")  # 另開新視窗
# driver.execute_script(f'windows.open("{url}")", "_blank"')  # 另開新視窗
driver.switch_to.window(driver.window_handles[1])
driver.get(url)
print(f"新開分頁視窗(第二個)Google，ID：{driver.current_window_handle}")
sleep(3)

# 確認目前視窗分頁為兩個
assert len(driver.window_handles) == 2

# 獲取所有分頁的ID
print(f"獲取所有分頁的ID：{driver.window_handles}")
sleep(3)

# 切換回第一個視窗yahoo
driver.switch_to.window(driver.window_handles[0])
print(f"切換回第一個分頁視窗Yahoo，ID：{driver.current_window_handle}")
sleep(3)

# 切換回第二個視窗Google
driver.switch_to.window(driver.window_handles[1])
print(f"切換回第二個分頁視窗Yahoo，ID：{driver.current_window_handle}")
sleep(3)

# 關閉所有視窗
print("關閉所有視窗")
driver.quit()