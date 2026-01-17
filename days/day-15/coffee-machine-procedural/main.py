from data import MENU,resources,art,coffee_map
MONEY=0.0

def display_art():
    #prints the welcome message and coffee ASCII ART
    print('Welcome to Coffee machine!!\n')
    print(art)

def select_coffee():
    #Takes the user input, asking which coffee and returns the same
    choice=input("""Enter the coffee you want: 
                 1 for espresso: 
                 2 for latte:
                 3 for cappuccino: \n""")
    #if user enters wrong input, take input again
    while choice not in ['report','off','1','2','3']:
            print("Invalid Choice")
            choice=select_coffee()
    return choice

def print_report():
    #prints the user report
    global MONEY
    print("\n-------------REPORT----------- ")
    for i in resources:
        print(i,resources[i])
    print(f"Money: {MONEY}")

def is_resources_enough(coffee):
    #Computes if resources are sufficient for that coffee
    #if not sufficient, it will tell which ingredient is not enough.
        for i in  resources:
            if MENU[coffee]['ingredients'][i]>resources[i]:
                print(f"{i} not enough for {coffee}!")
                return False
        return True

def process_coins():
    #This function asks the users to inpurt the coins, calculates and returns the total value of how much money is inserted.
    quarters =int(input('Enter Quarters:'))
    dimes =int(input('dimes:'))
    nickles =int(input('Nickles:'))
    pennies =int(input('Enter Pennies:'))
    #Calculate total money
    total_money=(0.25*quarters)+(0.10*dimes)+(0.05*nickles)+(0.01*pennies)
    return total_money

def update_resources(coffee):
    #Modify the resources after a successfull transaction.
    for i in resources:
        resources[i]-=MENU[coffee]['ingredients'][i]
    print(f"------------Your {coffee} is ready, please collect ------")

def calculate_change(coffee,input_money):
    #This function calculates the change to be given to user, when they enter more money.
    change=input_money-MENU[coffee]['cost']
    return change 

def make_coffee(coffee):
    #Takes coffee name as input -> Core logic of coffee machine
    global MONEY
    if is_resources_enough(coffee)==True:
                print("Enough resources, collecting money!")
                #if enough resources available, collect coins from user, else display warning!
                input_money=process_coins()
                if input_money<MENU[coffee]['cost']:
                    #if entered amount is not sufficient for making a type of coffee, return warning
                    print("Not enough money, Money Refunded")
                    return
                else:
                    #if the amount is more or equal to what is required:
                    #1. Calculate change 
                    #2. Redund the user the extra amount if extra
                    #3. Modify the existing resources
                    #4. Give the coffee to the user
                    change=calculate_change(coffee=coffee,input_money=input_money)
                    print(f"""
                        {coffee} cost -> {MENU[coffee]['cost']}$
                        You put {round(input_money,2)} $
                        Refunded {round(change,2)}, preparing coffee :)""")
                    update_resources(coffee=coffee)
                    MONEY+=(input_money-change)

def play():
    #Main Loop of game
    global MONEY
    display_art()
    while True:
        user_choice=select_coffee()
        if user_choice=='report':
            print_report()
        elif user_choice=='off':
            print("System Shut Down::---------------")
            exit(0)
        else:
            coffee=coffee_map[user_choice]
            make_coffee(coffee)

play()
    