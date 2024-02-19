from pygame.sysfont import SysFont
from pygame.font import Font


class Text:
    def __init__(self, screen, x_position, y_position) -> None:
        self.sys_font = SysFont("Consolas", 16)
        self.x_position = x_position
        self.y_position = y_position
        self.screen = screen

    def update(self, txt):
        # To update the number of food eated by snake
        self.text = Font.render(
            self.sys_font, txt, True, (240, 243, 244)
        )

    def render(self):
        # To draw the text in screen
        self.screen.blit(self.text, (self.x_position, self.y_position))
