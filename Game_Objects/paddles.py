import pygame


class Paddles:
    """All functions of paddles"""

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def move_paddle_up(self):
        self.y += -10
        #return self.y

    def move_paddle_down(self):
        self.y += 0.25
        return self.y

    def no_move(self):
        self.y += 0
        return self.y

    def check_borders(self):
        if self.y <= 0:
            self.y = 0
        elif self.y >= 458:
            self.y = 458
        return self.y

        # if paddle_1.y <= 0:
        #     paddle_1.y = 0
        # elif paddle_1.y >= 458:
        #     paddle_1.y = 458

    def move_up(self):
        new_y = self.y - 10
        return new_y
