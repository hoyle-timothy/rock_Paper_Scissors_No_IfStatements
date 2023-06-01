import random
round = 1
player_score = 0
computer_score = 0

def play_control(bout):
    '''this function has two jobs; 1st job, ask the user if they'd like to play and perform input validation on their response. 
    2nd job, after the user has already played a round, ask them if they'd like to play again and perform input validation on their response again.
    The number of rounds played is tracked with the 'bout' variable'''
    while bout <2:
        choice = input('Would you like to play rock, paper, scissors? y/n: ').lower()
        while not choice in ('y','n'):
            choice = input("invalid entry. Please type 'y' or 'n': ").lower()
        return choice,bout
    choice = input('\nWould you like to play again? y/n: ').lower() 
    while not choice in ('y','n'):
        choice = input("invalid entry. Please type 'y' or 'n': ").lower()
    return choice,bout
    
def obtain_choice(pwins,cwins):
    '''this function takes the user's choice, and performs input validation on it. Once the input validation check is done, it passes the user's choice back to main()'''
    print(f'Player score: {pwins}\nComputer score: {cwins}')
    player_choice = input('Please type rock, paper or scissors: ').lower()
    while not player_choice in ('rock','paper','scissors'):
        player_choice = input("invalid entry. Please type \'rock\', \'paper\' or \'scissors\': ").lower()
    print(f'\nYour choice was: {player_choice}')
    return player_choice
    
def tieFunc(pwins,cwins):
    print('it\'s a tie...boring!')
    return pwins,cwins
    #pass
    
def winFunc(pwins,cwins):
    print('you win!')
    pwins += 1
    #print(pwins)
    return pwins,cwins
    #pass
    
def loseFunc(pwins,cwins):
    print('you lose')
    cwins += 1
    return pwins,cwins
    #pass
    
def main(round,pwins,cwins):
    choice_dict = {'rock': 0, 'paper': 1,'scissors': 2} #assigns a numeric value to each possible valid choice
    choice_tuple = ('rock','paper','scissors')
    control,round = play_control(round)
    while control =='y':
        print(f"\nRound {round}")
        human_index = choice_dict.get(obtain_choice(pwins,cwins))
        computer_choice = random.choice(choice_tuple)
        print(f'The computer chose: {computer_choice}')
        computer_index = choice_dict.get(computer_choice)
        win_lose_tie_matrix = [[0,2,1],[1,0,2],[2,1,0]]
        result_index = win_lose_tie_matrix[human_index][computer_index]
        result_dict = {0:tieFunc,1:winFunc,2:loseFunc}
        pwins,cwins = result_dict[result_index](pwins,cwins)
        round += 1
        control,round = play_control(round)
    round -= 1
    print(f'\nThanks for playing! \n\nFinal scores:\nYour score: {pwins}\nComputer score: {cwins}\nAfter {round} rounds')   
    
main(round,player_score,computer_score)

    