from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
drinks_menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
coffee_maker.resources['water']=500
while True:
    user_choice=input(f"Enter your choice, {drinks_menu.get_items()}")
    if user_choice=='report':
        coffee_maker.report()
        money_machine.report()
    elif user_choice=='off':
        exit(0)
    else:
        drink=drinks_menu.find_drink(order_name=user_choice)
        if coffee_maker.is_resource_sufficient(drink=drink) and money_machine.make_payment(cost=drink.cost):
            coffee_maker.make_coffee(order=drink)
            




  
        
                

    

