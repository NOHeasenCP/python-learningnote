#双引号定义
s1 = "hello world"

#单引号定义
s2 = 'hello world'

#三引号定义(多行字符串)
s3 = """
    hello
        world!
"""

print(s1, s2, s3)
print(type(s1), type(s2), type(s3))

##########
#字符是字符串的最小单位，字符串是由字符组成的
##########

#########
#通过转义字符来表示特殊字符
#########
s4 = "hello\nworld\n"  # \n 表示换行
s5 = "hello\tworld\n"  # \t 表示制表符
s6 = "It\'s a beautiful day!\n"   # \' 表示单引号
s7 = "He said\"Hello, World!\"\n"  # \" 表示双引号
print(s4, s5, s6, s7)


########
#字符串拼接
########
s8 = "hello" + " " + "world"
print(s8)

slogan_1 = "hello"
slogan_2 = "world"
print(" He says: "+slogan_1+" "+slogan_2+"!")

########
#加号只能将字符串连接起来，不能将字符串与其他类型的数据连接起来
########

name = "easen"
age = str(18)#用str()函数将整数类型转换为字符串类型+
print("My name is " + name + " and I am " + age + " years old.")

########
#通过占位符来实现字符串的拼接
########
name = "alan"
age = 20
print("My name is %s and I am %s years old." % (name, age))#前面有几个占位符，后面就要有几个变量，且顺序要对应

##########
#用f"内容{变量/表达式}"的方式来实现字符串的拼接
##########
name = "L"
age = "21"
print(f"My name is {name} and I am {age} years old.")
print(f"{name}?,{age}?")