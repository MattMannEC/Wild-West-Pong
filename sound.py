import pygame
import random
import glob
import os

class Sound:
    def __init__(self):
        pygame.mixer.init()

        sound_dir = "sounds"
        pistol_dir = "pistol"
        ricochet_dir = "ricochet"

        # Load pistol sound files
        self.pistol_sound_files = []
        pistol_sound_paths = glob.glob(os.path.join(os.getcwd(), f"{sound_dir}/{pistol_dir}", "*.wav"))

        for p in pistol_sound_paths:
            s = pygame.mixer.Sound(f"{sound_dir}/{pistol_dir}/{os.path.basename(p)}")
            self.pistol_sound_files.append(s)

        # Load ricochet sound files
        self.ricochet_sound_files = []
        ricochet_sound_paths = glob.glob(os.path.join(os.getcwd(), f"{sound_dir}/{ricochet_dir}", "*.wav"))

        for r in ricochet_sound_paths:
            s = pygame.mixer.Sound(f"{sound_dir}/{ricochet_dir}/{os.path.basename(r)}")
            self.ricochet_sound_files.append(s)

        self.main_theme = pygame.mixer.Sound(f"{sound_dir}/theme.wav")

        self.music()

    def music(self):
        self.main_theme.play(-1)

    def fire(self):
        self.rand_pistol_sound = random.choice(self.pistol_sound_files)
        self.rand_pistol_sound.play()

    def ricochet(self):
        self.rand_ricochet_sound = random.choice(self.ricochet_sound_files)
        self.rand_ricochet_sound.play()