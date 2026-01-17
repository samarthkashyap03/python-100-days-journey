"""a=[]
with open('C:\\Users\samar\Desktop\PYTHON COURSE\Day 25- Working with CSV\weather_data.csv','r') as f:
    for i in f:
        b=i.strip('\n')
        a.append(b)
print(a)"""
"""import csv
with open('C:\\Users\samar\Desktop\PYTHON COURSE\Day 25- Working with CSV\weather_data.csv','r') as f:
    a=csv.reader(f)
    temperature=[]
    for i,j,k in a:
        if j=='temp':
            pass
        else:
            temperature.append(int(j))
print(temperature)"""
import pandas as pd
"""a=[]
data=pd.read_csv('C:\\Users\samar\Desktop\PYTHON COURSE\Day 25- Working with CSV\weather_data.csv')
a=data['temp']

print(f"max = {a.max()}")
monday=data[data.day=='Monday']
print(f"Temp in F = {((monday.temp *(9/5))+32)}")"""

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20251229.csv")
grey=len(data[data['Primary Fur Color']=='Gray'])
red=len(data[data['Primary Fur Color']=='Cinnamon'])
black=len(data[data['Primary Fur Color']=='Black'])
print(grey)
print(red)
print(black)
my_dict={
    'color':['gray','red','black'],
    'count':[grey,red,black]
}
frame=pd.DataFrame(my_dict)
print(frame)
frame.to_csv('new_data.csv')
