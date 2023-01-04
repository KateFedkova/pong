import pygame


class Ball:
    """All functions of paddles"""

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
