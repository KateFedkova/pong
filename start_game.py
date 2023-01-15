from Game_Objects.objects_for_game import main_screen, paddle_1, paddle_2, ball
import pygame

# Game Loop


def start_game():

    running = True
    paddle_2_change = 0
    paddle_1_change = 0
    font = pygame.font.SysFont('Georgia', 25, bold=False)
    new_paddle_2_y = 0

    while running:

        main_screen.screen.blit(main_screen.background, (0, 0))

        #pygame.time.get_ticks()

        # for i in range(5):
        #     main_screen.screen.blit(font.render(f"{i}", True, 'red'), (300, 300))
        #     time.sleep(1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    #paddle_2.y = paddle_2.move_paddle_up()
                    #paddle_2.move_paddle_up()
                    paddle_2_change = -0.25
                    #new_paddle_2_y = paddle_2.move_up()

                elif event.key == pygame.K_DOWN:
                    #paddle_2.y = paddle_2.move_paddle_down()
                    # if paddle_2.check_height():
                    paddle_2_change = 0.25

                elif event.key == pygame.K_w:
                    paddle_1_change = -0.25

                elif event.key == pygame.K_s:
                    paddle_1_change = 0.25

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #paddle_2.y = paddle_2.no_move()
                    paddle_2_change = 0

                if event.key == pygame.K_w or event.key == pygame.K_s:
                    # paddle_2.y = paddle_2.no_move()
                    paddle_1_change = 0

        paddle_2.y += paddle_2_change
        paddle_1.y += paddle_1_change
        #paddle_2.y = new_paddle_2_y

        paddle_1.y = paddle_1.check_borders()
        paddle_2.y = paddle_2.check_borders()

        # if paddle_2.y <= 0:
        #      paddle_2.y = 0
        # elif paddle_2.y >= 458:
        #      paddle_2.y = 458
        #
        # if paddle_1.y <= 0:
        #     paddle_1.y = 0
        # elif paddle_1.y >= 458:
        #     paddle_1.y = 458

        ball_new_x, ball_new_y = ball.move_ball()
        #ball.x, ball.y = ball.check_coordinates(ball_new_x, ball_new_y, paddle_2.x, paddle_2.y, paddle_1.x, paddle_1.y)

        # if ball_new_x > ball.x:
        #     print('check')
        #     ball.x = ball_new_x
        #     print('here')
        # elif ball_new_x < ball.x:
        #     print('yes')

        ball.x, ball.y = ball.check_borders(ball_new_x, ball_new_y)

        # if ball.collision_paddle2(paddle_2.x, paddle_2.y):
        #     ball.x += -0.25
        #     ball.y += -0.25




        main_screen.screen.blit(ball.image, (ball.x, ball.y))
        main_screen.screen.blit(paddle_2.image, (paddle_2.x, paddle_2.y))
        main_screen.screen.blit(paddle_1.image, (paddle_1.x, paddle_1.y))
        pygame.display.update()


# paddle 2 can't move with function only using change?
# more speed for paddle?
# move function should be changed in order to move ball near borders correctly
