
import os
import pygame
import random

from settings import *

class Reel:
    def __init__(self, pos):
        self.symbol_list = pygame.sprite.Group()
        self.shuffled_keys = list(symbols.keys())
        random.shuffle(self.shuffled_keys)
        init_keys = self.shuffled_keys[:4]

        self.reel_is_spinning = False
        
        # Sounds
        self.stop_sound = pygame.mixer.Sound(STOP_SOUND)
        self.stop_sound.set_volume(0.5)

        for idx, item in enumerate(init_keys):
            self.symbol_list.add(Symbol(symbols[item], pos, idx))
            pos = list(pos)
            pos[1] += 150
            pos = tuple(pos)

    def animate(self, delta_time):
        if self.reel_is_spinning:
            self.delay_time -= (delta_time * 1000)
            self.spin_time -= (delta_time * 1000)
            reel_is_stopping = False

            if self.spin_time < 0:
                reel_is_stopping = True

            # Stagger reel spin start animcation
            if self.delay_time <= 0:

                # Iterate through all 3 symbols in reel; truncate; add new random symbol on top of stack
                for symbol in self.symbol_list:
                    symbol.rect.bottom += 75

                    # Correct spacing is dependant on the adove addition eventually hitting 700?
                    if symbol.rect.top == 700:
                        if reel_is_stopping:
                            self.reel_is_spinning = False
                            self.stop_sound.play()
                        
                        symbol_idx = symbol.idx
                        symbol.kill()
                        # Spawn random symbol in place of the above
                        self.symbol_list.add(Symbol(symbols[random.choice(self.shuffled_keys)], ((symbol.x_val), 100), symbol_idx))

    def start_spin(self, delay_time):
        self.delay_time = delay_time
        self.spin_time = 3000 + delay_time
        self.reel_is_spinning = True

    def reel_spin_result(self):
        return self.symbol_list.sprites()[1].sym_type

class Symbol(pygame.sprite.Sprite):
    def __init__(self, pathToFile, pos, idx):
        super().__init__()

        # Friendly name
        self.sym_type = os.path.splitext(pathToFile)[0]

        self.pos = pos
        self.idx = idx
        self.image = pygame.image.load(pathToFile).convert_alpha()
        self.image = pygame.transform.scale(self.image, (SYM_SIZE, SYM_SIZE))
        self.rect = self.image.get_rect(topleft = pos)
        self.x_val = self.rect.left

    def update(self):
        pass