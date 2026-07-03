#########
#数据类型
#########
#int,float,bool,str,NoneType
a=10 #int:整数类型
b=3.14 #float:浮点数类型
c=True #bool:布尔类型
d="Hello, World!" #str:字符串类型
e=None #NoneType:空类型

#########
#type()函数 用于查看变量的数据类型
#########
print(a,b,c,d,e)
print(type(a),type(b),type(c),type(d),type(e))#变量本身是没有数据类型的，输出的是变量所引用的对象的数据类型
#type(a,b,c,d,e)type() 这个函数只能接收 1 个参数（或 3 个参数的特殊用法）

##########
#isinstance(a,int)函数 用于判断变量是否是指定的数据类型
##########
print(isinstance(a,int),isinstance(b,float),isinstance(c,bool),isinstance(d,str),isinstance(e,type(None)))#type(None)表示NoneType类型


