import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
''')
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
HANGMANPICS.reverse()
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
def choose_word():
    lives=7
    word=list(random.choice(words))
    guess=["_"]*len(word)
    return lives,word,guess
lives,word,guess=choose_word()
hint_count=0
while True:
    print(f"The word to be Guessed is {' '.join(guess)}")
    if guess==word:
        print(f"You WIN, The word {''.join(word)} is guessed Correctly")
        break
    user_input=input("Enter a Letter to guess:\n").lower()
    if user_input in guess:
        print(f"You have already Guessed {user_input}")
        continue
    if user_input in word:
        for i in range(len(word)):
            if word[i]==user_input:
                guess[i]=user_input
    else:
        lives-=1
        print(f"You have guessed wrong,Letter {user_input} is not in the word. ")
        print(f"You have {lives} Lives left")
        print(HANGMANPICS[lives])        
        if(lives==0):
            print(f"Game Over, the word to guess was: {''.join(word)} ")
            if input("Do you want to play the game Again? Y for Yes, N for No:\n").lower()=='y':
                lives,word,guess=choose_word()
                continue
            else: 
                print('Thank You for playing Hangman')
                break
        else:
            if input("Do You need help,(Y or N), it will cost 1 life per 2 hints: \n").lower()=='y':
                hint_count+=1
                if hint_count%2==0:
                    lives-=1
                    print("You used 2 hints, -1 life!")
                i=random.randrange(0,len(word))
                guess[i]=word[i]
                continue



