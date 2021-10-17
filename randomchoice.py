from math import e
import random

FirstThing = input("First: ")
SecondThing = input("Second: ")
ThirdThing = input("Third: ")

choicess = random.randint(1,3)
if choicess == 1:
    print(FirstThing)
elif choicess == 2:
    print(SecondThing)
elif choicess == 3:
    print(ThirdThing)
