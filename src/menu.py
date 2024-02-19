from pygame import QUIT
from pygame.display import flip
from pygame.event import get
from pygame.key import get_pressed
from pygame import K_RETURN

from .text import Text


class Menu:
    def __init__(self, screen) -> None:
        self.screen = screen

        self.score = Text(self.screen, 300, 200)
        self.press_a = Text(self.screen, 300, 220)
        self.press_d = Text(self.screen, 300, 240)
        self.press_w = Text(self.screen, 300, 260)
        self.press_s = Text(self.screen, 300, 280)
        self.press_enter = Text(self.screen, 270, 330)
        self.press_q = Text(self.screen, 270, 350)

        self.display_image = True
        self.running = True

    def handleEvents(self):
        for event in get():
            if event.type == QUIT:
                exit()

        keys = get_pressed()
        if keys[K_RETURN]:
            self.running = False

    def update(self) -> None:
        self.press_a.update("Press A to go left")
        self.press_d.update("Press D to go right")
        self.press_w.update("Press W to go up")
        self.press_s.update("Press S to go down")
        self.press_enter.update("Press Enter to start game")
        self.press_q.update("Press Q to return for menu")

    def render(self) -> None:
        self.screen.fill((22, 23, 25))
        self.press_a.render()
        self.press_d.render()
        self.press_w.render()
        self.press_s.render()
        self.press_enter.render()
        self.press_q.render()
        flip()
