import random
import ascii as d
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissor='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

a=['rock','paper','scissor']
b=[rock,paper,scissor]
while True:
    print(''' WELCOME TO 

██████████████████████████
█▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄███
██─▄─▄█─██─█─███▀██─▄▀████
▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
█████████████████████████████████
█▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀███
██─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄███
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀▀▀
██████████████████████████████████████████████
█─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
█▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
''')
    user_choice=int(input("Enter your Choice, 1 for rock,2 for paper, 3 for scissor: \n"))
    if not user_choice in range(1,4):
        print("Invalid choice")
        break
        
    comp_choice=random.randint(0,2)
    print(f"You chose\n {b[user_choice-1]}")
    print(f"{a[user_choice-1]}")
    print(f"Computer's Choice:\n{b[comp_choice]} ")
    print(a[comp_choice])
    if(user_choice==1 and comp_choice==2) or (user_choice==2 and comp_choice==0) or (user_choice==3 and comp_choice==1):
        print("You win")
    elif a[user_choice-1]==a[comp_choice]: 
        print("Draw")
    else:
        print("You lost")
    if(not input("Press Y to play the game again, N to stop:\n").upper()=="Y"):
        print("Thank You for playing: ")
        break
        


