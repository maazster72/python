"""
This program is an updated game of hangman that randomly chooses a word
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
    guesses_left = 10 - count
    print("")
    print("Current answer: " + ans)
    print("Letters already guessed: "+guesses)
    if(guesses_left == 0):
        print("Last guess!")
    else:
        print("Guesses left: "+str(guesses_left))


words = [
    "aadvark",
    "beetlejuice",
    "castle",
    "merlin",
    "vikings"
]

def get_all_words():
    with open('/Users/maazahmed/GitRepos/python/hangman/EnglishWords.txt') as file:
        words = [line.rstrip() for line in file]
        file.close()
    return(words)

def choose_level():
    levels = ["1","2","3","4"]
    level = input("Choose a level (1 Hard|2 Medium|3 Easy|4 Choose own word length): ")
    while(level not in levels):
        level = input("Please input the corresponding level number: ")
    return level

def level_one_words():
    words = []
    for word in get_all_words():
        if (len(word) < 6):
            words.append(word)
    return words

def level_two_words():
    words = []
    for word in get_all_words():
        if (len(word) > 5 and len(word) < 10):
            words.append(word)
    return words

def level_three_words():
    words = []
    for word in get_all_words():
        if (len(word) > 9):
            words.append(word)
    return words

def custom_word_len(length):
    words =[]
    for word in get_all_words():
        if(len(word) == length):
            words.append(word)
    return words

def choose_word(words):
    return(words[random.randint(0,len(words)-1)])
    

def get_level_word(level):
    if (level == "3"):
        word = choose_word(level_three_words())
    elif(level == "2"):
        word = choose_word(level_two_words())
    elif(level == "1"):
        word = choose_word(level_one_words())
    else:
        length = input("Please enter a word length you would like to guess: ")
        while((length < 1) and type(int(length)) != int):
            length = int(input("Please enter an integer: "))
        word = custom_word_len(length)
    return word

def main(level):
    word = get_level_word(level)
    ans_list = generate_start_answer(word)
    ans = get_answer(ans_list)
    guesses_list = []
    count = 0
    while(count < 11 and is_won(ans, word) == False):
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
        print("Damn, you lost...the word was " + word)

def start_game():
    print("Welcome to Hangman!")
    level = choose_level()
    return level

def play_again():
    b = input("Would you like to play again?(y/n) ")
    b = b.upper()
    if(b == 'Y'):
        return True
    else:
        return False

def hangman():
    in_play = True
    while(in_play):
        level = start_game()
        main(level)
        in_play = play_again()
    print("Goodbye!")

hangman()