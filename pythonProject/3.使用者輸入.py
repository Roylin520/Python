# input 取得使用者輸入
import datetime

# name = input('請輸入名字：')
# print(f"您的名字是：{name}")

# 練習一：填字練習
# name = input('請輸入姓名：')
# holiday = input('請輸入今天是「上班」還是「放假」：')
# Feeling = input('請輸入心情：')
# place = input('請輸入地點：')
# action = input('請輸入要做什麼事：')
# day = datetime.date.today()
# print(f"今天是{day}，是{name}的{holiday}日，要去{place}{Feeling}的{action}。")

# 練習二：計算矩形面積
# length = float(input("請輸入矩形的長度(cm)："))
# width = float(input("請輸入矩形的寬度(cm)："))
# area = length * width
# print(f"面積為：{area}平方公分。")

# 練習三：購物車程式
item = input("你想購買什麼商品?")
price = float(input("商品價格是多少?"))
quantity = int(input("需要幾個?"))
total = price * quantity
print(f"您購買了{item}，數量：{quantity}個，總價：{total}元。")