print('''
      *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
print("Welcome to Tressure Island, your mission is to find the Tressure in this island!! ")
way=input("Enter the way you want to proceed, 'left(L)' or 'right(R)' ??\n")
if way=='L':
    print("You/'ve come accross a lake, pick your choice, Do you want to swim and cross the river or wait for a boat?? ")
    choice1=input("\n Press 'S' to swim, 'W' to wait:\n ")
    if choice1=="S":
        print("You have drowned in the lake, Game Over")
        exit()
    elif choice1=="W":
        print("You have come to an unknown place using the boat, and it has three doors \n RED, BLUE AND YELLOW")
        door=input("Pick your choice! Press 'R' for red, 'B' for Blue, and 'Y' for yellow:\n ")
        if door=="R":
            print("Burned by Fire, Game over: ")
            exit()
        elif door=="Y":
            print("You win, Congratulations on finding the tressure!!")
            exit()
        elif door=="B":
            print("Eaten by beasts, Game over!!")
            exit
        else:
            print("Wrong choice, game over!")
            exit(0)
    else:
        print("Wrong Option, restart the game: ")
        exit
else:
    print("You have fell into a hole, Game Over!! Better Luck next time!!")
    exit(0)   
    