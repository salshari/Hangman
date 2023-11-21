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