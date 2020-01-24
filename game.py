import pygame
from settings import *
from sprite import *
from obstacle import *
from map import *
from player import *
from port import *
from spawn import *
from charakter import *
from matrix import *
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("RPG")
        self.window = pygame.display.set_mode((windowXSize, windowYSize))
        self.curMap = "home"
        self.load_charakter()
        self.start_level(self.curMap)
        self.loop()

    def load_charakter(self):
        for id in charakter:
            c = parse_charakter(id, self.window)
            allCharakter.add(c)

    def start_level(self, filename):
        self.isRunning = True
        self.clock = pygame.time.Clock()
        self.matrix = Matrix(MAX_WIDTH, MAX_HEIGHT, tileSize)
        self.playerSprite = Sprite("assets/Patreon sprites 1/3.png", width=192, height=256, col=4, row=4, offsetLeft=9, offestTop=18, offestBottom=15, offsetRight=19)
        self.player = Player(self.playerSprite.width, self.playerSprite.height/2, self.matrix)
        self.allSprites = pygame.sprite.Group()
        self.obstacleSprites = pygame.sprite.Group()
        self.ports = pygame.sprite.Group()
        self.playerSpawns = pygame.sprite.Group()
        self.allSprites.add(self.player)
        self.load_map(filename,"assets/map/" + filename + ".tmx")
        self.camera = Camera(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.spritePosition = pygame.Rect(self.player.rect.x, self.player.rect.y - (self.playerSprite.spriteHeight / 2),
                                          self.playerSprite.height, self.playerSprite.width)
        self.curMap = filename


    def load_map(self, filename, path):
        self.tileMap = TileMap(path)
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
                spawn = Spawn(obj.x, obj.y, obj.width, obj.height)
                spawn.type = obj.type
                self.playerSpawns.add(spawn)
            elif obj.name == 'port':
                port = Port(obj.x, obj.y, obj.width, obj.height)
                port.nextMap = obj.type
                self.ports.add(port)
            elif obj.name == "npc":
                for charakter in allCharakter:
                    if charakter.id == obj.type:
                        charakter.rect.x, charakter.rect.y = self.matrix.position_reset((obj.x, obj.y))
                        break

        for spawn in self.playerSpawns:
            if SPAWN_MAP == filename and self.curMap == filename:
                if spawn.type == "spawn":
                    self.player.set_world_pos(self.matrix.position_reset((spawn.rect.x, spawn.rect.y)))
                    break
            else:
                if self.curMap == spawn.type:
                    self.player.set_world_pos(self.matrix.position_reset((spawn.rect.x, spawn.rect.y)))
                    break


    def debug_mode(self):
        pygame.draw.rect(self.window, purple, self.camera.apply(self.player.rect), 1)
        for charakter in allCharakter:
            if charakter.map == self.curMap:
                pygame.draw.rect(self.window, purple, self.camera.apply(charakter.rect), 1)
        print(self.player.cur_tile_pos)
        self.matrix.debug(self.window, self.camera)

    def key_listener(self):
        global DEBUG
        events = pygame.event.get()
        for key in events:
            if key.type == pygame.QUIT:
                self.isRunning = False
            elif key.type == pygame.KEYUP:
                if key.key == pygame.K_e:
                    self.key_e_up()
                elif key.key == pygame.K_F1:
                    DEBUG = not DEBUG

    def key_e_up(self):
        charakter = get_colliding_charakter(self.player)
        if charakter and charakter.map == self.curMap:
            if not charakter.isDialogStarted:
                charakter.isDialogStarted = True
                self.player.canMove = False
                charakter.dialog.next_message()
            else:
                if charakter.dialog.has_dialog():
                    charakter.dialog.next_message()
                else:
                    charakter.isDialogStarted = False
                    charakter.dialog.reset()
                    self.player.canMove = True
            if charakter.dialog.get_current_message() == False:
                charakter.isDialogStarted = False
                self.player.canMove = True

    def loop(self):
        while(self.isRunning):
            self.clock.tick(fps)
            self.update()
            self.collide()
            self.move_player()
            self.draw()
            self.key_listener()
        pygame.quit()

    def collide(self):
        hit = False
        self.player.update_pos((self.player.cur_tile_pos + self.player.move_direction))
        hits = pygame.sprite.spritecollide(self.player, self.obstacleSprites, False)
        if hits:
            hit = True
        hits = pygame.sprite.spritecollide(self.player, self.ports, False)
        if hits:
            self.start_level(hits[0].nextMap)
            return
        self.player.update_pos((self.player.cur_tile_pos - self.player.move_direction))
        if hit:
            self.player.move_direction.x = 0
            self.player.move_direction.y = 0

    def draw(self):
        self.window.fill(black)
        self.window.blit(self.map, self.camera.apply(self.map.get_rect()))
        for charakter in allCharakter:
            if charakter.map == self.curMap:
                charakter.draw(self.camera, message_x=0, message_y=WINDOW_HEIGHT * 0.8)
        self.playerSprite.draw(self.window, self.camera.apply(self.spritePosition), self.player.direction)
        if DEBUG:
            self.debug_mode()
        pygame.display.flip()

    def move_player(self):
        if self.player.is_moving:
            for i in range(int(tileSize/2)):
                self.player.update_world_pos((self.player.rect.x + (self.player.move_direction.x * 2), self.player.rect.y + (self.player.move_direction.y  * 2)))
                self.spritePosition.y = self.player.rect.y - (self.playerSprite.height / 2)
                self.spritePosition.x = self.player.rect.x
                self.camera.update(self.player)
                self.draw()
                pygame.event.clear()
                pygame.time.wait(10)


    def update(self):
        self.allSprites.update()
        self.playerSprite.isMoving = self.player.is_moving
        self.spritePosition.y = self.player.rect.y - (self.playerSprite.height / 2)
        self.spritePosition.x = self.player.rect.x
        self.camera.update(self.player)

game = Game()
