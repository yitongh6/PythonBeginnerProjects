import random

def RockPaperScissors():
    retry = 'y'
    scores = [0, 0]  # first is user, second is computer
    while retry == 'y':
        user_input = input('Rock (r). Paper (p), Scissor (s)?! ')
        combo = [('Rock (r)', 'r'), ('Paper (p)', 'p'), ('Scissors (s)', 's')]
        computer_num = random.randint(0, 2)
        computer_input_show = combo[computer_num][0]
        computer_input = combo[computer_num][1]
        print(f'Computer: {computer_input_show}!')
        winning_conditions = [('r', 'p'), ('p', 's'), ('s', 'r')]
        computer_inputw = winning_conditions[computer_num][1]
        if computer_input == computer_inputw:
            print('Computer won!')
            scores[1] += 1
        elif computer_input == user_input:
            print('Tied!')
        else:
            print('You won!')
            scores[0] += 1
        print(f'Your score vs computer is {scores[0]}:{scores[1]}.')
        retry = input('\nDo you want to try again? (y/n) ')
    print(f'\nYour final score vs computer is {scores[0]}:{scores[1]}.')
