import sys
import os
from numpy import random

player_score = 0
pc_score = 0

def compareChoices(player_choice, computer_choice):
    
    global player_score
    global pc_score

    print("Player choosed: " + player_choice + " and PC choosed: " + computer_choice)
    if player_choice == computer_choice:
        print("Tie!")
    if player_choice == "rock":
        if computer_choice == "scisors":
            print("Player won!")
            player_score = player_score + 1
        if computer_choice == "paper":
            print("PC won")
            pc_score = pc_score + 1
    if player_choice == "paper":
        if computer_choice == "rock":
            print("Player won!")
            player_score = player_score + 1
        if computer_choice == "scisors":
            print("PC won")
            pc_score = pc_score + 1
    if player_choice == "scisors":
        if computer_choice == "paper":
            print("Player won!")
            player_score = player_score + 1
        if computer_choice == "rock":
            print("PC won")
            pc_score = pc_score + 1

print("Welcome to the trilling game of rock paper scisors!")
while 1:
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("Player: " + str(player_score))
    print("PC: " + str(pc_score))
    print("Choose wisely between rock - paper - scisors")
    player_choice = input("")
    if player_choice == "exit":
        print("Exiting...")
        sys.exit()
    computer_choice = random.choice(["rock", "paper","scisors"])
    compareChoices(player_choice, computer_choice)
    