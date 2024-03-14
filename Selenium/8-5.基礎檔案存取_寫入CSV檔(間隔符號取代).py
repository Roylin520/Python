import csv
fn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\CreateCSV.csv'
with open(fn, 'w', newline = '') as csvFile:  # 增加 newline = '' 避免資料空一行
    csvWriter = csv.writer(csvFile, delimiter = '?')  # 取代 , 使用?串字間隔字元
    csvWriter.writerow(['姓名', '電話', 'ID', '費用', '是否前往'])  # 寫入資料
    csvWriter.writerow(('李小明', '(02)22345678', 'A123456789', 100, True))
    csvWriter.writerow({'王大強', '(07)33998761', 'B123456789', 900, False})