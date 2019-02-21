import random
b=[]
c=[]
d=[]
for i in range(1,51):
    a=random.randint(-10, 10)
    if a>0:
        b.append(a)
    else:
        c.append(a)
d=b+c
print("正数的部分有:",b)
print("负数的部分有:",c)
print("所有的数是:",d)