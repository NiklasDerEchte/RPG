import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(120, 120, playerXSize, playerYSize)
        self.color = blue
        self.posX = self.rect.x
        self.posY = self.rect.y

    def update(self):
        keys = pygame.key.get_pressed()
        self.posX = self.rect.x
        self.posY = self.rect.y
        if keys[pygame.K_a]:
            self.rect.x += -playerSpeed
        if keys[pygame.K_d]:
            self.rect.x += playerSpeed
        if keys[pygame.K_w]:
            self.rect.y += -playerSpeed
        if keys[pygame.K_s]:
            self.rect.y += playerSpeed
