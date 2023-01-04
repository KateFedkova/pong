import random
from main_screen import MainScreen
from paddles import Paddles
from ball import Ball

main_screen = MainScreen()
paddle_1 = Paddles('images/paddle.png', 4, 100)
paddle_2 = Paddles('images/paddle.png', 782, 300)
ball = Ball('images/ball.png', random.randint(300, 600), random.randint(300, 400))