import random
class Hangman:
    def __init__(self,word_list:list,into_art:str,Hangman_art:list):
        self.lives=len(Hangman_art)
        self.score=0
        self.chosen_word=list(random.choice(word_list))
        self.guess_list=["_"]*len(self.chosen_word)
        self.hangman_art=list(reversed(Hangman_art))
        self.welcome_art=into_art
        
    def display_guess(self):
        return " ".join(self.guess_list)
    def check_win(self):
        if self.guess_list==self.chosen_word:
            print(f"You win, the Word is {self.display_guess()}")
            return True
    def check_letter(self,input):
        if input.lower() in self.chosen_word:
            return True
    def is_letter_present(self,input):
        if input in self.guess_list:
            return True
    def is_game_over(self):
        if self.lives==0:
            return True
    def play(self):
        print(self.welcome_art)
        while self.lives>0:
            if self.check_win():
                break
            print(f"The word to be Guessed: {self.display_guess()}")
            user_input=input("Enter the letter to be guessed: ")
            if self.is_letter_present(input=user_input):
                print(f"Letter {user_input} already Guessed!")
                continue
            if self.check_letter(input=user_input):
                for i in range(len(self.chosen_word)):
                    if self.chosen_word[i]==user_input:
                        self.guess_list[i]=user_input
            else:
                self.lives-=1
                print(self.hangman_art[self.lives])
                print(f"You have {self.lives} lives left")
                if self.is_game_over():
                    print(f"Game Over, the correct word was: {''.join(self.chosen_word)}")
                    break






