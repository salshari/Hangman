# include necessary libraries
import random
import pygame

# initialize the Pygame modules
pygame.init()

# set the width and height of the Pygame window (in pixels)
width = 500
height = 500

# initialize the Pygame window to specified dimensions
# this screen is where the Hangman figure will be drawn if the Pygame option is chosen by user as display
screen = pygame.display.set_mode((width, height))

# use RGB values to define colors 
black = (0, 0, 0)
white = (255, 255, 255)

class WordBank:
    '''
    this class represents a list of words that could be given to the user to guess
    parent class used for extensibility of game
    '''
    def __init__(self):
        self.words = []

    # returns a randomly chosen word from the list of words 
    def get_word(self):
        return random.choice(self.words)

class FruitWordBank(WordBank):
    '''
    inherits from parent class WordBank, represnts a word bank for fruits
    '''
    def __init__(self):
        # calls constructor of the parent class
        super().__init__()

        # a list of fruits
        self.words = ["apple", "banana", "orange", "grape", "pineapple", "mango", "blueberry", "cherry", "watermelon"]

class HolidayWordBank(WordBank):
    '''
    inherits from parent class WordBank, represnts a word bank for holidays
    '''
    def __init__(self):
        # calls constructor of the parent class
        super().__init__()

        # a list of holidays
        self.words = ["Christmas", "Thanksgiving", "Valentines", "Easter", "Halloween"]

class AnimalWordBank(WordBank):
    '''
    inherits from parent class WordBank, represnts a word bank for animals
    '''
    def __init__(self):
        # calls constructor of the parent class
        super().__init__()

        # a list of holidays
        self.words = ['sebra', 'elephant', 'cat', 'dog', 'mouse', 'giraffe', 'lion', 'cheetah', 
                      'alligator', 'snake', 'dolphin', 'rhino', 'penguin']

def draw_gallow_in_pygame():
    '''
    draw the gallow from which the Hangman will be hung in the pygame window
    '''
    # draw the bottom horizontal bar
    pygame.draw.line(screen, black, (50, 350), (350, 350), 5)
    # draw the vertical line for the pole
    pygame.draw.line(screen, black, (200, 350), (200, 50), 5)
    # draw a small horizontal line at the top of the vertical line
    pygame.draw.line(screen, black, (200, 50), (250, 50), 5)
    # draw a small vertical bar attached to the top of the head and to the small horizontal line
    pygame.draw.line(screen, black, (250, 50), (250, 80), 5)

    # update the Pygame window
    pygame.display.update()

