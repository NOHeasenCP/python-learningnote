#input 获取用户输入
name = input("请输入你的名字：")
print(f"{name},hello!")#字符串拼接，所以用规范化的f“{}”

money = 10000
takeout = input("请输入你要取出的金额：")
print(f"你取出了{takeout}元，你的余额为{money-int(takeout)}元。")#input输入

number_1 = input("请输入第一个数字：")
number_2 = input("请输入第二个数字：")
print(f"两个数字之和为:{int(number_1)+int(number_2)}")#input输入
