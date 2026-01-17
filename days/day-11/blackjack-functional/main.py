#Black jack game
# Sum of cards must be <=21
#Deck of cards : 2 to 10, face values, J,Q,and K - 10, ace- can be 1 or 11
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
deck_of_cards={
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    'King':10,
    'Queen':10,
    'Jack':10,
    'Ace':11 ,
    }
def compute_winner(user_deck,computer_deck):
    #Function to compare the scores and calculate the winner
    user_total=sum_of_deck(user_deck)
    computer_total=sum_of_deck(computer_deck)
    if user_total>21:
        print("You Lose")
    elif computer_total>21:
        print("You win")
    elif user_total==computer_total:
        print("Draw :)")
    elif user_total>computer_total:
        print("You win")
    else:
        print("You lose!!")

def sum_of_deck(cards):
    #Function to compute the sum of the values of the cards inside list:cards
    return sum(cards)

def ace_replacement(card):
    #To replace the value of ace from default 11 to 1 if required
    while sum_of_deck(card)>21 and 11 in card:
        card.remove(11)
        card.append(1)

def draw_cards():
    #Function to initialise 2 arrays, fill them each with 2 cards, check for weather to change ace value, and return the 2 arrays.
    computer_deck=[]
    user_deck=[]
    for _ in range(2):
        user_deck.append(random.choice(list(deck_of_cards.values())))
        computer_deck.append(random.choice(list(deck_of_cards.values())))
        ace_replacement(user_deck)
        ace_replacement(computer_deck)
    
    return user_deck,computer_deck

def check_black_jack(user,comp):
    #Function to check blackjack condition initially, i.e if sum equals 21.
    if sum_of_deck(user)==21 and sum_of_deck(comp)==21:
        print("Both hit Jackpot, Its a Draw:)")
        return True
    elif sum_of_deck(user)==21:
        print("You win, as you hit BlackJack!")
        return True
    elif sum_of_deck(comp)==21:
        print("Computer wins by Hitting Blackjack, You Lose!")
        return True
    
    else:
        return False

def is_play_game():
    #To ask user to continue or quit the game
    if input("Do you want to play Black jack?: ").lower()=='y':
        return True
    else:
        print("Thank you for playing Blackjack!!!")
        return False

def print_deck_info(card1,card2):
    #Prints the deck information, for both user and computer
    print(f"Your deck of cards {card1}, total is: {sum_of_deck(card1)}")
    print(f"Computer Deck {card2}, total is :{sum_of_deck(card2)}")

def insert_one_card(card):
    #Picks a random card from the deck, and inserts it to user and computer deck
    random_card=random.choice(list(deck_of_cards.values()))
    card.append(random_card)
    ace_replacement(card)

def play_game():
    user_deck,computer_deck=draw_cards()
    if check_black_jack(user=user_deck,comp=computer_deck):
        print_deck_info(user_deck,computer_deck)
        return
    
    print(f"Your deck of cards {user_deck}, total is: {sum(user_deck)}")
    print(f"Computer Deck {[computer_deck[0]]}, total is :{computer_deck[0]}")

    while sum_of_deck(user_deck) <=21:
        user_input=input("Do you want to draw another card or Call, Y or C:").lower()
        if user_input=='y':
            insert_one_card(user_deck)
            print(f"Your deck of cards {user_deck}, total is: {sum(user_deck)}")
        elif user_input=='c':
            break
        else:
            print("Wrong input, Try again:")
            continue
    
    while sum_of_deck(computer_deck)<=16:
        insert_one_card(computer_deck)
    
    print_deck_info(card1=user_deck,card2=computer_deck)
    compute_winner(user_deck,computer_deck)
    
while is_play_game():
    play_game()
    #Main Loop
    
    
            
