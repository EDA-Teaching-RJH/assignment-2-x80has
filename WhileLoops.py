### Part Two -- your code goes here. 
import random
rightnum = random.randint(1, 100)
guess = int(input("guess a number between 1 and 100: "))

while guess != rightnum:
    if guess < rightnum:
        print("Too low, try again!")
    elif guess > rightnum:
        print("Too high, try again!")
    guess = int(input("Enter your guess: "))
print("guessed right big up")