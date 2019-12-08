import pygame
from settings import *
from sprite import *
from obstacle import *
from map import *
from player import *
from port import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RPG")
        self.window = pygame.display.set_mode((windowXSize, windowYSize))
        self.start_level("home")
        self.loop()

    def start_level(self, filename):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.playerSprite = Sprite("assets/Patreon sprites 1/3.png", width=192, height=256, col=4, row=4, offsetLeft=9, offestTop=18, offestBottom=15, offsetRight=19)
        self.player = Player(self.playerSprite.width, self.playerSprite.height/2)
        self.allSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.ports = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.load_map("assets/map/" + filename + ".tmx")
        self.camera = Camera(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.spritePosition = pygame.Rect(self.player.rect.x, self.player.rect.y - (self.playerSprite.spriteHeight / 2),
                                          self.playerSprite.height, self.playerSprite.width)


    def load_map(self, filename):
        self.tileMap = TileMap(filename)
        self.map = self.tileMap.make_map()
        for obj in self.tileMap.tmxdata.objects:
            if obj.name == 'wall':
                obstacle = Obstacle()
                obstacle.rect.x = obj.x
                obstacle.rect.y = obj.y
                obstacle.rect.width = obj.width
                obstacle.rect.height = obj.height
                self.obstacleSprites.add(obstacle)
            elif obj.name == 'player':
                self.player.rect.x = obj.x
                self.player.rect.y = obj.y
            elif obj.name == 'port':
                port = Port(obj.x, obj.y, obj.width, obj.height)
                port.nextMap = obj.type
                self.ports.add(port)


    def debug_mode(self):
        pygame.draw.rect(self.window, purple, self.camera.apply(self.player.rect), 1)
        print(self.clock.get_fps())

    def loop(self):
        while(self.isRunning):
            self.clock.tick(fps)
            self.update()
            self.collide()
            self.draw()
            self.close_listener()
        pygame.quit()

    def collide(self):
        hits = pygame.sprite.spritecollide(self.player, self.obstacleSprites, False)
        if hits:
            self.player.rect.x = self.player.posX
            self.player.rect.y = self.player.posY
        hits = pygame.sprite.spritecollide(self.player, self.ports, False)
        if hits:
            self.start_level(hits[0].nextMap)

    def close_listener(self):
        events = pygame.event.get()
        for key in events:
            if key.type == pygame.QUIT:
                self.isRunning = False

    def draw(self):
        self.window.fill(black)
        self.window.blit(self.map, self.camera.apply(self.map.get_rect()))
        self.playerSprite.draw(self.window, self.camera.apply(self.spritePosition), self.player.direction)
        if DEBUG:
            self.debug_mode()
        pygame.display.flip()

    def update(self):
        self.allSprites.update()
        self.playerSprite.isMoving = self.player.isMoving
        self.spritePosition.y = self.player.rect.y - (self.playerSprite.height / 2)
        self.spritePosition.x = self.player.rect.x
        self.camera.update(self.player)

game = Game()
