import pygame
from pygame import *
import random

class Enemy(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("enemy1.png")
		self.image = pygame.transform.scale(self.image, (100, 100))
		self.rect = self.image.get_rect()
		self.rect.center = (random.randint(0, F_BREITE), random.randint(0, F_HOEHE))
		self.speed = 15
		self.lt = None
		self.alive = True
		
	def block(self):
		if self.lt == "up":
			self.rect.y += 8
		elif self.lt == "down":
			self.rect.y -= 8
		elif self.lt == "left":
			self.rect.x += 8
		elif self.lt == "right":
			self.rect.x -= 8
				
				
	def update(self):
		rs = ["up", "down", "left", "right"]
		self.lt = random.choice(rs)
		if self.lt == "up":
			self.rect.y -= self.speed
			self.lt = "up"
		elif self.lt == "down":
			self.rect.y += self.speed
			self.lt = "down"
		elif self.lt == "left":
			self.rect.x -= self.speed
			self.lt = "left"
		elif self.lt == "right":
			self.rect.x += self.speed
			self.lt = "right"
		
		self.rect.clamp_ip(pygame.Rect(0, 0, self.F_BREITE, self.F_HOEHE))