import pygame
from pygame import *
import random

class Wand(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.x = 0
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("wand.jpg")
		self.image = pygame.transform.scale(self.image, (1000, 50))
		self.rect = self.image.get_rect()
		self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)
		self.alive = True
		
	def update(self):
		if self.rect.top > self.F_HOEHE:
			self.kill()
			self.update()
		if pygame.time.get_ticks() >= 15000:
			self.kill()
			self.alive = False