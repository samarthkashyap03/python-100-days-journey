from Blackjack import Blackjack
game=Blackjack()
def play():
    user_deck:list=game.user_deck
    computer_deck:list=game.computer_deck
    game.start_game()
    print(f"Your Deck of Cards: {user_deck}, Total={game.calculate_sum(user_deck)}")
    print(f"Computer Deck: {computer_deck[0]}, Total={computer_deck[0]}")
    check_blackjack=game.check_blackjack()
    if check_blackjack=='user':
        print(f"You hit Blackjack, You win!")
        return
    if check_blackjack=='computer':
        print(f"Computer hits Blackjack, You lose!")
        return
    while game.calculate_sum(user_deck)<21:
        ask_user=input("Press Y to draw one more card, C to call:").lower()
        if ask_user=='y':
            game.update_deck(user_deck)
            print(f"Your Deck of Cards: {user_deck}, Total={game.calculate_sum(user_deck)}")
        else:
            break
    
    game.computer_play()
    print(f"Your Deck of Cards: {user_deck}, Total={game.calculate_sum(user_deck)}")
    print(f"Computer Deck: {computer_deck}, Total={game.calculate_sum(computer_deck)}")
    winner=game.check_winner()
    if winner!='Draw':
        print(f"{winner} Wins")
    else:
        print("Draw")
play()
    
            