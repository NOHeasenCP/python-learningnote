##########
#变量
##########
num = 114.1
print(num)

num = num + 1
print(num)

num = "nohcp"
print(num)

##########
#python中变量可以不断进行赋值
###########

base=20.7
incr=1.5

print("赋值前的base值:", base)
print("print中赋值展示:", incr+base)#不改变原值
print(incr,base)#生成的结果为无限小数，原因是计算机中浮点数的存储方式导致的精度问题
num_result=incr*base
print(num_result)
print(round(num_result,2))#round()函数用于四舍五入，第二个参数为保留小数位数
print(f"{num_result:.2f}")#格式化输出，.2f表示保留两位小数
from decimal import Decimal#dicimal模块可以解决浮点数精度问题,为十进制储存
a,b= Decimal("1.5"),Decimal("20.7")#同时为两个变量赋值
print(a * b)
c,d=3.5,"saved"#可以同时为不同类型的变量赋值
print(c,d)