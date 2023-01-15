import random
from Menu.main_screen import MainScreen
from Game_Objects.paddles import Paddles
from Game_Objects.ball import Ball
from Rules.rules import Rules

main_screen = MainScreen()
#main_screen.write_text(30, False, 'Pong Game', 315, 80)
paddle_1 = Paddles('images/paddle.png', 4, 100)
paddle_2 = Paddles('images/paddle.png', 782, 300)
ball = Ball('images/ball.png', random.randint(500, 600), random.randint(200, 300))
rule = Rules(main_screen)
