from objects_for_game import main_screen, paddle_1, paddle_2, ball
import pygame


# Game Loop

def start_game():

    running = True
    paddle_2_change = 0

    while running:

        main_screen.screen.blit(main_screen.background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #paddle_2.y = paddle_2.move_paddle_up()
                    # if paddle_2.check_height():
                    paddle_2_change = -0.25
                    # else:
                    #     paddle_2.y = 0

                if event.key == pygame.K_DOWN:
                    #paddle_2.y = paddle_2.move_paddle_down()
                    # if paddle_2.check_height():
                    paddle_2_change = 0.25
                    # else:
                    #     paddle_2.y = 533

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #paddle_2.y = paddle_2.no_move()
                    paddle_2_change = 0

        paddle_2.y += paddle_2_change
        if paddle_2.y <= 0:
            paddle_2.y = 0
        elif paddle_2.y >= 458:
            paddle_2.y = 458

        main_screen.screen.blit(paddle_1.image, (paddle_1.x, paddle_1.y))
        main_screen.screen.blit(paddle_2.image, (paddle_2.x, paddle_2.y))
        main_screen.screen.blit(ball.image, (ball.x, ball.y))



        pygame.display.update()

# paddle 2 can't move with function only using change?
# границы не работают