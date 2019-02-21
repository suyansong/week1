# a=input("请输入第一个人的生日:")
# b=input("请输入第二个人的生日:")
# if a<b:
#     print("1楼大")
# else:
#     print("二楼大")
#
# a=2
# b=1
# sum=0
# for i in range(1,21):
#     sum+=a/b
#     t=a
#     a=a+b
#     b=t
# print(sum)

# sum=0
# fact=1
# num=int(input("请输入一个数字:"))
# for i in range(1,num+1):
#     fact=fact*i
#     sum+=fact
# print('阶乘之和:',sum)
#
# sum=0
# a=1
# num=int(input('请输入一个数:'))
# for i in range(1,num+1):
#     a=a*i
#     sum+=a
# print(sum)

try:
    import random
    b=random.randint(1,101)
    a=int(input("请输入一个数:"))
    while 1:
       if a==b:
          print("恭喜你猜对了！")
          break
       elif a<b:
          print("你这次猜的小了！")
          a = int(input("请再次输入一个数:"))
       elif a>b:
          print("你这次猜的大了！")
          a = int(input("请再次输入一个数:"))
except:
          print("不能输入汉字")





