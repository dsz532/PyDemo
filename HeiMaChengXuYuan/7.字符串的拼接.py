name = "dsz"
addr = 10086
file = "dsz%s" % addr
print(file)

num1 = 11
num2 = 11.345
print("数字1宽度限制5，结果为：%5d" % num1)
print("数字1宽度限制1，结果为：%1d" % num1)
print("数字2宽度限制5，精度限制1，结果为：%5.2f" % num2)
print("数字2宽度不限制，精度限制1，结果为：%.2f" % num2)
