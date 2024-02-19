from pygame import Rect
from pygame.draw import rect
from random import randrange


class Apple:
    def __init__(self, screen, color, x_position, y_position) -> None:
        self.screen = screen
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.food = Rect(self.x_position, self.y_position, 20, 20)

    def update(self, snake_head) -> None:
        # To vanish the food when the snake eat it 
        # and to appear the food in other coordnate of screen
        if snake_head.colliderect(self.food):
            self.food.x = randrange(0, 780, 20)
            self.food.y = randrange(0, 580, 20)

    def render(self) -> None:
        # To draw the apple 
        rect(self.screen, self.color, self.food)
