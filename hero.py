import pygame
import sys
from settings import config

class Hero(pygame.sprite.Sprite):
    def __init__(self, posX:int, posY:int, group: pygame.sprite.Group) -> None:
        """Инициализация основного класса игрока

        Args:
            posX (int): координата x
            posY (int): координата y
            group (pygame.sprite.Group): группа спрайтов к которой будет принадлежать игрок
        """
        super().__init__(group)
        
        self.image = pygame.Surface((64, 32))
        self.image.fill(config["GREEN"])
        
        self.rect = self.image.get_rect()