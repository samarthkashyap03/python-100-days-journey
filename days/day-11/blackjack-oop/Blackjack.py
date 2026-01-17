import random
class Blackjack:
    def __init__(self):
        '''Contains Logic BlackJack Game\n
        Mehods:\n
        1.generate_cards() ->Distributes 2 cards each for user and Computer initially, followed by 1 card later\n
        2.fix_ace() -> Called when ace value has to be changed from 11 to 1\n
        3.check_blackjack() -> Check if user or computer hits blackjack, i.e sum=21\n
        4.check_winner() ->checks and returns the winner, user or computer or Draw\n
        5.calculate_sum(deck) -> Calculates the sum of a list, can be user deck or computer deck\n
        6.update_deck(deck) ->Appends a random card into the specidied deck\n
        7.computer_play() -> Fills cards to Computer deck till sum is 16
        '''
        self.user_deck=[]
        self.computer_deck=[]
        
    def generate_cards(self):
        """Distributes 2 cards each for user and Computer initially, followed by 1 card later"""
        cards={
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
        if len(self.user_deck)==0 and len(self.computer_deck)==0: 
            self.user_deck.extend(random.sample(list(cards.values()),k=2))
            self.computer_deck.extend(random.sample(list(cards.values()),k=2))
        else:
            return random.choice(list(cards.keys()))
    def start_game(self):
        """Initialises the game, generates 2 cards for user and computer, and handles ace logic automatically."""
        self.generate_cards()
        self.fix_ace(self.user_deck)
        self.fix_ace(self.computer_deck)

    def fix_ace(self,deck:list):
        """
        Called when ace value has to be changed from 11 to 1
        :param deck: A list containing all the card value, can be user or computer.
        :type deck: list
        """
        if self.calculate_sum(deck)>21 and 11 in deck:
            deck.remove(11)
            deck.append(1)
    def check_blackjack(self)->str:
        """Checks Blackjack condition, returns a string"""
        if sum(self.user_deck)==21:
            return 'user'
        if sum(self.computer_deck)==21:
            return 'computer'
    def calculate_sum(self,deck:list):
        """
        Returns the sum of the list
        
        :param deck: List of cards
        :type deck: list
        """
        return sum(deck)
    def check_winner(self)->str:
        """Computes the winner, and returns User or Computer"""
        if self.calculate_sum(self.user_deck)>21:
            return 'Computer'
        elif self.calculate_sum(self.computer_deck)>21:
            return 'User'
        elif self.calculate_sum(self.computer_deck)>self.calculate_sum(self.user_deck):
            return 'Computer'
        elif self.calculate_sum(self.user_deck)>self.calculate_sum(self.computer_deck):
            return 'User'
        else:
            return 'Draw'
    def update_deck(self,deck:list):
        """
        Appends a random card into the specidied deck
        :param deck: A list containing user or computer cards
        :type deck: list
        """
        deck.append(self.generate_cards())
        self.fix_ace(deck)
    def computer_play(self):
        """Generates cards in computer deck till a value is reached"""
        while self.calculate_sum(self.computer_deck)<16:
            self.update_deck(self.computer_deck)
    
    
    










