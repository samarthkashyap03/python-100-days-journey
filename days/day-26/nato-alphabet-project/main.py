import pandas as pd
import string

#Constants
FILE_NAME="nato_phonetic_alphabet.csv"

#Main Script
data_from_csv=pd.read_csv(FILE_NAME) #Read the csv file as a pandas Dataframe
#Make a (letter,code) dict using pandas iterrows() function and dict comprehension
letter_encodings_dict={value.letter:value.code for index,value in data_from_csv.iterrows()}
#Ask user input

user_input=input("Enter your name:").strip().upper()

#Check if user has inputted anything else than letters in their name, if yes, handle the same!
user_input=[i for i in user_input if i in string.ascii_uppercase]
#Create a list of phonetic values for each letter in the name
letter_to_phonetic_list=[letter_encodings_dict[i] for i in user_input]
#Display the same
print(letter_to_phonetic_list)

