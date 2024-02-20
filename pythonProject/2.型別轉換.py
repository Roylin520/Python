#  型別轉換 type casting

# 顯式型別轉換

# 字串轉整數
name = "123"
print(f"轉換前，變數：{name}，型別：", type(name))
name = int(name)
print(f"轉換後，變數：{name}，型別：", type(name))

# 整數轉浮點數
age = 21
print(f"轉換前，變數：{age}，型別：", type(age))
age = float(age)
print(f"轉換後，變數：{age}，型別：", type(age))

# 浮點數轉整數
gpa = 1.9
print(f"轉換前，變數：{gpa}，型別：", type(gpa))
gpa = int(gpa)
print(f"轉換後，變數：{gpa}，型別：", type(gpa))

# bool轉字串
student = True
print(f"轉換前，變數：{student}，型別：", type(student))
student = str(student)
print(f"轉換後，變數：{student}，型別：", type(student))

# 隱式型別轉換
x = 10
y = 2.0
z = x / y
print(f'x=整數、y=浮點數、z=x/y=浮點數：{z}', type(z))
