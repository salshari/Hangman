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