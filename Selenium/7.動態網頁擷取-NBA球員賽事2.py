from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd


driver = webdriver.Chrome()
# url = "http://stats.nba.com/players/traditional/?sort=PTS&dir=-1"
url = "https://www.nba.com/stats/players/traditional"
driver.get(url)

# 點擊「I Accept」Cookie Policy
driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()

sleep(2)
pages_remaining = True

# 擷取總頁數
page_num = int(driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[4]').text.split()[-1])  # split將 of 12 拆分兩個字串
page_current = 1

while pages_remaining:
    soup = BeautifulSoup(driver.page_source, "lxml")
    table = soup.select_one('#__next > div.Layout_base__6IeUC.Layout_justNav__2H4H0.Layout_withSubNav__ByKRF > div.Layout_mainContent__jXliI > div.MaxWidthContainer_mwc__ID5AG > section.Block_block__62M07.nba-stats-content-block > div > div.Crom_base__f0niE > div.Crom_container__C45Ti.crom-container > table')  
    # 使用 StringIO 將 HTML 字串包裝成文件對象
    table_file = StringIO(str(table))
    # 使用 pd.read_html 讀取 HTML 表格數據
    data = pd.read_html(table_file)
    data[0].to_csv("All_players_stats" + str(page_current) + ".csv", index=0)  # index=0 →資料表表頭
    print("儲存頁面", page_current)
    try:
        # 自動按下一頁
        next_link = driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[3]/section[2]/div/div[2]/div[2]/div[1]/div[5]/button[2]').click()
        # next_link.click()
        sleep(2)
        if page_current < page_num:
            page_current += 1
        else:
            pages_remaining = False
    except:
        pages_remaining = False
print("已完成，")
driver.quit()

