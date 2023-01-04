from objects_for_game import main_screen
import pygame


def rules_scene():
    font = pygame.font.SysFont('Georgia', 25, bold=False)
    surf_rule_1 = font.render('1. Игра продолжается до 11 пропущенных одним игроком', True, 'white')
    surf_rule_2 = font.render('2. Из игры можно выйти в любой момент', True, 'white')
    surf_to_game = font.render('Вернуться на главное меню', True, 'white')
    button_rule_1 = pygame.Rect(80, 150, 682, 50)
    button_rule_2 = pygame.Rect(150, 230, 500, 50)
    button_to_game = pygame.Rect(240, 360, 330, 50)

    running = True

    while running:

        main_screen.screen.fill((155, 183, 47))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_to_game.collidepoint(event.pos):
                    running = False
                    return True

        x, y = pygame.mouse.get_pos()

        if button_to_game.x <= x <= button_to_game.x + 330 and button_to_game.y <= y <= button_to_game.y + 50:
            pygame.draw.rect(main_screen.screen, (86, 183, 47), button_to_game)
        else:
            pygame.draw.rect(main_screen.screen, (232, 164, 71), button_to_game)

        pygame.draw.rect(main_screen.screen, (232, 164, 71), button_rule_1)
        main_screen.screen.blit(surf_rule_1, (button_rule_1.x + 5, button_rule_1.y + 5))

        pygame.draw.rect(main_screen.screen, (232, 164, 71), button_rule_2)
        main_screen.screen.blit(surf_rule_2, (button_rule_2.x + 5, button_rule_2.y + 5))

        main_screen.screen.blit(surf_to_game, (button_to_game.x + 5, button_to_game.y + 5))

        pygame.display.update()
