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

    # update the Pygame window
    pygame.display.flip()