import pygame
from pygame import *
import random

class Item(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("item.jpg")
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(0, F_BREITE), random.randint(0, F_HOEHE))
		self.x = 0
		self.alive = True
		if self.rect.center == (self.F_BREITE / 2, self.F_HOEHE / 2):
			self.rect.center = (random.randint(0, F_BREITE), random.randint(0, F_HOEHE))
	def update(self):
		if self.rect.top > self.F_HOEHE:
			self.kill()
