import pygame, sys
from config import *
from level import Level


class Game:
    def __init__(self):

        # general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF | pygame.SCALED,
                                              vsync=1)

        pygame.display.set_caption('Mega-Alpha-Force')
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.clock.tick(60)

            self.screen.fill('blue')
            self.level.run()

            pygame.display.update()

            pygame.display.set_caption(str(self.clock.get_fps()))


if __name__ == '__main__':
    game = Game()
    game.run()

