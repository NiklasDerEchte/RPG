import pygame
class Sprite:
    def __init__(self, filename, width, height, col, row, offestTop=0, offestBottom=0, offsetLeft=0, offsetRight=0):
        self.sprite = pygame.image.load(filename).convert_alpha()
        self.colls = col
        self.rows = row
        self.spriteWidth = width / col
        self.spriteHeight = height / row
        self.cells = [[pygame.Rect((x*self.spriteWidth) + offsetLeft, (y*self.spriteHeight) + offestTop, self.spriteWidth, self.spriteHeight) for x in range(row)] for y in range (col)]
        self.width = self.spriteWidth - offsetRight
        self.height = self.spriteHeight - offestBottom
        self.frame = 0
        self.fpsCounter = 0
        self.isMoving = False

    def draw(self, window, dest, direction, delay=10):
        if self.isMoving:
            self.fpsCounter = self.fpsCounter + 1
            if self.fpsCounter == delay:
                self.fpsCounter = 0
                self.frame = self.frame + 1
            if self.frame == self.rows:
                self.frame = 0
            window.blit(self.sprite, dest, (self.cells[direction][self.frame]))
        else:
            window.blit(self.sprite, dest, (self.cells[direction][0]))