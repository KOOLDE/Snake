import sys
import pygame

from random import randrange

pygame.init()

def draw_snake_rect(x: int, y: int, size: int, screen):
    global snake_position_and_size
    
    snake_color: tuple(int) = (8, 217, 214)
    snake_position_and_size = pygame.Rect(x, y, size, size)
    pygame.draw.rect(screen, snake_color, snake_position_and_size, border_radius=2)

def draw_fruit_rect(x: int, y: int, size: int, screen):
    global fruit_position_and_size

    fruit_color: tuple(int) = (255, 46, 99)
    fruit_position_and_size = pygame.Rect(x, y, size, size)
    pygame.draw.rect(screen, fruit_color, fruit_position_and_size, border_radius=8)

def growth_snake(positions: list, index: int, rect: int, screen):
    for position in positions[index:]:
        draw_snake_rect(position[0], position[1], rect, screen)

def main():
    pygame.display.set_caption("Snake")

    window_width: int = 480
    window_height: int = 480
    window_background: tuple = (37, 42, 52)

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((window_width, window_height))

    rect_size: int = 20
    snake_index: int = -1
    get_all_snake_position: list[int] = list()

    snake_vector: int = 20
    snake_add_pixel: list[int] = [0, 0]
    snake_default_x: int = randrange((window_width - window_width), window_width, rect_size)
    snake_default_y: int = randrange((window_height - window_height), window_height, rect_size)

    fruit_default_x: int = randrange((window_width - window_width), window_width, rect_size)
    fruit_default_y: int = randrange((window_height - window_height), window_height, rect_size)

    while True:
        clock.tick(8)

        snake_default_x += snake_add_pixel[0]
        snake_default_y += snake_add_pixel[1]

        get_all_snake_position.append([snake_default_x, snake_default_y])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if snake_add_pixel[0] != -20:
                        snake_add_pixel[0] = snake_vector
                        snake_add_pixel[1] = 0
                if event.key == pygame.K_LEFT:
                    if snake_add_pixel[0] != 20:
                        snake_add_pixel[0] = -snake_vector
                        snake_add_pixel[1] = 0
                if event.key == pygame.K_DOWN:
                    if snake_add_pixel[1] != -20:
                        snake_add_pixel[0] = 0
                        snake_add_pixel[1] = snake_vector
                if event.key == pygame.K_UP:
                    if snake_add_pixel[1] != 20:
                        snake_add_pixel[0] = 0
                        snake_add_pixel[1] = -snake_vector

        window.fill(window_background)

        draw_fruit_rect(fruit_default_x, fruit_default_y, rect_size, window)
        growth_snake(get_all_snake_position, snake_index, rect_size, window)        
        
        pygame.display.flip()

        # 1.0 Get collision when head od snake collide with fruit 
        if snake_position_and_size == fruit_position_and_size:
            # 1.1 Increase snake length
            snake_index += -1

            # 1.2 Set new random position to fruit
            fruit_default_x: int = randrange((window_width - window_width), window_width, rect_size)
            fruit_default_y: int = randrange((window_height - window_height), window_height, rect_size)
        
        # 2.0 When rect x axis is > than 480px, rect appear on left side of window
        if (snake_position_and_size[0] + rect_size) > window_width:
            snake_default_x = (window_width - window_width - rect_size)

        # 2.1 When rect x axis is < than 0px, rect appear on right side of window
        if snake_position_and_size[0] < (window_width - window_width):
            snake_default_x = window_width
        
        # 2.2 When rect y axis is > than 480px, rect appear on up side of window
        if (snake_position_and_size[1] + rect_size) > window_height:
            snake_default_y = (window_height - window_height - rect_size)

        # 2.3 When rect y axis is < than 0px, rect appear on down side of window
        if snake_position_and_size[1] < (window_height - window_height):
            snake_default_y = window_height

if __name__ == "__main__":
    main()