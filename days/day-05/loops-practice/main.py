a=[]
import random as r
for i in range(0,int(input("Enter the number of elements in the list:\n"))):
    a.append(r.randrange(1,100))
print("List updated successfully")
max=a[0]
min=a[0]
print(a)
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
print(f"The highest score is {max} and the Lowest score is {min}")    
#alternate use sort function or max and min function

