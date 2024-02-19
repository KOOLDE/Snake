from pygame import QUIT
from pygame.display import set_mode, set_caption, flip
from pygame.event import get
from pygame.key import get_pressed
from pygame import K_w, K_s, K_a, K_d, K_q
from random import randrange
from os import getcwd
from sys import exit

from .snake import Snake
from .apple import Apple
from .text import Text
from .information import Information
from .menu import Menu


class Game:
    def __init__(self, title, width, height) -> None:
        set_caption(title)
        self.screen = set_mode((width, height))
        self.fps = 8
        self.frame_delay = int(1000 / self.fps)

        self.apple = Apple(
            self.screen, (231, 76, 60), randrange(0, 780, 20), randrange(0, 580, 20)
        )
        self.snake = Snake(
            self.screen, (46, 204, 113), randrange(0, 780, 20), randrange(0, 580, 20)
        )
        self.score = Text(self.screen, 40, 40)

        self.project_path = getcwd()
        self.prees_path = self.project_path + "\\assets\\press.png"
        self.directions_path = self.project_path + "\\assets\\directions.png"

        self.press = Information(self.screen, self.prees_path, 160, 32, 400, 280, 1)
        self.directions = Information(
            self.screen, self.directions_path, 128, 32, 400, 312, 1
        )

        self.menu = Menu(self.screen)

        self.display_image = True
        self.running = True

    def handleEvents(self) -> None:
        for event in get():
            if event.type == QUIT:
                exit()

        keys = get_pressed()
        if keys[K_a]:
            if self.snake.x_direction != 20:
                self.snake.x_direction = -20
                self.snake.y_direction = 0
            self.display_image = False
        if keys[K_d]:
            if self.snake.x_direction != -20:
                self.snake.x_direction = 20
                self.snake.y_direction = 0
            self.display_image = False
        if keys[K_w]:
            if self.snake.y_direction != 20:
                self.snake.y_direction = -20
                self.snake.x_direction = 0
            self.display_image = False
        if keys[K_s]:
            if self.snake.y_direction != -20:
                self.snake.y_direction = 20
                self.snake.x_direction = 0
            self.display_image = False

        if keys[K_q]:
            self.running = False
            self.menu.running = True

    def update(self) -> None:
        self.snake.update(self.apple.food)
        self.apple.update(self.snake.head)
        self.score.update(f"APPLE : {(self.snake.index * -1) - 1}")

        # To increase the speed of snake
        match (self.snake.index * -1) - 1:
            case 10:
                self.frame_delay = int(1000 / 10)
            case 20:
                self.frame_delay = int(1000 / 12)
            case 30:
                self.frame_delay = int(1000 / 14)
            case 40:
                self.frame_delay = int(1000 / 16)
            case 50:
                self.frame_delay = int(1000 / 18)
            case 60:
                self.frame_delay = int(1000 / 20)
            case 70:
                self.frame_delay = int(1000 / 22)
            case 80:
                self.frame_delay = int(1000 / 24)
            case 80:
                self.frame_delay = int(1000 / 26)
            case 100:
                self.running = False
                self.menu.running = True

        # Exit when snake collide on itself
        if self.snake.collide:
            self.running = False
            self.menu.running = True

    def render(self) -> None:
        self.screen.fill((22, 23, 25))
        self.apple.render()
        self.snake.render()
        self.score.render()
        if self.display_image:
            self.press.render()
            self.directions.render()
        flip()
