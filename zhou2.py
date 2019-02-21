import random
b=[]
for i in range(1,51):
    a=random.randint(-10, 10)
    b.append(a)
print(b)
print(b[1])
c=[]
d=[]
for j in range(0,50):
    if b[i]>=0:
        d.append(b[i])
    elif b[i]<0:
        c.append(b[i])
print(c)
print(d)




