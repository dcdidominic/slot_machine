
import sys
import pygame

from settings import *
from machine import Machine

class Game:
    def __init__(self):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Party Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        # Machine class
        self.machine = Machine()
        self.delta_time = 0

        # Sound
        if PLAY_SOUND:
            main_sound = pygame.mixer.Sound(MAIN_SOUND)
            main_sound.play(loops = -1)

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0,0))
            self.machine.update(self.delta_time, self.screen)
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()