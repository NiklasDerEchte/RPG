import pygame
from settings import *
from obstacle import *
from map import *
from player import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RPG")
        self.window = pygame.display.set_mode((windowXSize, windowYSize))
        self.new_game()
        self.loop()

    def new_game(self):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.allSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.load_map("assets/map/home.tmx")
        self.camera = Camera(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    def load_sprite_sheet(self, filename, col, row):
        sprite = pygame.image.load(filename).convert_alpha()
        spriteWidth = sprite.rect.width / row
        spriteHeight = sprite.rect.height / col

        pass

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

    def loop(self):
        while(self.isRunning):
            self.clock.tick(fps)
            print(self.clock.get_fps())
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

    def close_listener(self):
        events = pygame.event.get()
        for key in events:
            if key.type == pygame.QUIT:
                self.isRunning = False

    def draw(self):
        self.window.fill(black)
        self.window.blit(self.map, self.camera.apply(self.map.get_rect()))
        for sprite in self.allSprites.sprites():
            pygame.draw.rect(self.window, sprite.color, self.camera.apply(sprite.rect))
        pygame.display.flip()

    def update(self):
        self.allSprites.update()
        self.camera.update(self.player)

game = Game()