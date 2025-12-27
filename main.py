import random


# get_choices is a function here

def get_choices():
    
    player_choice = input("Enter a choice (rock, paper, scissor) : ")       # this var is taking input from user
    
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)
    
    choices = {"player" : player_choice, "computer" : computer_choice}      # choices is a dictionary (key-value pair)
    
    return choices
    



def check_win(player, computer):
    
    print(f"You chose {player}, Computer chose {computer}")
    
    if player == computer:
        return "Its a Tie."
        
    elif player == "rock" :
        if computer == "scissor":
            return "Rock smashes Scissors! You Win!"
        else:
            return "Paper covers Rock! You Loose!"
    elif player == "paper" :
        if computer == "rock":
            return "Paper covers Rock! You Win!"
        else:
            return "Scissors cuts Paper! You Loose!"
    elif player == "scissor" :
        if computer == "paper":
            return "Scissors cuts Paper! You Win!"
        else:
            return "Rock smashes Scissors! You Loose!"
            
    return "Error in check_win"



choices = get_choices()

result = check_win(choices["player"], choices["computer"])

print (result)







