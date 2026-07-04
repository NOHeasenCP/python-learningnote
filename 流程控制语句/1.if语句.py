##########
#if else语句
###########

n=int(input("输入一个整数："))
if n>=10 and n<=20:
    print(f"{n}在10-20之间")
else: print("不符合条件")

n=int(input("输入一个整数："))
if n<=10 or n>=20:
    print(f"{n}不在10-20之间")
else: print("不符合条件")

n=int(input("输入一个整数："))
if  not n<10 or n>20:
    print(f"{n}不在10-20之间")
else: print("不符合条件")

