import pygame
from pygame import *
import random

class Bigbubble(pygame.sprite.Sprite):

	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		

	def update(self):
		if self.rect.top > self.F_HOEHE:
			self.kill()
		z = pygame.time.get_ticks()
		if z >= self.tod:
			self.alive = False
			self.kill()
			
	def start(self, F_BREITE, F_HOEHE):
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("bigbubble.png")
		self.image = pygame.transform.scale(self.image, (200, 200))
		self.rect = self.image.get_rect()
		self.rect.center = (-10, -10)
		self.alive = False
		self.tod = pygame.time.get_ticks() + 10000
		
