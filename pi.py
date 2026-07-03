from mpmath import mp

# 输入想查看的小数位数
n = int(input("请输入要查看圆周率的第几位小数："))

# 设置计算精度（多算几位，避免误差）
mp.dps = n + 10

pi_str = str(mp.pi)

# pi_str 形如 "3.1415926..."

if n <= 0:
    print("请输入大于 0 的整数！")
else:
    print(f"π 的第 {n} 位小数是：{pi_str[n + 1]}")