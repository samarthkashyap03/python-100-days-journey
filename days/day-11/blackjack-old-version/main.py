import random
print(''' 
 __        _______ _     ____ ___  __  __ _____   _____ ___  
 \ \      / / ____| |   / ___/ _ \|  \/  | ____| |_   _/ _ \ 
  \ \ /\ / /|  _| | |  | |  | | | | |\/| |  _|     | || | | |
   \ V  V / | |___| |__| |__| |_| | |  | | |___    | || |_| |
    \_/\_/  |_____|_____\____\___/|_|  |_|_____|   |_| \___/ 
                                                             

 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\.
                       _/ |                
                      |__/       
      ''')
cards={
    "Ace":11,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    "King":10,
    "Jack":10,
    "Queen":10
}
player_set=[]
computer_set=[]
#choice=input("Press D for playing your deck:/n")
player_set.extend([random.choice(list(cards.keys())),random.choice(list(cards.keys()))])
computer_set.append(random.choice(list(cards.keys())))
print(player_set)
sum_of_player=[]
sum_of_computer=[]
for i in player_set:
    sum_of_player.append(cards.get(i))
sum1=sum(sum_of_player)
sum_of_computer.append(cards[computer_set[0]])
sum2=sum(sum_of_computer)
print(f"The players deck is {player_set} and the total value is: {sum1}")
print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
while sum1<21:
    choice=input("Do you want to play another card? Press Y for yes, N for No:\n")
    if choice.lower()=='y':
        player_set.append(random.choice(list(cards.keys())))
        for i in player_set:
            sum_of_player.append(cards.get(i))
        sum1=sum(sum_of_player)
        print(f"The players deck is {player_set} and the total value is: {sum1}")
        print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
    else: 
        print(f"The players deck is {player_set} and the total value is: {sum1}")
        count=1
        while sum2<21:
            computer_set.append(random.choice(list(cards.keys())))
            sum_of_computer.append(cards[computer_set[count]])
            count+=1
            sum2=sum(sum_of_computer)
        if sum2<sum1:
            print(f"The players deck is {player_set} and the total value is: {sum1}")
            print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
            print("You win")
            exit(0)
        else:
            if sum2>21:
                print(f"The players deck is {player_set} and the total value is: {sum1}")
                print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
                print("You Win, the opponent went over")
                exit(0)
            else:
                print(f"The players deck is {player_set} and the total value is: {sum1}")
                print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
                print("You Lose")
                exit(0)

print(f"The players deck is {player_set} and the total value is: {sum1}")
print(f"The Computer's deck is {computer_set} and the total value is: {sum2}")
print("You went over, you loose")