import string
from words import choose_word
from images import IMAGES

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: return True kare agar saare letters jo ki user ne guess kiye hai wo secret_word mai hai, warna no
      False otherwise
    '''
    if secret_word == get_guessed_word(secret_word, letters_guessed):
        return True
    return False

# Iss function ko test karne ke liye aap get_guessed_word("kindness", [k, n, d]) call kar sakte hai
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: string, hame ye return karna hai ki kaun kaun se letters aapne nahi guess kare abhi tak
    eg agar letters_guessed = ['e', 'a'] hai to humme baki charecters return karne hai
    jo ki `bcdfghijklmnopqrstuvwxyz' ye hoga
    '''
   #def pattern(number):
    all_letters = string.ascii_lowercase
    letters_left = " "
    for letters in all_letters: 
        if letters not in letters_guessed:
            letters_left += letters
    return letters_left
def invalid_guess(guess):
    if len(guess) != 1 :
        return False
    if not guess.isalpha():
        return False
    return True
def get_hint(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess karna hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek character jo abhi tak guess nahi hua hai
    '''

    import random
    letters_not_guessed = []
    
    index = 0
    while (index < len(secret_word)):
        letter = secret_word[index]
        if letter not in letters_guessed:
            if letter not in letters_not_guessed:
                letters_not_guessed.append(letter)

        index += 1

    return random.choice(letters_not_guessed)
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Hangman game yeh start karta hai:
    * Game ki shuruaat mei hi, user ko bata dete hai ki
      secret_word mei kitne letters hai
    * Har round mei user se ek letter guess karne ko bolte hai
    * Har guess ke baad user ko feedback do ki woh guess uss
      word mei hai ya nahi
    * Har round ke baar, user ko uska guess kiya hua partial word
      display karo, aur underscore use kar kar woh letters bhi dikhao
      jo user ne abhi tak guess nahi kiye hai
    '''
    print("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    difficulty_level = input("Which level you want to choose?\na\teasy\nb\tmedium\nc\thard\n")
    total_lives = turns = 8
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]

    if difficulty_level not in ["a", "b", "c"]:
        print ("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")

    else:
        if difficulty_level == "b":
            total_lives = turns = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]

        elif difficulty_level == "c":
            total_lives = turns = 4
            images_selection_list_indices = [1, 3, 5, 7]
    letters_guessed = []

    
    turns = 8
    from images import IMAGES
    while turns > 0:
        available_letters = get_available_letters(letters_guessed)
        print ("Available letters: " +str(available_letters))

        guess = input("Please guess a letter: ")
        if guess == "hint":
            letter = get_hint(secret_word, letters_guessed)
        else:
            letter = guess.lower()
            if not invalid_guess(letter):
                continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print ("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print ("")

            if is_word_guessed(secret_word, letters_guessed) == True:
                print (" * * Congratulations, you won! * * ")
                print ("")

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print (IMAGES[total_lives-turns])
            print ("Remaining Lives : ", turns)
            print ("")
            letters_guessed.append(letter)
            turns-=1
    
# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
