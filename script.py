print("christopher's game")
count = 1

flag = True
while flag:
    num = input("a number you want to play with")
    guess = int(num)
    if guess == 8:
        print("you got the number")
        flag = False
    else:
        print("please try another num!")
        count += 1
print("it took you " + str(count) + " times to get the right number!")
