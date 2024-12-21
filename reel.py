
import os
import pygame
import random

from settings import *

class Reel:
    def __init__(self, pos:tuple):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        self.shuffled_keys = self.shuffled_keys[:3]

        self.reel_is_spinning = False
        
        # Sounds
        # self.stop_sound = pygame.mixer.Sound('audio/stop.mp3')
        # self.stop_sound.set_volume(0.5)

        for idx, item in enumerate(self.shuffled_keys):
            self.symbol_list.add(Symbol(symbols[item], pos, idx))
            pos = list(pos)
            pos[1] += 300
            pos = tuple(pos)

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile, pos, idx):
        super().__init__()

        # Friendly name
        self.sym_type = os.path.splitext(pathToFile)[0]

        self.pos = pos
        self.idx = idx
        self.image = pygame.image.load(pathToFile).convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass