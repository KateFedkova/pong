import pygame


class Paddles:
    """All functions of paddles"""

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.velocity = 0

    def move_paddle_up(self):
        self.velocity = -1

    def move_paddle_down(self):
        self.velocity = 1

    def no_move(self):
        self.velocity = 0

    def check_borders(self):
        if self.y <= 0:
            self.y = 0
        elif self.y >= 458:
            self.y = 458
        return self.y + self.velocity

    def collision_paddle(self, ball_given):
        paddle = self.image.get_rect(topleft=(self.x, self.y))
        ball = ball_given.image.get_rect(topleft=(ball_given.x, ball_given.y))
        if paddle.colliderect(ball):
            return True
        return False
