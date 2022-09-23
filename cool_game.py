import random

computer_guessed_number = random.randint(1, 100)
continue_game = True


while(continue_game):
    user_guess = int(input("guess a number from 1 to 100: "))

    if user_guess == computer_guessed_number:
        print('You win!')
        continue_game = False
    elif user_guess < computer_guessed_number:
        print('You Lose!')
    elif user_guess > computer_guessed_number:
        print('Too much!')
    else:
        print('There was an error')

print('Game over!')
