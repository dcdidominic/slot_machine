
import pygame
pygame.init()


from creditor import Creditor

from settings import *

class Messages():

    def __init__(self):
        # Images
        self.font = pygame.font.Font(None, 30)
        self.stolen_img = pygame.image.load(STOLEN_IMG).convert_alpha()
        self.tamper_img = pygame.image.load(TAMPER_IMG).convert_alpha()
        self.scale_pwr_img = pygame.image.load(SCALE_PWR_IMG).convert_alpha()
        self.jackpot_img = pygame.image.load(JACKPOT_IMG).convert_alpha()
        self.chicken_win_img = pygame.image.load(CHICKEN_WIN_IMG).convert_alpha()
        self.beer_win_img = pygame.image.load(BEER_WIN_IMG).convert_alpha()
        self.chance_win_img = pygame.image.load(CHANCE_WIN_IMG).convert_alpha()
        
        # Sounds
        self.sound_playing = False
        self.jackpot_sound = pygame.mixer.Sound(JACKPOT_WIN_SOUND)
        self.jackpot_sound.set_volume(1.0)
        self.chicken_sound = pygame.mixer.Sound(CHICKEN_SOUND)
        self.chicken_sound.set_volume(1.0)
        self.beer1_sound = pygame.mixer.Sound(BEER1_SOUND)
        self.beer1_sound.set_volume(1.0)
        self.beer2_sound = pygame.mixer.Sound(BEER2_SOUND)
        self.beer2_sound.set_volume(1.0)
        self.CHANCE_sound = pygame.mixer.Sound(CHANCE_SOUND)
        self.CHANCE_sound.set_volume(1.0)
        

    def check_creditor(self, creditor:Creditor):
        if creditor.stolen:
            display_surface = pygame.display.get_surface()
            display_surface.blit(self.stolen_img, (0,0))

        if creditor.tamper:
            display_surface = pygame.display.get_surface()
            display_surface.blit(self.tamper_img, (0,0))

    def display_spin_count(self, info, y=50, x=10):
        display_surface = pygame.display.get_surface()
        debug_surf = self.font.render(str(info), True, (255, 255, 255))
        debug_rect = debug_surf.get_rect(midtop=(display_surface.get_width() / 2, y))  # Center at the top
        
        # Draw a rounded rectangle with a fun color
        pygame.draw.rect(display_surface, 'Purple', debug_rect.inflate(20, 20), border_radius=10)
        display_surface.blit(debug_surf, debug_rect)

    def display_scale_error(self):
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.scale_pwr_img, (0,0))
        self.sound_playing = True

    def display_jackpot(self):
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.jackpot_img, (0,0)) 
        self.jackpot_sound.play() if not self.sound_playing else None
        self.sound_playing = True

    def display_chicken(self):
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.chicken_win_img, (0,0)) 
        self.chicken_sound.play() if not self.sound_playing else None
        self.sound_playing = True

    def display_beer(self):
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.beer_win_img, (0,0))
        self.beer1_sound.play() if not self.sound_playing else None
        self.beer2_sound.play() if not self.sound_playing else None
        self.sound_playing = True

    def display_chance(self):
        display_surface = pygame.display.get_surface()
        display_surface.blit(self.chance_win_img, (0,0)) 
        self.chance_sound.play() if not self.sound_playing else None
        self.sound_playing = True
