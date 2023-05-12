import time
import random

name = input("hello my name is James what is your name?: ")
time.sleep(2)
print("Hello "+name)
time.sleep(2)
print("i want to play rock paper scissors")
time.sleep(2)

ask = input ("Will you play rock paper scissors with me (y) or (n)")
time.sleep(2)
if ask == ("y"):print("Great")
if ask == ("n"):print("oh ok")
if ask == ("n"):quit()

options = ("r", "p", "s")
running = True

while running:

    player = None
    ai = random.choice(options)

    while player not in options:
        player = input("Enter a choice (r, p, s): ")
    time.sleep(1)
    print(f"Player: {player}")
    time.sleep(1)
    print(f"Computer: {ai}")

    if player == ai:
        print("Draw!")
    elif player == "r" and ai == "s":
        print("wow your good " +name)
    elif player == "p" and ai == "r":
        print("wow your good " +name)
    elif player == "s" and ai == "p":
        print("wow your good " +name)
    else:
        print("Hahaha i won")

