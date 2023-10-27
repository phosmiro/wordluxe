import random
import wordbank
from nltk.corpus import words
from termcolor import colored

dictionary = set(words.words())
wordbank_cat = {
    "general": wordbank.gen_difficulty,
    "countries": wordbank.countries_difficulty,
    "animals": wordbank.animals_difficulty,
    "fruits": wordbank.fruits_difficulty,
    "sports": wordbank.sports_difficulty,
    "artists": wordbank.artists_difficulty,
    "songs": wordbank.songs_difficulty
}

def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input. Please try again.")

def calculate_reward(attempt, max_attempts):
    if attempt <= 2:
        return 3
    elif attempt <= max_attempts - 2:
        return 2
    else:
        return 1

def play_game(word, category, max_attempts):
    currency = 0
    attempt = 1
    msg = ""

    while attempt <= max_attempts:
        print(f"Attempt #{attempt}")
        guess = input()

        if guess.lower() not in dictionary:
            if category not in ["general", "fruits", "animals"]:
                break
            print(f"'{guess}' is not in the English dictionary.")
            guess = input()

        if len(guess) != len(word):
            print(f"Guess should be {len(word)} letters.")
            continue

        print(check_guess(guess, word))

        if guess == word:
            msg = "You won!"
            currency += calculate_reward(attempt, max_attempts)
            break
        elif guess != word and attempt == max_attempts:
            msg = "Game over."
            print(f"The word was: {word}")
            break
        
        attempt += 1

    if max_attempts != float("inf"):
        print(f"Coins: {currency}")
    print(msg)

def check_guess(guess, word):
    length = len(word)
    output = ["-"] * length

    for i in range(length):
        if guess[i] == word[i]:
            output[i] = colored(guess[i], 'green')
            word = word.replace(guess[i], "-", 1)

    for i in range(length):
        if guess[i] in word and output[i] == "-":
            output[i] = colored(guess[i], 'yellow')
        elif guess[i] in output[i]:
            continue
        else:
            output[i] = colored(guess[i], 'dark_grey')

    return ''.join(output)

def easy_mode(word, category):
    play_game(word, category, max_attempts = float("inf"))
    print("Coins: No coins are rewarded in easy mode")

def normal_mode(word, category):
    play_game(word, category, max_attempts = 6)

def hard_mode(word, category):
    play_game(word, category, max_attempts = 4)

def extreme_mode(word, category):
    play_game(word, category, max_attempts = 3)

def main():
    cat_input = validate_input("Choose category: ", wordbank.categories)
    dif_input = validate_input("Choose difficulty: ", wordbank.gen_difficulty)

    word = random.choice(wordbank_cat[cat_input][dif_input])

    game_modes = {
        "easy": easy_mode,
        "normal": normal_mode,
        "hard": hard_mode,
        "extreme": extreme_mode
    }
    game_modes[dif_input](word, cat_input)

main()
