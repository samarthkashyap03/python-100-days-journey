print("Welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M, or L")
cost=0
if size=="S":
    cost+=15
elif size=="M":
    cost+=20
elif size=="L":
    cost+=25
else:
    print("Invalid Input")
    exit(0)
pepperoni=input('Do you want Pepperoni? Y or N: ')
if pepperoni=="Y":
    if(size=="S"):
        cost+=2
    else:
        cost+=3
cheese=input("Do you need cheese, Y or N: ")
if cheese=="Y":
    cost+=1
print(cost)