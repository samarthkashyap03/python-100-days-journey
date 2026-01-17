height=int(input('Enter the height in cms: '))
if height>120:
    print("You can ride roller coaster")
    a=int(input("Enter age: "))
    cost=0
    if a<12:
        cost=5
    elif a>=12 and a<=18:
        cost=7
    else:
        cost=12
    if input("Do you need a photo?, Y or N")=="Y":
        print(f"The total cost is {cost+3}")
    else:
        print(f"The total cost is {cost}")
else: 
    print("Not allowed due to height restrictions")