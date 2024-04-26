import pygame
import sys
from world import World
from settings import config

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config["WIDTH"],config["HEIGHT"]))
        self.clock = pygame.time.Clock()
        
        self.world = World() # Храню тут мир
        
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            frame = self.clock.tick()
            self.world.run(frame)
            pygame.display.update()
            
if __name__ == "__main__":
    game = Game()
    game.start()