import pygame
from pygame import *

class Bullet(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("bullet.png")
		self.image = pygame.transform.scale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)
		self.speed = 8
		self.lt = None
		self.gp = False
		self.alive = False
	def update(self):
		if self.lt == "up":
			self.rect.y -= self.speed
		elif self.lt == "down":
			self.rect.y += self.speed
		elif self.lt == "left":
			self.rect.x -= self.speed
		elif self.lt == "right":
			self.rect.x += self.speed
		else:
			gedrueckt = pygame.key.get_pressed()
			if gedrueckt[pygame.K_UP]:
				self.gp = True
				self.rect.y -= self.speed
				self.lt = "up"
				self.alive = True
			if gedrueckt[pygame.K_DOWN]:
				self.gp = True
				self.rect.y += self.speed
				self.lt = "down"
				self.alive = True
			if gedrueckt[K_LEFT]:
				self.gp = True
				self.rect.x -= self.speed
				self.lt = "left"
				self.alive = True
			if gedrueckt[K_RIGHT]:
				self.gp = True
				self.rect.x += self.speed
				self.lt = "right"
				self.alive = True
		
		self.rect.clamp_ip(pygame.Rect(0, 0, self.F_BREITE, self.F_HOEHE))