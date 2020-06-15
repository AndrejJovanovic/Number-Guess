import sys

print("Welcome to my mega python project. Which project do you want to run: ")
print("")
print("1. Rolling Dice")
print("2. Number Guess")
print("3. Mad Libs")
print("4. Rock Paper Scisors")
print("")
print("Enter the number: ")
choice = input("")
if choice == "1":
    exec(open("./rolling-dice/rolling-dice.py").read())
if choice == "2":
    exec(open("./number-guess/number-guess.py").read())
if choice == "3":
    exec(open("./mad-libs/mad-libs.py").read())
if choice == "4":
    exec(open("./rock-paper-scisors/rps.py").read())
else:
    sys.exit()