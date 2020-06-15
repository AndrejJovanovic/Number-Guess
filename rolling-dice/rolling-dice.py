import sys
from numpy import random

while 1:
    print("Role the dice? Answer y to role or n to exit:")
    state = input("")
    if state == "n":
        print("Exiting...")
        sys.exit()
    if state == "y":
        x = random.choice([1, 2, 3, 4, 5, 6])
        print(x)
    else:
        print("Please answer with y or n")