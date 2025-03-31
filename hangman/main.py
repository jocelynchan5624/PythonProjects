import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.


print(logo)

answer = random.choice(word_list)
print(answer)
word_to_guess = ''
for letter in range(0, len(answer)):
    word_to_guess += '_'
print(f'Ready? Here is your word to guess:\n{word_to_guess}')

# print(answer)



num_of_lives = 6
num_of_right_guess = 0
correct_guess = []
while num_of_right_guess < len(set(answer)) and num_of_lives > 0:
    print(f'*****************{num_of_lives}/6 Lives Left*****************')
    guess = input("Guess a letter:")
    num_of_wrong_answer = 0
    word_guessed = ''
    for char in answer:
        # print(letter)
        if char in correct_guess:
            # print(correct_guess)
            word_guessed += char
            # num_of_right_guess += -1
            # print(num_of_right_guess)
        elif char == guess and not char in correct_guess:
            # print(char)
            word_guessed += guess
            correct_guess.append(guess)
            num_of_right_guess += 1
        else:
            num_of_wrong_answer += 1
            word_guessed += '_'
    print(f'Word to guess: {word_guessed}')
    # print(num_of_wrong_answer)
    if guess not in correct_guess:
        num_of_lives += -1
        # print(num_of_wrong_guess)
        if num_of_lives > 0:
            print("You lose a life!")
        else:
            print(f"The answer is {answer}, you lose!")
    else:
        # num_of_right_guess += 1
        if num_of_right_guess == len(set(answer)):
            print("You won!")
        else:
            print("Right Guess")
    print(num_of_right_guess)
    print(num_of_lives)
    print(stages[num_of_lives])
