# HangmanComputing
# This application is a Hangman Game coded using VSCode (Python)

# The dependencies of this application are that the user must have Python to run this 
# application and have the Pygame library downloaded. 

# IMPORTANT Notes about Running the Game and the Pygame Window: 
# Once you run the game, the pygame window will pop up in the middle of your computer. It is 
# recomended that before you start the game, the user minimize the tab that they are running 
# the code in or move it to either side of the computer so that when the Pygame window pops up, 
# it can be seen. 
# Do not click directly on or try to move the Pygame window as this will result in the Pygame 
# window not updating. All you will see is a black screen which is why it is important to set 
# up the tab where you are running the code as described above. 
# No matter which interface the user has chosen, once the game is over (you have won or you 
# have lost), you need to X out of the Pygame window. This will stop the program and allow 
# the user to be able to run the program again. If the Pygame window is not X'd out of,
# hitting the run button will not restart the game until the X button of the Pygame
# window is clicked. You must X out of the Pygame Window after the game has concluded. 

# Important Notes about Guesses:
# Guesses must be one singular letter. 
# Numbers, multiple letters, and symbols will not be accpetable inputs and an error message 
# will be displayed (this will not count against the user's attempts)
# If you are playing and think you know the word (say you have "b l _ e b e r r _ " and you 
# know the word is "blueberry"), you cannot type "blueberry" into the terminal because of the
# rules described above. You must type in your letter guesses of "u" and "y" separately. 

# Gameplay:
# First, the user will be asked to pick a wordbank. A number correlating to a specific 
# wordbank must be typed in. If an invalid input is enetered, the default wordbank is fruit.
# Then, the user will be asked to choose an interface. A number correlating to a specific 
# interface must be typed in. If an invalid input is enetered, the default interface is text.
# Users can see the hidden word and revealed letters of this word in the terminal regardless
# of chosen interface. 
# User has 6 attempts and if the user guesses an incorrect letter, they have lost an attempt 
# and the Hangman figure in the chosen interface is updated. 
