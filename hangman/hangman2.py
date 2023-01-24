"""
This program plays a game of hangman
"""
import random

def generate_start_answer(word):
    ans_list = list(word)
    for i in range(len(ans_list)):
        ans_list[i] = " _ "
    return ans_list

def get_answer(ans_list):
    ans = ""
    for char in ans_list:
        ans += char
    return ans

def get_guess():
    valid_chars = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    guess = input("Guess a letter: ")
    while((len(guess) != 1) or guess.upper() not in valid_chars):
        guess = input("Guess a valid letter:")
    return guess

def check_guess_in_word(guess_char, word):
    guess_char = guess_char.upper()
    word = word.upper()
    for char in word:
        if (char == guess_char):
            return True
    return False

def check_if_prev_guessed(guess_char, guesses):
    if guess_char in guesses:
        return True
    else:
        return False

def add_char_to_answer(guess_char, word, ans_list):
    for i in range(len(word)):
        if(guess_char == word[i]):
            ans_list[i] = guess_char
    return ans_list

def is_won(ans, word):
    if (ans == word):
        return True
    else:
        return False

def get_guesses(guesses_list):
    guesses = ""
    for char in guesses_list:
        guesses += " "+char
    return guesses

def display_current_game(ans, count, guesses_list):
    guesses = get_guesses(guesses_list)
    guesses_left = 11 - count
    print("")
    print("Current answer: " + ans)
    print("Letters already guessed: "+guesses)
    if(guesses_left == 0):
        print("Last guess!")
    else:
        print("Guesses left: "+str(guesses_left))
    
def main(word):
    ans_list = generate_start_answer(word)
    ans = get_answer(ans_list)
    guesses_list = []
    count = 0
    while(count < 12 and is_won(ans, word) == False):
        display_current_game(get_answer(ans_list), count, guesses_list)
        guess_char = get_guess()
        if(check_if_prev_guessed(guess_char, guesses_list)):
            print("You already guessed " + guess_char)
            continue
        else:
            guesses_list.append(guess_char)
            if(check_guess_in_word(guess_char, word)):
                ans_list = add_char_to_answer(guess_char, word, ans_list)
                ans = get_answer(ans_list)
            else:
                print("WRONG!")
                count += 1
    
    if(is_won(ans, word)):
        print("YOU WIN! The word was " + word)
    else:
        print("Damn, you lost...the word " + word)

words = [
    "aadvark",
    "beetlejuice",
    "castle",
    "merlin",
    "vikings"
]

def choose_word():
    file = open()

word = choose_word(words)
main(word)
