import random
from hangman_arts import stages, logo
from hangman_words import word_list
from os import system, name
from replit import clear


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


chosen_word = random.choice(word_list).lower()

#Testing code and transforming the word in a list
print(chosen_word)
chosen_list = []
for letter in chosen_word:
    chosen_list.append(letter)

# initializing a variable life = nr of stages
lives = 6

# display "_" instead of chosen word letter and logo
print(logo)
display = []
for letter in chosen_word:
    display.append("_")
print(display)


game_on = True
while game_on:

    guess = input("Guess a letter: ").lower()
    clear()

    # Check guessed letter
    for position in range(len(chosen_word)):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f'You have {lives} lives left!')

    if "_" not in display:
        end_of_game = True
        print('You won!')
        game_on = False

    if lives == 0:
        print('You lost! Game over!')
        game_on = False


