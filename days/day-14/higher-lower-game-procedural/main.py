import game_data
import random
from art import VS, Welcome_logo

def print_comparisons(a, b):
    print(f"COMPARE A: {a['name']}, a {a['description']}, from {a['country']}")
    print(VS)
    print(f"COMPARE B: {b['name']}, a {b['description']}, from {b['country']}")

def generate_comparisons(prev=None):
    #Return (A, B). If prev is given, use it as A.
    if prev is None:
        a, b = random.sample(game_data.data, k=2)
    else:
        a = prev
        b = random.choice(game_data.data)
        while b == a:
            b = random.choice(game_data.data)
    return a, b

def is_correct(user_input, a, b):
    #Returns True if user’s guess is correct else False
    A = a['follower_count']
    B = b['follower_count']
    return (user_input == 'a' and A > B) or (user_input == 'b' and B > A)

def play():
    print(Welcome_logo)
    score = 0

    # First comparison (no previous winner yet)
    a, b = generate_comparisons()

    while True:
        print_comparisons(a, b)

        guess = input("Who has more followers? Type A or B: ").lower()
        while guess not in ('a', 'b'):
            guess = input("Type only 'A' or 'B': ").lower()

        if is_correct(guess, a, b):
            score += 1
            print(f"You guessed correctly! Current score: {score}")

            # Winner becomes the next A
            winner = a if guess == 'a' else b

            # Generate next round with that winner
            a, b = generate_comparisons(prev=winner)

        else:
            print(f"Game over! Final score: {score}")
            return  # cleaner than exit(0)

play()
