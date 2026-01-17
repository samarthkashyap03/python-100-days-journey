print("Welcome to the tip calculator")
total_bill=int(input("Enter the total bill amount: "))
tip=int(input("Enter the tip percentage, 10, 12 or 15"))
num_people=int(input("How many people to split the bill? "))
sub_total=total_bill+(total_bill*(tip/100))
print(sub_total)
split=sub_total/num_people
print(f"Each has to pay {round(split, 2)}")
