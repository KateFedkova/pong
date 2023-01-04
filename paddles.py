import pygame


class Paddles:
    """All functions of paddles"""

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def move_paddle_up(self):
        self.y += -0.1
        return self.y
        #screen.blit(self.image, (self.x, self.y))

    def move_paddle_down(self):
        self.y += 0.1
        return self.y
        #screen.blit(self.image, (self.x, self.y))

    def no_move(self):
        self.y += 0
        return self.y
        # screen.blit(self.image, (self.x, self.y))

    def check_height(self):
        if self.y <= 0 or self.y >= 533:
            return False
        else:
            return True
