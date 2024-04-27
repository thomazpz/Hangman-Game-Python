#Importing class from Hangman file
from Hangman import *

#Menu main class
class Main:
    while(True):
        game_mode = input("\033[94mSelect the game mode: \n\033[90m1 - Solo\033[0m \n\033[92m2 - Duo\033[0m\n\033[91m0 - Exit\n\033[0m").strip()
        if game_mode == "1":
            Hangman.solo()
        elif game_mode == "2":
            Hangman.duo()
        elif game_mode == "0":
            print("Exiting the game, thanks for playing! :) ")
            break
        else:
            print("\033[91mError, type only 1, 2 or 0 to select\033[0m")


