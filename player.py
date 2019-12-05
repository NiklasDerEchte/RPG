import pygame
from settings import *

class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(0, 0, width, height)
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.isMoving = False
        self.direction = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.posX = self.rect.x
        self.posY = self.rect.y
        self.isMoving = False
        if keys[pygame.K_a]:
            self.rect.x += -playerSpeed
            self.isMoving = True
            self.direction = 1
        if keys[pygame.K_d]:
            self.rect.x += playerSpeed
            self.isMoving = True
            self.direction = 2
        if keys[pygame.K_w]:
            self.rect.y += -playerSpeed
            self.isMoving = True
            self.direction = 3
        if keys[pygame.K_s]:
            self.rect.y += playerSpeed
            self.isMoving = True
            self.direction = 0