import random

player_move = input('Choose [r]ock , [p]aper or [s]cissors:').lower()

your_move = ''

if player_move == 'r':
    your_move = 'rock'
elif player_move == 'p':
    your_move = 'paper'
elif player_move == 's':
    your_move = 'scissors'
else:
    raise SystemExit('Invalid Input. Try again...')
print(f'You chose {your_move}.')

computer_random_move = random.randint(1, 3)
computer_move = ''
if computer_random_move == 1:
    computer_move = 'rock'
elif computer_random_move == 2:
    computer_move = 'paper'
else:
    computer_move = 'scissors'
print(f'The computer chose {computer_move}.')

condition = ''
if your_move == 'rock':
    if computer_move == 'scissors':
        condition = 'You win!'
    elif computer_move == 'paper':
        condition = 'You lost!'
    else:
        condition = 'Draw!'

elif your_move == 'paper':
    if computer_move == 'scissors':
        condition = 'You lost!'
    elif computer_move == 'paper':
        condition = 'Draw!'
    else:
        condition = 'You win!'

else:
    if computer_move == 'scissors':
        condition = 'Draw!'
    elif computer_move == 'paper':
        condition = 'You win!'
    else:
        condition = 'You lost!'

print(condition)