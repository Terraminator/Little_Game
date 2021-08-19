import pygame
from pygame import *
import random

class Welcome(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("Welcome.png")
		self.image = pygame.transform.scale(self.image, (1000, 600))
		self.rect = self.image.get_rect()
		self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)