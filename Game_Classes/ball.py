import pygame


class Ball:
    """All functions of the ball"""

    def __init__(self, image, x, y, score):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.velocity_x = 1
        self.velocity_y = 1
        self.score = score

    def move_ball(self):
        new_x = self.x + self.velocity_x
        new_y = self.y + self.velocity_y
        return new_x, new_y

    def check_borders(self, new_x, new_y):

        # upper border
        if new_x < self.x and new_y <= 0 < self.y:
            self.velocity_x = -1
            self.velocity_y = 1

        elif new_x > self.x and new_y <= 0 < self.y:
            self.velocity_x = 1
            self.velocity_y = 1

        # left border
        elif new_x < self.x <= 0 and new_y > self.y:
            self.velocity_x = 1
            self.velocity_y = 1
            self.score.update_score_2()

        elif new_x < self.x <= 0 and new_y < self.y:
            self.velocity_x = 1
            self.velocity_y = -1
            self.score.update_score_2()

        # bottom border
        elif new_x > self.x and new_y > self.y and new_y >= 490:
            self.velocity_x = 1
            self.velocity_y = -1

        elif new_x < self.x and new_y > self.y and new_y >= 490:
            self.velocity_x = -1
            self.velocity_y = -1

        # right border
        elif new_x > self.x and new_y < self.y and new_x >= 760:
            self.velocity_x = -1
            self.velocity_y = -1
            self.score.update_score_1()

        elif new_x > self.x and new_y > self.y and new_x >= 760:
            self.velocity_x = -1
            self.velocity_y = 1
            self.score.update_score_1()

    def check_coords(self, ball, new_x, new_y, paddle1, paddle2):
        if new_x > self.x and new_y < self.y and paddle2.collision_paddle(ball):
            self.velocity_x = -1
            self.velocity_y = -1

        elif new_x > self.x and new_y > self.y and paddle2.collision_paddle(ball):
            self.velocity_x = -1
            self.velocity_y = 1

        elif new_x < self.x and new_y > self.y and paddle1.collision_paddle(ball):
            self.velocity_x = 1
            self.velocity_y = 1

        elif new_x < self.x and new_y < self.y and paddle1.collision_paddle(ball):
            self.velocity_x = 1
            self.velocity_y = -1