def draw_hangman_pygame(stage):
    '''
    determines which parts of the Hangman figure will be 
    drawn to the Pygame window using the current stage
    '''

    # set the background color of the Pygame window
    screen.fill(white)
    
    # after screen has been filled white, call the following function to draw the gallow in the pygame window
    draw_gallow_in_pygame()

    # set up the stages that the Hangman figure will be drawn in to the Pygame window
    
    # if stage greater than or equal to 1, draw the head of the Hangman figure
    if stage >= 1:
        pygame.draw.circle(screen, black, (250, 100), 20)

    # if stage greater than or equal to 2, draw the body of the Hangman figure
    if stage >= 2:
        pygame.draw.line(screen, black, (250, 120), (250, 200), 5)

    # if stage greater than or equal to 3, draw the left arm of the Hangman figure
    if stage >= 3:
        pygame.draw.line(screen, black, (250, 140), (200, 170), 5)

    # if stage greater than or equal to 4, draw the right arm of the Hangman figure
    if stage >= 4:
        pygame.draw.line(screen, black, (250, 140), (300, 170), 5)

    # if stage greater than or equal to 5, draw the left leg of the Hangman figure
    if stage >= 5:
        pygame.draw.line(screen, black, (250, 200), (200, 250), 5)

    # if stage greater than or equal to 6, draw the right leg of the Hangman figure
    if stage >= 6:
        pygame.draw.line(screen, black, (250, 200), (300, 250), 5)

        # if the user has used this sixth/last attempt, a "you lost" messsage will print to the pygame window
        font = pygame.font.Font(None, 56)
        text = font.render("You lost!", True, black)
        text_rect = text.get_rect(center=(width // 2, height - 50))
        screen.blit(text, text_rect)

    # update the Pygame window
    pygame.display.flip()

def draw_hangman_text(stage):
    '''
    determines which parts of the Hangman figure will be 
    drawn to the terminal with a text based interface
    using the current stage
    '''

    # set up the stages that the Hangman figure will be drawn in to the terminal
    stages = [
        # stage 0 is the Hangman figure when no incorrect guesses have been made
            """
            _______
            |     |
            |    
            |    
            |    
            |    
            |__|___
            """,
        # stage 1 is the Hangman figure when 1 incorrect guess has been made and the head is drawn
            """
            _______
            |     |
            |     O
            |    
            |    
            |    
            |__|___
            """,
        # stage 2 is the Hangman figure when 2 incorrect guesses have been made and the body is drawn
            """
            _______
            |     |
            |     O
            |     |
            |    
            |    
            |__|___
            """,
        # stage 3 is the Hangman figure when 3 incorrect guesses have been made and the left arm is drawn
            """
            _______
            |     |
            |     O
            |    /|
            |    
            |    
            |__|___
            """,
        # stage 4 is the Hangman figure when 4 incorrect guesses have been made and the right arm is drawn
            """
            _______
            |     |
            |     O
            |    /|\\
            |    
            |    
            |__|___
            """,
        # stage 5 is the Hangman figure when 5 incorrect guesses have been made and the left leg is drawn
            """
            _______
            |     |
            |     O
            |    /|\\
            |    / 
            |    
            |__|___
            """,
        # stage 6 is the Hangman figure when 6 incorrect guesses have been made and the right leg is drawn
            """
            _______
            |     |
            |     O
            |    /|\\
            |    / \\
            |    
            |__|___
            """
        ]
    
      # track the amount of incorrect guesses 
    incorrect_guesses = len([letter for letter in self.guessed_letters if letter not in self.chosen_word])
    
    # if incorrect guesses is less than number of attempts
    if incorrect_guesses < len(stages):
        # print the corresponding stage of the Hangman figure
        print(stages[incorrect_guesses])

def draw_hangman(stage, using_pygame=True):
    '''
    this function chooses between the Pygame interface or the text-based interface
    '''
    # if using_pygame is True, the Hangman figure will be drawn using Pygame
    if using_pygame:
        draw_hangman_pygame(stage)

    # if using_pygame is False, the Hangman figure will be drawn using a text-based interface
    else:
        draw_hangman_text(stage)

class HangmanGame:
    '''
    this class manages the state of the game and tracks which letters have been guessed 
    as well as tracks the state of our Hangman figure
    '''

    def __init__(self, word):
        self.chosen_word = word.lower()
        self.guessed_letters = set()
        self.max_attempts = 6

    # same stages as defined in draw_hangman_text function
    stages = [
            """
            _______
            |     |
            |    
            |    
            |    
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |    
            |    
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |     |
            |    
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |    /|
            |    
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |    /|\\
            |    
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |    /|\\
            |    / 
            |    
            |__|___
            """,
            """
            _______
            |     |
            |     O
            |    /|\\
            |    / \\
            |    
            |__|___
            """
        ]
    
    def display_word_to_guess(self):
        '''
        displays the current state of the word that the user is attempting to guess
        '''
        displayed_word = ""
        for letter in self.chosen_word:
            if letter in self.guessed_letters:
                displayed_word += letter + " "
            else:
                displayed_word += "_ "
        return displayed_word
    
    def guess_letter(self, letter):
        '''
        checks the letter guessed by the user
        adds this letter to the list of letters guessed
        handles repeat guesses by printing an error message to the terminal
        makes sure the guess is not a number
        '''
        letter = letter.lower()

        # Check if the input is a valid letter
        if not letter.isalpha() or len(letter) != 1:
            print("Invalid input! Please enter a letter or adjust your guess to 1 letter")
            return
        
        if letter in self.guessed_letters:
            print("That letter has already been guessed! Try again!")
            return
        
        self.guessed_letters.add(letter)

    def check_win(self):
        '''
        this function checks if all the letters in the word being guessed have been guessed
        '''
        return all(letter in self.guessed_letters for letter in self.chosen_word)
    
    def check_lose(self):
        '''
        this function checks to see if the user has used all their attempts and therefore, lost the game
        '''
        incorrect_guesses = len([letter for letter in self.guessed_letters if letter not in self.chosen_word])
        return incorrect_guesses >= self.max_attempts
    
    def is_game_over(self):
        '''
        this function determines if the game is over
        the game is over if the user has won or if the user has lost
        '''
        return self.check_lose() or self.check_win()
    
    def draw_hangman_text(self):
        '''
        this function draws the Hangman figure in stages using a text-based interface 
        the figure is drawn based on the number of incorrect guesses the user has guessed
        '''
        incorrect_guesses = len([letter for letter in self.guessed_letters if letter not in self.chosen_word])
        if incorrect_guesses < len(self.stages):
            print(self.stages[incorrect_guesses])
    
    def draw_hangman(self, use_pygame=True):
        '''
        this function chooses between the Pygame interface or the text-based interface
        '''
        stage_index = len([letter for letter in self.guessed_letters if letter not in self.chosen_word])
        if stage_index < len(self.stages):
            if use_pygame: 
                draw_hangman_pygame(stage_index)
            else: 
                self.draw_hangman_text()

def select_word_bank():
    '''
    this function allows the user to pick which word bank they would like to use to pick their word to be guessed
    '''

    print("Choose a word bank:")
    print("1. Fruits")
    print("2. Holidays")
    print("3. Animals")
    user_choice = input("Enter your choice (1, 2, or 3): ")

    # if the user enters 1, their chosen word bank is the FruitWordBank
    if user_choice == "1":
        return FruitWordBank()
    # if the user enters 2, their chosen word bank is the HolidayWordBank
    elif user_choice == "2":
        return HolidayWordBank()
    # if the user enters 3, their chosen word bank is the AnimalWordBank
    elif user_choice == "3":
        return AnimalWordBank()
    # if the user enters an invalid choice, their chosen word bank defaults to option 1, the FruitWordBank
    else:
        print("Invalid choice. Defaulting to option 1, Fruits.")
        return FruitWordBank()

def play_hangman(word_bank):
    '''
    handles gamplay for the Hangman game using the wordbank and drawing method chosen by the user
    '''

    # ask the user how they would like the game to be displayed
    print("Choose how to display the game:")
    print("1. Pygame")
    print("2. Text")

    drawing_choice = input("Enter your choice (1 or 2): ")

    # if drawing_choice is 1, the pygame interface will be used
    use_pygame = (drawing_choice == "1")

    # choose a random word from the word bank chosen by the user 
    chosen_word = word_bank.get_word()

    game = HangmanGame(chosen_word)

    # as long as the game is not over, keep displaying the word, updating the word, asking for a letter, and taking a letter from user
    while not game.is_game_over():
        print("\nWord:", game.display_word_to_guess())
        game.draw_hangman(use_pygame)
        guess = input("Enter a letter: ")
        game.guess_letter(guess)

    # if the user has won, display a congratulations message
    if game.check_win():
        print("Congratulations! You guessed the word:", game.chosen_word)
    # if the user did not win and they're playing in the pygame window, display a message alerting them of their loss
    if not game.check_win() and use_pygame == True:
            game.draw_hangman(use_pygame)
            '''print("""
            _______
            |     |
            |     O
            |    /|\\
            |    / \\
            |    
            |__|___
            """)
        '''
            pygame.draw.line(screen, black, (200, 200), (250, 250), 5)
            print("Sorry, you ran out of attempts and have lost. The word was:", game.chosen_word)
    # if the user did not win and they're playing in the terminal, display a message alerting them of their loss
    if not game.check_win() and use_pygame == False:
        print("""
            _______
            |     |
            |     O
            |    /|\\
            |    / \\
            |    
            |__|___
            """)
        print("Sorry, you ran out of attempts and have lost. The word was:", game.chosen_word)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # If the window close button is clicked, stop the game loop
                running = False

    pygame.quit() 

# set the game into motion
chosen_word_bank = select_word_bank()
play_hangman(chosen_word_bank)