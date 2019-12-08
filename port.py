import pygame
class Port(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.nextMap = ""
        self.rect = pygame.Rect(x, y, width, height)