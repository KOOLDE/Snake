from pygame.image import load
from pygame import Surface
from pygame.transform import scale


class Information:
    def __init__(
        self, screen, path, width, height, x_position, y_position, set_scale
    ) -> None:
        self.image = load(path).convert_alpha()
        self.surface = Surface((width, height)).convert_alpha()
        self.surface.blit(self.image, (0, 0), (0, 0, width, height))
        self.surface = scale(self.surface, (width * set_scale, height * set_scale))
        self.surface.set_colorkey((0, 0, 0))
        self.x_position = x_position - ((width * set_scale) / 2)
        self.y_position = y_position - ((height * set_scale) / 2)
        self.screen = screen

    def render(self) -> None:
        self.screen.blit(self.surface, (self.x_position, self.y_position))
