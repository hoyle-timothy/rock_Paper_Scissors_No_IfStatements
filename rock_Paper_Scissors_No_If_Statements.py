import random #importing the random module. This module is utilized for the computer to randomely select 'rock', 'paper' or 'scissors'
import sys # importing the sys module. If the player chooses to quit the game, 'sys.exit' is utilized 
round = 0 #this variable is used to track the number of rounds played
playerwins = 0 # this variable is used to track the number of rounds the player has won
computerwins = 0 #this variable is used to track the number of rounds the computer has won


def endFunc ():
    '''this function handles exiting the program when a player wants to quit the game'''
    print("\nthanks for playing. Have a good day.")
    sys.exit()
    
def continueFunc ():
    '''this function handles continuing the program when a player chooses to play another round'''
    print("Awesome, lets play...")
    pass
    
def tieFunc ():
    '''this function handles a situation where both the player and the computer select the same element (rock, paper or scissors)'''
    print("It\'s a tie...boring!")
    print(f'\nPlayer score: {playerwins}\nComputer score: {computerwins}')
    
def winFunc ():
    '''this function handles tells the computer what to do when the player wins the round'''
    global playerwins 
    playerwins += 1
    print("You win!")
    print(f'\nPlayer score: {playerwins}\nComputer score: {computerwins}')
    
def loseFunc ():
    '''this function tells the computer what to do when the player loses the round'''
    global computerwins
    computerwins += 1
    print("Sorry you\'re a loser lol")
    print(f'\nPlayer score: {playerwins}\nComputer score: {computerwins}')
    
def invalidFunc1 ():
    '''this function tells the computer what to do when a player inputs something other than 'rock', 'paper' or 'scissors'''
    print("\nInvalid choice, please try again")
    pass

def invalidFunc2 ():
    '''this function tells the computer what to do when a player inputs something other than 'y' or 'n' when asked if they would like to continue'''
    print("\nInvalid choice, please try again")
    playAgain()
    
def playAgain ():
    '''this function handles asking the user if they would like to play another round. it also has input validation if the user enters something other than a 'y' or 'n'''
    again_choice = input('\nWould you like to play again? y/n ').lower()
    again_result = {'y': 0, 'n': 1}
    again_idx = again_result.get(again_choice,2)
    again_tuple = continueFunc,endFunc,invalidFunc2
    again_tuple[again_idx]()
    
while True:
    round += 1 #tracks the number of rounds played
    print(f"ROCK--PAPER--SCISSORS\n\nRound {round}; fight!")
    choice = input('Make your choice...if you dare: ').lower() #takes the user input, and forces it all to be lowercase
    print(f'\nYour choice was: {choice}')

    choice_dict = {'rock': 0, 'paper': 1,'scissors': 2} #assigns a numeric value to each possible valid choice
    
    '''the code below grabs the numeric value (value) of the user's choice (key) from 'choice_dict'. If the user selected key/value pair 
    does not exist in 'choice_dict', then 'choice_index' will default to a value of '3'''
    choice_index = choice_dict.get(choice,3) 

    choices = ['rock','paper','scissors'] #sets up a list of possible choices for the computer
    computer_choice = random.choice(choices) #utilizes the 'random' module to randomely select a value from the 'choices' list, and place it inside the 'computer_choice' variable
    print(f"Computer choice was: {computer_choice}")

    '''the below code takes the computer player's random choice, and uses that choice as a 'key' to grab the numeric 'value' from 'choice_dict'. 
    Then the code places that numeric value into the 'computer_index' variable'''
    computer_index = choice_dict.get(computer_choice)

    '''below is where most of the magic happens. Below is a list of 4 sub-lists, and the game's winner is determined by which number is ultimately
    selected by (or placed inside of) the result_idx variable; a '0' means the round has ended in a tie. A '1' means the player wins, a '2' means the 
    computer wins, and a '3' means that the player has input an invalid response. An explanation of how this is used can be found below'''
    result_matrix = [[0,2,1],[1,0,2],[2,1,0],[3,3,3]]
    
    '''the line below interacts with the magic 'result_matrix' to determine who wins the round. 'result_matrix' has 4 sub-lists; [0,2,1], [1,0,2], [2,1,0] and [3,3,3].
    the first index in the line below, [choice_index], contains the value of the players choice and determines the sub-list that is selected. For instance, the value 
    of 'rock' is '0' (see line 60) and so if the player chose 'rock' then the sub-list at position '0' would be selected, which is [0,2,1]. 
    Next the computer's random choice found in [computer_index] is used to select the number within the sub-list. In the previous example, the player had 
    chosen 'rock', which has a value of '0', so sub-list [0,2,1] was selected. If the computer then chose 'paper', which has a value of '1' (again, see line 60), then
    the number at position '1' would be selected. The value at position '1' within [0,2,1] is '2', which would result in the computer winning. Props to you if
    you took the time to read/understand this!'''
    result_idx = result_matrix[choice_index][computer_index]

    '''the two lines of code below handle the different possible outcomes of a tie ('0', so call function 'tieFunc'), the player winning ('1', so call function 'winFunc')
    etc. The line below 'result_dict' is a nifty little trick that I learned from a really good cyber security coder; it uses an index value as a key to call a 
    function from a dictionary. In this case, the dictionary 'result_dict'.'''
    result_dict = {0:tieFunc,1:winFunc,2:loseFunc,3:invalidFunc1}
    result_dict[result_idx]()
    playAgain()