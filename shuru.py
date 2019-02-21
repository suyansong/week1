# a=input("请输入第一个人的生日:")
# b=input("请输入第二个人的生日:")
# if a<b:
#     print("1楼大")
# else:
#     print("二楼大")

a=2
b=1
sum=0
for i in range(1,21):
    sum+=a/b
    t=a
    a=a+b
    b=t
print(sum)