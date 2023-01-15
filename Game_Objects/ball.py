import pygame
import math


class Ball:
    """All functions of the ball"""

    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y

    def move_ball(self):
        new_x = self.x - 0.02
        new_y = self.y - 0.02
        #self.x += 0.02
        #self.y += -0.02
        # self.x += random.randint(0, 1)
        # self.y += random.randint(0, 1)
        return new_x, new_y

    # def check_borders(self):
        # if self.x <= 0:
        #     self.x = 0
        # elif self.x >= 760:
        #     self.x = 760
        # if self.y <= 0:
        #     self.y = 0
        # elif self.y >= 490:
        #     self.y = 490
        #
        # if self.x <= 760 and self.y >= 490:
        #     self.x += -0.02
        #     self.y += 0.02
        # return self.x, self.y

    def check_borders(self, new_x, new_y):

        # upper border
        if new_x < self.x and new_y < self.y <= 0:
            self.x = new_x + 0.2
            self.y = new_y + 0.2

        elif new_x > self.x and new_y < self.y <= 0:
            self.x = new_x - 0.2
            self.y = new_y + 0.2

        # left border
        elif new_x < self.x <= 0 and new_y > self.y:
            self.x = new_x + 0.2
            self.y = new_y + 0.2

        elif new_x < self.x <= 0 and new_y < self.y:
            self.x = new_x + 0.2
            self.y = new_y - 0.2

        # bottom border
        elif new_x > self.x and new_y > self.y and new_y >= 490:
            self.x = new_x + 0.2
            self.y = new_y - 0.2

        elif new_x < self.x and new_y > self.y and new_y >= 490:
            self.x = new_x - 0.2
            self.y = new_y - 0.2

        else:
            self.x = new_x
            self.y = new_y

        return self.x, self.y



        # elif self.x >= 760:
        #     self.x = 760
        # if self.y <= 0:
        #     self.y = 0
        # elif self.y >= 490:
        #     self.y = 490
        #
        # if self.x <= 760 and self.y >= 490:
        #     self.x += -0.02
        #     self.y += 0.02
        # return self.x, self.y

        # if self.x <= 0 and self.y :
        #     return
        #     or self.x >= 800:
        #     return
        # if self.y <= 0 or self.y >= 450:
        #     return False
        # else:
        #     return True

    def collision_paddle2(self, paddlex, paddley):
        distance = math.sqrt(math.pow(self.x - paddlex, 2) + (math.pow(self.y - paddley, 2)))
        if distance < 45:
            return True
        else:
            return False

    def collision_paddle1(self, paddlex, paddley):
        distance = math.sqrt(math.pow(self.x - paddlex, 2) + (math.pow(self.y - paddley, 2)))
        if distance < 45:
            return True
        else:
            return False

    def check_coordinates(self, new_x, new_y, paddle2_x, paddle2_y, paddle1_x, paddle1_y):
        #if self.collision_paddle2(paddle2_x, paddle2_y):
        #     if new_x > self.x and new_y < self.y:
        #         print('2 yes')
        #         self.x = new_x
        #         self.y = new_y
        #     elif new_x > self.x and new_y < self.y:
        #         print('2 collide')
        #         self.x = new_x
        #         self.y = new_y
        # elif self.collision_paddle1(paddle1_x, paddle1_y):
        #     if new_x < self.x and new_y > self.y:
        #         print('1 yes')
        #         self.x = new_x
        #         self.y = new_y
        #     elif new_x < self.x and new_y < self.y:
        #         print('1 collide')
        #         self.x = new_x
        #         self.y = new_y
        # else:
        #     self.x = new_x
        #     self.y = new_y
        # return self.x, self.y

        if new_x > self.x and new_y < self.y:
            if self.collision_paddle2(paddle2_x, paddle2_y):
                #print('2 yes')
                self.x = new_x - 0.2
                self.y = new_y - 0.2
            else:
                self.x = new_x
                self.y = new_y
        elif new_x > self.x and new_y < self.y:
            if self.collision_paddle2(paddle2_x, paddle2_y):
                #print('2 collide')
                self.x = new_x - 0.2
                self.y = new_y + 0.2
            else:
                self.x = new_x
                self.y = new_y

        elif new_x < self.x and new_y > self.y:
            if self.collision_paddle1(paddle1_x, paddle1_y):
                #print('1 yes')
                self.x = new_x + 0.2
                self.y = new_y + 0.2
            else:
                self.x = new_x
                self.y = new_y
        elif new_x < self.x and new_y < self.y:
            if self.collision_paddle1(paddle1_x, paddle1_y):
                #print('1 collide')
                self.x = new_x - 0.2
                self.y = new_y - 0.2
            else:
                self.x = new_x
                self.y = new_y
        else:
            self.x = new_x
            self.y = new_y

        return self.x, self.y
