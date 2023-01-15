import pygame
from Game_Objects.objects_for_game import rule


def rules_scene():
    button_to_game = rule.main_screen.draw_rect(240, 360, 330, 50)
    running = True

    while running:
        rule.main_screen.screen.fill((155, 183, 47))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return running
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_to_game.collidepoint(event.pos):
                    running = False
                    return True

        x, y = pygame.mouse.get_pos()

        rule.main_screen.create_button(rule.text_size, rule.text_bold, 'Вернуться на главное меню', button_to_game, x, y, (86, 183, 47), rule.b_color)

        rule.create_rect_with_text('1. Игра продолжается до 11 пропущенных одним игроком', rule.main_screen.draw_rect(80, 150, 682, 50))
        rule.create_rect_with_text('2. Из игры можно выйти в любой момент', rule.main_screen.draw_rect(150, 230, 500, 50))

        pygame.display.update()
