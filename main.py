import sys
import pygame

from settings import *
from machine import Machine

class Game:
    def __init__(self, starting_pot=0):

        # General setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Party Slot Machine')
        self.clock = pygame.time.Clock()
        self.bg_image = pygame.image.load(BG_IMAGE_PATH)

        # Starting pot amount
        self.starting_pot = starting_pot

        # Machine class
        self.machine = Machine(self.starting_pot)
        self.delta_time = 0

        # Sound
        if PLAY_SOUND:
            main_sound = pygame.mixer.Sound(MAIN_SOUND)
            main_sound.set_volume(0.5)
            main_sound.play(loops=-1)

    def run(self):

        self.start_time = pygame.time.get_ticks()

        while True:
            # Handle quit operation
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Time variables
            self.delta_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.start_time = pygame.time.get_ticks()

            pygame.display.update()
            self.screen.blit(self.bg_image, (0, 0))
            self.machine.update(self.delta_time, self.screen)
            self.clock.tick(FPS)

if __name__ == "__main__":
    try:
        starting_pot = int(input("Enter the starting pot amount (leave blank to set to 0): ") or 0)
    except ValueError:
        starting_pot = 0
    
    game = Game(starting_pot)
    game.run()
