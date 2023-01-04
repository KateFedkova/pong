import pygame


class MainScreen:
    """Class for setting a mode"""

    pygame.init()  # Initialize the pygame

    screen = pygame.display.set_mode((800, 533))  # Create the screen

    background = pygame.image.load('images/background.png')  # Background image

    pygame.display.set_caption("Pong")  # Title
