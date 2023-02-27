import pygame
from game_objects import rule


def rules_scene():
    button_to_game = rule.main_screen.draw_rect(220, 360, 385, 50)
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

        rule.main_screen.create_button(rule.text_size, rule.text_bold, 'Повернутися до головного меню', button_to_game, x, y, (86, 183, 47), rule.b_color)

        rule.create_rect_with_text('1. Гра триває до 11 пропущених одним гравцем', rule.main_screen.draw_rect(130, 150, 560, 50))
        rule.create_rect_with_text('3. З гри можна вийти будь-якої миті', rule.main_screen.draw_rect(190, 230, 435, 50))

        pygame.display.update()
