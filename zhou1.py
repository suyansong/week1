# 要对手机号的号段进行判断，
# 号段任意给出6个作为模拟号段即可.
# 判断手机号码是否是由数字组成的(总分15分，
# 5分能够判断是否为数字，5分判断是否为有效号段，5分实现)
a=input("请输入一个手机号")
if type(a[1])!=str:
    print("请输入数字")
elif len(a)<11:
    print("手机号码过于简短")
else:
    print("您的手机号码输入正确！")
