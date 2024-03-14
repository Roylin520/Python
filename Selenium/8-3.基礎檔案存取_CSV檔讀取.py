import csv
fn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\csvReport.csv'
with open(fn, encoding='utf8') as csvFile:  # 開啟csv檔案
    csvReport = csv.reader(csvFile)  # 讀取檔案物件建立Reader物件
    listReport = list(csvReport)  # 將資料轉成串列
# print(listReport)  # 列印所有資料

# 使用索引讀取串列資料表
print(listReport[3])  # 讀取索引第三筆資料
print(listReport[3][2])  # 讀取索引第三筆資料的第二個欄位值

# 讀取索引第四筆第二欄位值、第五筆第六欄位值
print(listReport[4][2], listReport[5][6])




