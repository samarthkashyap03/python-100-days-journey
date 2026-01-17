import random
print('''
 __          ________ _    _____ ____  __  __ ______   _______ ____  
 \ \        / /  ____| |    / ____/ __ \|  \/  |  ____| |__   __/ __ \ 
  \ \  /\  / /| |__  | |   | |   | |  | | \  / | |__       | | | |  | |
   \ \/  \/ / |  __| | |   | |   | |  | | |\/| |  __|      | | | |  | |
    \  /\  /  | |____| |___| |___| |__| | |  | | |____     | | | |__| |
     \/  \/   |______|______\_____\____/|_|  |_|______|    |_|  \____/ 
      ''')
print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
      ''' )
words = [
    "apple", "grape", "banana", "orange", "cherry", "lemon",
    "table", "chair", "shelf", "glass", "clock", "sofa",
    "forest", "desert", "island", "ocean", "valley", "plains",
    "python", "coding", "script", "input", "output", "buggy",
    "dragon", "wizard", "castle", "sword", "knight", "beast",
    "rocket", "planet", "space", "orbit", "aster", "alien",
    "cloud", "storm", "breeze", "thunder", "light", "windy",
    "school", "pencil", "eraser", "marker", "notebook", "chalk",
    "heart", "brain", "nerve", "blood", "muscle", "lungs",
    "smile", "laugh", "happy", "sadly", "angry", "sorry"
]
hangman_art=[
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''']
hangman_art.reverse()
com_word=random.choice(words)
comp_word=list(com_word)
copy=[i for i in comp_word]
print("The word to be Guessed is :\n")
dash=[]
dash_str=""
for i in range(0,len(comp_word)):
    dash.append("_ ")
for i in dash:
    dash_str+=i
print(dash_str)
user_lives=6
print(hangman_art[6])
while user_lives>0:
    user_input=input("\nGuess a letter:\n")
    if not user_input in comp_word:
        user_lives-=1
        print(hangman_art[user_lives])
        print(f"You Have {user_lives} Lives left")
    else:
        c=int(comp_word.index(user_input))
        dash[c]=user_input
        comp_word[c]="_"
        str=""
        for i in dash:
            str+=i
        print(str)
        if dash==copy:
            print("You win")
            exit(0)
print(f"You lost all the Lives, Try again:, the word was {com_word} ")