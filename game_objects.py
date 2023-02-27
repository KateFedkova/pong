import random
from Menu import MainScreen
from Game_Classes import Paddles, Ball
from scores import Scores
from Rules import RulesScreen
from countdown import Countdown

main_screen = MainScreen()
rule = RulesScreen(main_screen)
paddle_1 = Paddles('images/paddle.png', 2, 100)
paddle_2 = Paddles('images/paddle.png', 782, 300)

score = Scores()
ball = Ball('images/ball.png', random.randint(500, 600), random.randint(100, 200), score)
countdown = Countdown()
