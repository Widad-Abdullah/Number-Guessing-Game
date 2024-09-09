import art
import random

EASY_DIFFICULTY_TRIES=10
HARD_DIFFICULTY_TRIES=5

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")

number=random.randint(1,100)
print(number)

def set_difficulty():
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty=='easy':
        return EASY_DIFFICULTY_TRIES
    elif difficulty=='hard':
        return HARD_DIFFICULTY_TRIES
    else:
        print("Enter a valid difficulty level!")

def decision(num,tries):
    while tries != 0:
        print(f"You have {tries} attempts remaining to guess the number.")
        tries -= 1
        guess = int(input("Make a guess: "))
        if guess==num:
            print("You have guessed right. You Win!!!")
            tries=0
        elif max(guess, num)-min(guess,num)>9 and guess>num:
            print("Too High.\nGuess again.")
        elif max(guess, num)-min(guess,num)>9 and guess<num:
            print("Too Low.\nGuess again.")
        else:
            print("You are close.\nGuess again.")

attempts=set_difficulty()
decision(number,attempts)


