# pip install pdfplumber 安裝pdf套件
import pdfplumber
file_path = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\example2.pdf'
pdf = pdfplumber.open(file_path, password='test')  # 開啟pdf檔,輸入密碼
print(pdf.pages)

# %%
# 讀取文字
page = pdf.pages[0]  # 讀取第一頁
text = page.extract_text()  # 取出文字
print(text)
pdf.close()