import random

luckyno = random.randint(1,10)
guess = 0
while guess != luckyno:
    guess = int(input("Guess any no between 1 and 10"))
    if guess == luckyno:
        print("You got it")
        print("lucky no is {0}".format(luckyno))
    else :
        print("Better luck next time")


