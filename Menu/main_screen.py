import pygame


class MainScreen:

    """Class for setting a mode"""

    def __init__(self):
        pygame.init()  # Initialize the pygame
        self.width = 800
        self.height = 533
        self.screen = pygame.display.set_mode((self.width, self.height))  # Create the screen
        self.background = pygame.image.load('images/background.png')  # Background image
        self.title = pygame.display.set_caption("Pong")  # Title
        self.font = 'Georgia'  # maybe change
        self.default_color = 'pink'
        self.b_color = (232, 164, 71)

    def change_button_color(self, button, mouse_x, mouse_y, b_color=False, d_color=False):
        if not b_color and not d_color:
            b_color = self.b_color
            d_color = self.default_color
        if button.x <= mouse_x <= button.x + button.width and button.y <= mouse_y <= button.y + button.height:
            pygame.draw.rect(self.screen, b_color, button)
        else:
            pygame.draw.rect(self.screen, d_color, button)

    def write_text(self, size, bold, text, x, y):
        font = pygame.font.SysFont(self.font, size, bold=bold)
        rule = font.render(text, True, 'white')
        self.screen.blit(rule, (x, y))

    def draw_rect(self, left, top, width, height):
        button = pygame.Rect(left, top, width, height)
        return button

    def create_button(self, size, bold, text, button, x, y, b_color, d_color):
        self.change_button_color(button, x, y, b_color, d_color)
        self.write_text(size, bold, text, button.x, button.y)

