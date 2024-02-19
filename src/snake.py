from pygame import Rect
from pygame.draw import rect


class Snake:
    def __init__(self, screen, color, x_position, y_position) -> None:
        self.screen = screen
        self.color = color
        self.x_position = x_position
        self.y_position = y_position
        self.x_direction = 0
        self.y_direction = 0
        self.head = Rect(self.x_position, self.y_position, 20, 20)
        self.positions = [[self.head.x, self.head.y]]
        self.index = -1
        self.collide = False

    def update(self, food) -> None:
        # Make snake run continuously
        self.head.x += self.x_direction
        self.head.y += self.y_direction

        # Grow snake body when eat the food
        self.positions.append([self.head.x, self.head.y])
        self.positions = self.positions[self.index :]

        # Increase the score when eat the food
        if self.head.colliderect(food):
            self.index -= 1

        # Make snake to appear in other side of screen
        if self.head.x >= 800:
            self.head.x = -20
        elif self.head.x <= -20:
            self.head.x = 800
        elif self.head.y >= 600:
            self.head.y = -20
        elif self.head.y <= -20:
            self.head.y = 600

        # Detect when head touch the body
        for coordinate in self.positions[:-4]:
            if self.positions[-1] == coordinate:
                self.collide = True

    def render(self) -> None:
        # To draw the snake body
        for coordinate in self.positions:
            rect(self.screen, self.color, Rect(coordinate[0], coordinate[1], 20, 20))
