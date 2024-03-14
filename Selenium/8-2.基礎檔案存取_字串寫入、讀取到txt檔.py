# file = open('C:\\Users\\Roy\\Documents\\git\\Python\\Selenium\\txt\\writedata.txt', 'a')
# 字串前面加r，免處理跳脫字元 \

'''
w:自動建立檔案，單次寫入(會覆蓋原檔)
x：需原有的檔案存在，否則會報錯
a：自動建立檔案，不會覆蓋原檔，接下寫入資料
'''
# file = open(r'C:\Users\Roy\Documents\git\Python\Selenium\txt\writedata.txt', 'a')
# file.write('寫入資料到檔案\n')
# file.write('ABCDE\n')
# file.write('1234')
# file.close()

'''
 簡易寫法，好處：最後不用file.close()
 with open(file,mode) as 檔案物件名稱
 ........　　　　　　　　＃存取檔案的動作

'''
with open(r'C:\Users\Roy\Documents\git\Python\Selenium\txt\writedata.txt', 'a') as file:
    file.write('寫入資料到檔案\n')
    file.write('ABCDE\n')
    file.write('1234')

# file = open(r'C:\Users\Roy\Documents\git\Python\Selenium\txt\writedata.txt', 'r')
# content = file.read()
# print(content)
# file.close()

with open(r'C:\Users\Roy\Documents\git\Python\Selenium\txt\writedata.txt', 'r') as file:
    content = file.read()
    print(content)

