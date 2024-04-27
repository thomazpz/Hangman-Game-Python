#importing libraries
from random import choice
from os import system, name
from time import sleep

class Hangman:
    #file get method
    @staticmethod
    def words_file(file_name):
        with open(file_name, "r") as arquivo:
            words = [line.strip() for line in arquivo]
        return words
    #drawings creation
    @staticmethod
    def drawings(n):
        if n == 0:
            print('''
  +---+
  |   |
      |
      |
      |
      |
=========''')  
        
        elif n == 1:
            print('''\033[94m
  +---+
  |   |
  O   |
      |
      |
      |
=========\033[0m''')
            
        elif n == 2:
                                print('''\033[34m
  +---+
  |   |
  O   |
  |   |
      |
      |
=========\033[0m''')
                                
        elif n == 3:
            print('''\033[93m
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========\033[0m''')
            
        elif n == 4:
            print('''\033[31m
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========\033[0m''')
            
        elif n == 5:
            print('''\033[91m
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========\033[0m''')
        elif n == 6:
            
            print('''\033[90m
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========\033[0m''')
        elif n == 7:
            print('''\033[93m             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""""""`
                Victory\033[0m''')
        elif n == 8:
             print("""\033[91m
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[0m""")

            
    #solo mode
    @staticmethod
    def solo():
        animals = Hangman.words_file("animals.txt")
        objects = Hangman.words_file("objects.txt")
        errors = 0
        guessed_letters = []
        choose_word_type = choice([animals, objects])
        word_tip = "animal" if choose_word_type == animals else "objeto" 
        chose_word = choice(choose_word_type)
        hidden_word = ["_" for letters in chose_word]

        print("Gamemode mode selected: Solo")
        print(f"Welcome to the solo mode, the tip is: {word_tip}.")
        print(hidden_word)
        Hangman.drawings(0)

        while(True):
            print(f"Guessed letters: {guessed_letters}")
            print(hidden_word)
            guess = input("Which letter do you want to guess?: ").lower().strip()
            if guess in guessed_letters:
                print("\033[91mYou already used this letter!\033[0m")
                continue
            if len(guess) == 1 and guess.isalpha():
                if guess in chose_word:
                    system('cls' if name == 'nt' else 'clear')
                    print(f"\033[93mYou guessed the letter {guess} right\033[0m")
                    index = 0
                    for letter in chose_word:
                        if letter == guess:
                            hidden_word[index] = guess
                        index += 1
                elif guess not in chose_word:
                    system('cls' if name == 'nt' else 'clear')
                    print(f"\033[91mYou got the letter {guess} wrong!\033[0m")
                    errors += 1
                
                #chamando drawings
                if errors == 0:
                    Hangman.drawings(0)
                elif errors == 1:
                    Hangman.drawings(1)
                elif errors == 2:
                    Hangman.drawings(2)
                elif errors == 3:
                    Hangman.drawings(3)
                elif errors == 4:
                    Hangman.drawings(4)
                elif errors == 5:
                    Hangman.drawings(5)
                elif errors == 6:
                    system('cls' if name == 'nt' else 'clear')
                    Hangman.drawings(6)
                    print(f"\033[91mYou used all your chances, better luck next time! :(\033[0m")
                    print(f"A palavra era {chose_word}")
                    Hangman.drawings(8)
                    break
            #retorno de erro caso o usuario nao digite uma letter
            else:
                print("\033[91mType only letters!\033[0m")
                continue
            if guess not in guessed_letters:
                guessed_letters.append(guess)

            #verificacao se o usuario ganhou
            if "_" not in hidden_word:
                Hangman.drawings(7)
                print(hidden_word)
                break

    #duo mode
    def duo():
        print("Game mode selected: Duo")
        errors = 0 
        guessed_letters = []
        chose_word = input("Type the word that your partner will guess: ")
        word_tip = input("Give a tip to your partner: ")
        print("The game will start soon, get ready!") 
        for i in range(5, 0, -1):
            print(f"Starting in {i} seconds...")
            sleep(1)
            system('cls' if name == 'nt' else 'clear')
            hidden_word = ["_" for letters in chose_word]
            print(f"Now its time to guess! The tip for the word is: {word_tip}.")
            Hangman.drawings(0)

        while True:
            print(f"Guessed letters: {guessed_letters}")
            print(hidden_word)
            guess = input("Which letter do you want to guess?: ").lower().strip()
            if guess in guessed_letters:
                print("\033[91mYou already guessed this letter!\033[0m")
                continue
            if len(guess) == 1 and guess.isalpha():
                if guess in chose_word:
                    system('cls' if name == 'nt' else 'clear')
                    print(f"\033[93mYou got the letter {guess} right!\033[0m")
                    index = 0
                    for letter in chose_word:
                        if letter == guess:
                            hidden_word[index] = guess
                        index += 1
                elif guess not in chose_word:
                    system('cls' if name == 'nt' else 'clear')
                    print(f"\033[91mYou got the letter {guess} wrong!\033[0m")
                    errors += 1
                
                #calling out drawings
                if errors == 0:
                    Hangman.drawings(0)
                elif errors == 1:
                    Hangman.drawings(1)
                elif errors == 2:
                    Hangman.drawings(2)
                elif errors == 3:
                    Hangman.drawings(3)
                elif errors == 4:
                    Hangman.drawings(4)
                elif errors == 5:
                    Hangman.drawings(5)
                elif errors == 6:
                    system('cls' if name == 'nt' else 'clear')
                    Hangman.drawings(6)
                    print(f"\033[91mYou used all your chances, better luck next time! :( \033[0m")
                    Hangman.drawings(8)
                    break

            if guess not in guessed_letters:
                guessed_letters.append(guess)

            #verification to see if the user typed a letter.
            else:
                print("\033[91mType a letter!\033[0m")
                continue

            #verification to see if the user has won.
            if "_" not in hidden_word:
                Hangman.drawings(7)
                print(hidden_word)
                break
                


