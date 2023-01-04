# pygame.time.delay() - pause the program for an amount of time
from objects_for_game import main_screen, paddle_1, paddle_2, ball
from rules_scene import rules_scene
from start_game import start_game
import pygame


font = pygame.font.SysFont('Georgia', 33, bold=True)
surf_rules = font.render('Правила', True, 'white')
button_rules = pygame.Rect(330, 310, 170, 50)

surf_start = font.render('Начать', True, 'white')
button_start = pygame.Rect(340, 230, 140, 50)

font_2 = pygame.font.SysFont('Georgia', 30, bold=False)
surf_game = font.render('Pong Game', True, 'white')
surf_expl = font_2.render('Игра на двоих', True, 'white')


# Game Loop

running = True

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

    if button_rules.x <= x <= button_rules.x + 170 and button_rules.y <= y <= button_rules.y + 50:
        pygame.draw.rect(main_screen.screen, (232, 164, 71), button_rules)
    else:
        pygame.draw.rect(main_screen.screen, 'pink', button_rules)

    if button_start.x <= x <= button_start.x + 140 and button_start.y <= y <= button_start.y + 50:
        pygame.draw.rect(main_screen.screen, (232, 164, 71), button_start)
    else:
        pygame.draw.rect(main_screen.screen, 'pink', button_start)

    main_screen.screen.blit(surf_rules, (button_rules.x + 5, button_rules.y + 5))
    main_screen.screen.blit(surf_start, (button_start.x + 5, button_start.y + 5))
    main_screen.screen.blit(surf_game, (315, 80))
    main_screen.screen.blit(surf_expl, (311, 150))

    pygame.display.update()

# rules_scene  - change colour
