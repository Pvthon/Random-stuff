import time
import random

name = input("hello my name is James what is your name?: ")
time.sleep(1)
print("Hello "+name)
time.sleep(1)
print("i want to play a number game")
time.sleep(1)

ask = input ("Will you play a number game with me? (y) or (n)")
time.sleep(1)
if ask == ("y"):print("Great")
if ask == ("n"):print("oh ok")
if ask == ("n"): quit()


n = random.randint(1, 50)
guess = int(input("Enter an number from 1 to 50: "))
while True:
    if guess < n:
        print ("guess is to low")
        guess = int(input("Enter an number from 1 to 50: "))
    elif guess > n:
        print ("guess is to high")
        guess = int(input("Enter a number from 1 to 50: "))
    else:
        print ("Well done, that is correct!")
        break

