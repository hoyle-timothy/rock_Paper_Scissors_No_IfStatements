import random
round = 0
player_score = 0
computer_score = 0

def play_control(bout):
    '''this function has two jobs; 1st job, ask the user if they'd like to play and perform input validation on their response. 
    2nd job, after the user has already played a round, ask them if they'd like to play again and perform input validation on their response again.
    The number of rounds played is tracked with the 'bout' variable'''
    while bout <2: #validate that this is the first round, and if it is, run the code below
        choice = input('Would you like to play rock, paper, scissors? y/n: ').lower() #assigns the player's choice, 'yes' or 'no', to variable 'choice'
        while not choice in ('y','n'): #input validation
            choice = input("invalid entry. Please type 'y' or 'n': ").lower()
        return choice,bout # return the player's choice and the round
    choice = input('\nWould you like to play again? y/n: ').lower() #if this is the second round or greater, assign the players choice, 'yes' or 'no', to variable 'choice' and run the code below
    while not choice in ('y','n'): # input validation
        choice = input("invalid entry. Please type 'y' or 'n': ").lower()
    return choice,bout #return the player's choice and the round
    
def obtain_choice(pwins,cwins):
    '''this function takes the user's choice, and performs input validation on it. Once the input validation check is done, it passes the user's choice back to main()'''
    print(f'Player score: {pwins}\nComputer score: {cwins}') #display the number of times the player has won, and the number of times the computer has won
    player_choice = input('Please type rock, paper or scissors: ').lower() #take the user input and assign it to variable 'player_choice'
    while not player_choice in ('rock','paper','scissors'): #input validation
        player_choice = input("invalid entry. Please type \'rock\', \'paper\' or \'scissors\': ").lower()
    print(f'\nYour choice was: {player_choice}') #display the player's choice
    return player_choice #return the value of the variable 'player_choice' to the 'main()' function
    
def tieFunc(pwins,cwins):
    '''this function is called if the round ends in a tie'''
    print('it\'s a tie...boring!')
    return pwins,cwins
    
def winFunc(pwins,cwins):
    '''this function is called if the round ends with the player winning. Their 'win count' tracker (pwins) is updated and returned to main()'''
    print('you win!')
    pwins += 1
    return pwins,cwins
    
def loseFunc(pwins,cwins):
    '''this function is called if the round ends with the computer winning. The computer's 'win count' tracker (cwins) is updated and returned to main()'''
    print('you lose')
    cwins += 1
    return pwins,cwins
    
def main(round,pwins,cwins): #main function, where the majority of the action takes place
    choice_dict = {'rock': 0, 'paper': 1,'scissors': 2} #assigns a numeric value to each possible valid choice
    choice_tuple = ('rock','paper','scissors') #a list of choices in a tuple for the computer player to select
    control,round = play_control(round) #this function asks the user if they would like to play and records the results
    while control =='y': #if the player selects 'y' to a round, then this while loop is activated
        round += 1
        print(f"\nRound {round}")
        human_index = choice_dict.get(obtain_choice(pwins,cwins)) #takes the player choice, uses it to obtain a numeric value from the 'choice_dict', and places that numeric value in the 'human_index' variable
        computer_choice = random.choice(choice_tuple) #runs the 'choice' function from the 'random' module and uses it to grab a random value from the 'choice_tuple' tuple, and assign that to the 'computer_choice' vars
        print(f'The computer chose: {computer_choice}') 
        computer_index = choice_dict.get(computer_choice) #uses the 'computer_choice' variable to retrieve a numeric value from the 'choice_dict' dictionary
        win_lose_tie_matrix = [[0,2,1],[1,0,2],[2,1,0]] #initializes the 'win', 'lose', 'tie' matrix
        result_index = win_lose_tie_matrix[human_index][computer_index] #calculates who wins. The value of 'human_index' selects the sub-list, the value of 'computer_index' selects the value within the sublist. The result is then plugged into the 'result_index' variable
        result_dict = {0:tieFunc,1:winFunc,2:loseFunc} # initializes the 'result_dict'; if a key of '0' is given, 'tieFunc' is returned. If a key of '1' is given, 'winFunc' is returned and so on
        pwins,cwins = result_dict[result_index](pwins,cwins) #calls the 'result_dict' and gives it the value of 'result_dict', along with arguments to hand to any of the three possible functions
        control,round = play_control(round) #this calls the 'play_control' func to determine if the user wishes to play again, and the 'round' argument helps track the number of rounds played
    print(f'\nThanks for playing! \n\nFinal scores -\nYour score: {pwins}\nComputer score: {cwins}\nAfter {round} rounds') #if the user selects 'n' in the 'play_control' function, this line is ran
    
main(round,player_score,computer_score) #kicks off the start of the code

    