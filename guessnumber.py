import random

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    while guess != randomNumber:
        guess = int(input(f"Test Your Luck Between 1 and {x}: "))
        if guess < randomNumber:
            print("You are low lol :S ")
        elif guess > randomNumber:
            print("You are too high -_- ")

    print(" You are lucky dude ")

Luck = input("Do you want big luck or small luck your choise; ")

def do_it_you_can(x):
    low = 1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low
        feedback = input(f"Can i made it 0_0 Is it {guess}  h,l or c ???" )
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("You done it ^-^ ")


if Luck == "small":
    guess(10)
elif Luck == "big":
    guess(50)

