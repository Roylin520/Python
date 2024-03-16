# pip install pdfplumber 安裝pdf套件
import pdfplumber
file_path = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\example.pdf'
pdf = pdfplumber.open(file_path)  # 開啟pdf檔
print(pdf.pages)

# %%
# 讀取文字
page = pdf.pages[0]  # 讀取第一頁
text = page.extract_text()  # 取出文字
print(text)

# %%
# 讀取表格
pagetable = pdf.pages[1]
table = pagetable.extract_table()  # 取出表格
print(table)
pdf.close()