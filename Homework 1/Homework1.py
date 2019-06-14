"""
@author: Vaibhav Vishnu Shanbhag
@homework: HW 01
This code demonstrates the python code for rock, paper and scissors game
"""

from random import choice


def game():
    """
    I have defined a function game that has 3 other functions that runs
    according to computers response which is random
    """
    computer_response = choice(['rock', 'paper', 'scissor'])
    if computer_response == 'rock':
        computer_response_rock()
    elif computer_response == 'paper':
        computer_response_paper()
    else:
        computer_response_scissor()


def computer_response_rock():
    """this function is called in function game if the computer response is rock"""
    user_response = input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
    if user_response == 'r':
        print("Tie: we both chose rock")
        continue_play()
    elif user_response == 'p':
        print("paper beats rock - I win!")
        continue_play()
    elif user_response == 's':
        print("rock beats scissor - You win")
        continue_play()
    else:
        print("Thanks for playing!")
        quit()


def computer_response_paper():
    """this function is called in function game if the computer response is paper"""
    user_response = input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
    if user_response == 'r':
        print("Paper beats rock - You win")
        continue_play()
    elif user_response == 'p':
        print("Tie: we both chose paper")
        continue_play()
    elif user_response == 's':
        print("Scissor beats paper - I win")
        continue_play()
    else:
        print("Thanks for playing!")
        quit()


def computer_response_scissor():
    """this function is called in function game if the computer response is scissor"""
    user_response = input("Please choose 'R', 'P', 'S' or 'Q' to quit:")
    if user_response == 'r':
        print("Rock beats scissor - I win")
        continue_play()
    elif user_response == 'p':
        print("Scissor beats paper - You win!")
        continue_play()
    elif user_response == 's':
        print("Tie: we both chose scissor")
        continue_play()
    else:
        print("Thanks for playing!")
        quit()


def continue_play():
    """Here I a have used while loop to ask if the user wants to play the game if response is yes
    that is string 'y' then the logic will return to game function"""
    user_response = input("Do you want to play again? y/n")
    while user_response == 'y':
        return game()
    else:
        print("Thanks for playing!")




game() # this calls the function game()