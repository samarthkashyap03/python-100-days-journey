import random
a=[1,2,3,7,8]
num=3
while num>0:
    a.append(round(random.random(),2))
    num-=1
print(a)