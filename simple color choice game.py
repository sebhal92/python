#simple color choice game in text mode
print("Hi, this is simple color choice game in text mode")

#import random module
import random

#show rules
print("Rules:"+ "\nType number from 1 to 5 and check computer choice")

#set scores to 0
computer_score = 0
player_score = 0



while True:
    print("red=1 \nyellow=2 \norange=3 \ngreen=4 \nblue=5 \ntype number: ")

    #input value of player choise
    player_choice = int(input("Player choose: "))
    
    #while loop to check value is in range
    while player_choice > 5 and player_choice < 1:
        #if typed value is out of range show below text
        player_choice = int(input("Enter value between 1 and 5: "))
        
    #match colors to numbers in player_choice variable 
    if player_choice == 1:
        player_choice_color = "red"
    elif player_choice == 2:
        player_choice_color = "yellow"
    elif player_choice == 3:
        player_choice_color = "orange"
    elif player_choice == 4:
        player_choice_color = "green"
    else:
        player_choice_color = "blue"
        
    #show user choice
    print("You choose: " + player_choice_color)
    
    #random computer choise from range 1 to 5
    computer_choice = random.randint(1, 5)
    
    #loop white to equal choices
    while computer_choice == player_choice:
        computer_choice = random.randint(1, 5)
        
    #match colors to numbers in computer_choice variable
    if computer_choice == 1:
        computer_choice_color = "red"
    elif computer_choice == 2:
        computer_choice_color = "yellow"
    elif computer_choice == 3:
        computer_choice_color = "orange"
    elif computer_choice == 4:
        computer_choice_color = "green"
    else:
        computer_choice_color = "blue"
        
    #show computer choice
    print("computer choose: " + computer_choice_color)
    
    #winning condition
    if(player_choice_color == computer_choice_color):
        player_score += 1
        #show scores
        print("player score: "+str(player_score))
        print("computer score: "+str(computer_score))
    else:
        computer_score +=1
        #show scores
        print("player score: "+str(player_score))
        print("computer score: "+str(computer_score))
        
    print("Do you want play again? Y/N")
    answer = input()
    
    #if user type n or N condition is True and game will stop
    if answer == "n" or answer == "N":
        break

#when game stop it will show winner
if computer_score == player_score:
    print("Tie - nobody wins")
    print("Thanks for playing")
elif computer_score < player_score:
    print("Player wins")
    print("Thanks for playing")
else: 
    print("Computer wins")