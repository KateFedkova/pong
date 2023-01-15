import pygame


class Rules:

    """All functions for creating the page with rules"""

    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.font = 'Georgia'
        self.default_color = 'pink'
        self.b_color = (232, 164, 71)
        self.text_size = 25
        self.text_bold = False

    def create_rect_with_text(self, text, button):
        pygame.draw.rect(self.main_screen.screen, self.b_color, button)
        self.main_screen.write_text(self.text_size, self.text_bold, text, button.x + 5, button.y + 5)
