# random number guessing game
import random

while True:
    flag = True
    while flag:
        num = input("Please put a number here for start:")

        if num.isdigit():
            print("let's play!")
            num = int(num)
            # this is for stop going back to while at front after you input a valid digit
            flag = False
        else:
            print("worng type, please try again!")

    seceret = random.randint(1, num)

    guess = None
    count = 1

    while guess != seceret:
        guess = input("please type a number between 1 and" + str(num) + ":")
        if guess.isdigit():
            guess = int(guess)

        if guess == seceret:
            print("You got it!")
        else:
            print("Please try again!")
            count += 1

    print("it took you ", count, " times")
