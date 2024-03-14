'''
JSON使用{}為物件
{
 "name":"Jack",
 "phonenumber":"0912345678"
 "Bool":True  # 要改成小寫true
}

JSON使用[]為陣列
[
 {"1","boy"},
 {"2","0922111555"},
 {"3",False}
]

'''
import json
fn = r'C:\Users\Roy\Documents\git\Python\Selenium\samples\NewBike.json'
with open(fn, encoding='utf-8-sig') as fn:  # utf-8-sig 檔案格式為 使用BOM UTF-8
    data = json.load(fn)
print(data)


