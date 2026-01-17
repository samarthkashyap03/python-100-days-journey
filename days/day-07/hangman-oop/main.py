from hangman import Hangman
import art
hangman=Hangman(word_list=art.words,into_art=art.welcome_art,Hangman_art=art.HANGMANPICS)
print(hangman.chosen_word)
hangman.play()
