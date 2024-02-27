from time import sleep
from selenium import webdriver

driver = webdriver.Edge()

url = "https://tw.yahoo.com/"
driver.get(url)

# 自行設定視窗座標
driver.set_window_position(0, 300)
print(f"視窗的X座標為：{driver.get_window_position().get('x')}")
print(f"視窗的X座標為：{driver.get_window_position().get('y')}")
sleep(3)

# 自行設定視窗的寬與高
driver.set_window_size(500, 300)
print(f"視窗的寬為：{driver.get_window_size().get('width')}")
print(f"視窗的高為：{driver.get_window_size().get('height')}")
sleep(3)

# 改變視窗大小為「最小化」
driver.minimize_window()
print(f"視窗最小化時，視窗的寬度：{driver.get_window_size().get('width')}")
print(f"視窗最小化時，視窗的高為：{driver.get_window_size().get('height')}")
sleep(3)

## 改變視窗大小為「最大化」 
driver.maximize_window()
print(f"視窗最大化時，視窗的寬度：{driver.get_window_size().get('width')}")
print(f"視窗最大化時，視窗的高為：{driver.get_window_size().get('height')}")
sleep(3)

## 改變視窗大小為「全屏」 
driver.fullscreen_window()
print(f"視窗為全屏時，視窗的寬度：{driver.get_window_size().get('width')}")
print(f"視窗為全屏時，視窗的高為：{driver.get_window_size().get('height')}")

sleep(3)
driver.quit()