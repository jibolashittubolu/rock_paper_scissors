import random

game_options = ['R', 'P', 'S', 'NIL']   
def runGame():
    while True:
        print('R for rock, P for paper, S for scissors')
        # print(' ')
        user_turn = str(input('Pick your option among R or P or S: '))

        

        if user_turn not in (game_options):
            print (' ')
            print('Invalid input, please enter a valid input')
            continue

        if user_turn in (game_options):
            computer_turn = random.choice(game_options)
            turns = [user_turn, computer_turn]
            text = "Player {} : CPU {} "
            print(text.format(user_turn, computer_turn))

            if user_turn == computer_turn:
                print('Game Tie, start again')
                continue

            if 'R' in turns and 'S' in turns:
                index = turns.index('R')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            if 'P' in turns and 'R' in turns:
                index = turns.index('P')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            if 'S' in turns and 'P' in turns:
                index = turns.index('S')
                if index == 0:
                    print('Player wins')
                if index == 1:
                    print ('Computer wins')
                break

            else:
                print('An unexpected error occurred, restarting program')
                continue

runGame()
