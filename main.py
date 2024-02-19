from pygame import init, quit
from pygame.time import get_ticks, delay

from src.game import Game

init()


def main() -> None:

    game = Game("PySnake", 800, 600)

    frameStart: int
    frameTime: int

    while game.menu.running:
        game.menu.handleEvents()
        game.menu.update()
        game.menu.render()

    while game.running:

        frameStart = get_ticks()

        game.handleEvents()
        game.update()
        game.render()

        frameTime = get_ticks() - frameStart

        if game.frame_delay > frameTime:
            delay(game.frame_delay - frameTime)

    if game.menu.running == False and game.running == False:
        quit()
    else:
        main()


if "__main__" == __name__:
    main()
