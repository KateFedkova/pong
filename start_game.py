import pygame
from game_objects import main_screen, paddle_1, paddle_2, ball, score, countdown

# Game Loop


def start_game():

    running = True
    start = countdown.start
    counter = countdown.counter
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    while running:

        main_screen.screen.blit(main_screen.background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.USEREVENT:
                counter -= 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle_2.move_paddle_up()

                elif event.key == pygame.K_DOWN:
                    paddle_2.move_paddle_down()

                elif event.key == pygame.K_w:
                    paddle_1.move_paddle_up()

                elif event.key == pygame.K_s:
                    paddle_1.move_paddle_down()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    paddle_2.no_move()

                if event.key == pygame.K_w or event.key == pygame.K_s:
                    paddle_1.no_move()

        if start:

            paddle_1.y = paddle_1.check_borders()
            paddle_2.y = paddle_2.check_borders()

            ball_new_x, ball_new_y = ball.move_ball()

            ball.check_borders(ball_new_x, ball_new_y)
            ball.check_coords(ball, ball_new_x, ball_new_y, paddle_1, paddle_2)

            ball.x = ball_new_x
            ball.y = ball_new_y

        text_x, text_y = countdown.show_num(counter)

        if not start:
            main_screen.write_text(countdown.size, countdown.bold, countdown.text, text_x, text_y)
            if counter < 0:
                start = True

        main_screen.screen.blit(ball.image, (ball.x, ball.y))
        main_screen.screen.blit(paddle_2.image, (paddle_2.x, paddle_2.y))
        main_screen.screen.blit(paddle_1.image, (paddle_1.x, paddle_1.y))
        main_screen.write_text(25, True, f"Гравець 1: {score.score_1}", 20, 15)
        main_screen.write_text(25, True, f"Гравець 2: {score.score_2}", 620, 15)
        player = score.game_over()

        if player:
            main_screen.write_text(50, False, f"Виграв гравець {player}!", 200, 230)
            pygame.display.update()
            pygame.time.wait(2000)
            running = False

        pygame.display.update()
