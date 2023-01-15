# pygame.time.delay() - pause the program for an amount of time
import pygame
from Rules.rules_scene import rules_scene
from start_game import start_game
from Game_Objects.objects_for_game import main_screen, paddle_1, paddle_2, ball


# Game Loop

running = True

button_rules = main_screen.draw_rect(330, 310, 170, 50)
button_start = main_screen.draw_rect(340, 230, 140, 50)

while running:

    main_screen.screen.blit(main_screen.background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rules.collidepoint(event.pos):
                running = rules_scene()
            if button_start.collidepoint(event.pos):
                running = start_game()

    main_screen.screen.blit(paddle_1.image, (paddle_1.x, paddle_1.y))
    main_screen.screen.blit(paddle_2.image, (paddle_2.x, paddle_2.y))
    main_screen.screen.blit(ball.image, (ball.x, ball.y))

    x, y = pygame.mouse.get_pos()

    main_screen.change_button_color(button_rules, x, y)
    main_screen.change_button_color(button_start, x, y)

    main_screen.write_text(33, True, 'Pong Game', 315, 80)
    main_screen.write_text(30, False, 'Игра на двоих', 311, 150)

    main_screen.write_text(33, True, 'Правила', button_rules.x + 5, button_rules.y + 5)
    main_screen.write_text(33, True, 'Начать',  button_start.x + 5, button_start.y + 5)

    pygame.display.update()
