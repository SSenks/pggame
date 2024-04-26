import pygame
import sys
from settings import config
from hero import Hero

class World(): # Класс мира 
    
    def __init__(self):
        self.display = pygame.display.get_surface() # Получил поверхность
    
        self.sprites = pygame.sprite.Group()
        
        self.setup()
        
    def setup(self) -> None:
        self.hero = Hero(50, 20, self.sprites)
        

    def run(self, frame):
        self.display.fill(config["GOLD"])
        self.sprites.draw(self.display)
        self.sprites.update()