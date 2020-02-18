## 基本数据结构
# 1.数字型 Number
print(2 + 2)

# 2.字符串 String
print('C:\some\\name')
print(r'C:\some\name')   # r表示原生的
print('py' 'thon')       # 进行连接

x='abc'
print('C:\some\\name\\'+x)
print(f'C:\some\\name\\{x}')     # f表示连接
print("C:\some\\name\\{y}\\{x}".format(y=x,x=123))

print(x[0])               # 字符串属于特殊的列表，可切片操作

# 3.列表 List
squares = [1, 4, 9, 16, 25]
print(squares[0])
print(squares[0:3])          # 切片

list = [x*10 for x in range(10)]  #创建列表方法
print(list)