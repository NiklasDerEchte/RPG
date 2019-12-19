import pygame
from sprite import *
from settings import *
class Charakter(pygame.sprite.Sprite):
    def __init__(self, dialog_array, charakter_name, charakter_id, sprite_rect, window, map_name):
        pygame.sprite.Sprite.__init__(self)
        self.dialog = Dialog(dialog_array)
        self.rect = sprite_rect
        self.name = charakter_name
        self.id = charakter_id
        self.__font = pygame.font.SysFont('arial', 30)
        self.isDialogStarted = False
        self.window = window
        self.map = map_name

    def load_sprite(self, path, offset_top = 0, offset_bottom = 0, offset_left = 0, offset_right = 0):
        self.sprite = Sprite(path, width=192, height=256, col=4, row=4, offestTop=offset_top, offestBottom=offset_bottom, offsetLeft=offset_left, offsetRight=offset_right)

    def update(self):
        pass

    def blit_text(self, surface, text, pos, font, color):
        words = [word.split(' ') for word in text.splitlines()]
        space = font.size(' ')[0]
        max_width = windowYSize
        max_height = windowXSize
        x, y = pos
        word_height = 0
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]
                    y += word_height
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]
            y += word_height

    def draw(self, camera, message_x = 0, message_y = 0):
        self.sprite.draw(self.window, camera.apply(self.rect), 0)
        if self.isDialogStarted:
            self.blit_text(self.window, self.name + ": " + self.dialog.get_current_message(), (message_x, message_y), self.__font, (255, 128, 0))


class Dialog:
    def __init__(self, dialogArray):
        self.dialog_array = dialogArray
        self.dialog_pos = 0

    def reset(self):
        self.dialog_pos = 0

    def has_dialog(self):
        return self.dialog_pos < len(self.dialog_array)-1

    def get_current_message(self):
        if self.dialog_pos > len(self.dialog_array):
            return False
        return self.dialog_array[self.dialog_pos]

    def get_next_dialog(self):
        if self.has_dialog():
            dialog = self.dialog_array[self.dialog_pos]
            self.dialog_pos = self.dialog_pos+1
            return dialog
        else:
            return False


allCharakter = pygame.sprite.Group()

def parse_charakter(name, window):
    global charakter
    array = charakter[name]
    rect = pygame.Rect(array['rect'][0], array['rect'][1], array['rect'][2], array['rect'][3])
    char = Charakter(dialog_array=array['m'], charakter_name=array['name'], charakter_id=name, sprite_rect=rect, window=window, map_name=array['map'])
    if "offset" in array:
        char.load_sprite(array['sprite'], array['offset'][0], array['offset'][1], array['offset'][2], array['offset'][3])
    else:
        char.load_sprite(array['sprite'])
    return char

def get_colliding_charakter(player):
    hits = pygame.sprite.spritecollide(player, allCharakter, False)
    if hits:
        return hits[0]
    else:
        return False


charakter = {
    "man": {
        "name": "Vadder",
        "m": ["Jo, erstmal ein gut cool in die Runde !", "Was macht denn die Frucht meines Samens hier ?"],
        "rect": [350, 300, 192/4, 256/4],
        "offset": [18, 10, 10, 20],
        "sprite": "assets/Patreon sprites 1/2.png",
        "map": "home"
    },
    "typ": {
            "name": "Typ",
            "m": ["Raus mit de Viecher !"],
            "rect": [0, 0, 192/4, 256/4],
            "offset": [18, 10, 10, 20],
            "sprite": "assets/Patreon sprites 1/2.png",
            "map": "home_first_floor"
        }
}
