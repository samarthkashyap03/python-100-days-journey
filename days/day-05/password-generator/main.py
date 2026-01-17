import random
import string
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)
let=int(input("Enter how many letter you need:\n"))
num=int(input("Enter how many numbers you need:\n"))
sym=int(input("Enter how many symbols you need:\n"))
p=random.choices(letters,k=let)+random.choices(numbers,k=num)+random.choices(symbols,k=sym)
random.shuffle(p)
print(f'Your Password: {"".join(p)}')



