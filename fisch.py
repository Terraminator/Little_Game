import pygame
from pygame import *

class Fisch(pygame.sprite.Sprite):
	
	def __init__(self, F_BREITE, F_HOEHE):
		super().__init__()
		self.F_BREITE = F_BREITE
		self.F_HOEHE = F_HOEHE
		self.image = pygame.image.load("fisch.png")
		self.image = pygame.transform.scale(self.image, (100, 50))
		self.rect = self.image.get_rect()
		self.rect.center = (self.F_BREITE / 2, self.F_HOEHE / 2)
		self.speed = 8
		self.lt = None
		self.leben = 20
	
	def block(self, strong):
		if strong == None:
			if self.lt == "up":
				self.rect.y += 8
				self.image = pygame.image.load("fischup.png")
				self.image = pygame.transform.scale(self.image, (50, 100))
			elif self.lt == "down":
				self.rect.y -= 8
				self.image = pygame.image.load("fischdown.png")
				self.image = pygame.transform.scale(self.image, (50, 100))
			elif self.lt == "left":
				self.rect.x += 8
				self.image = pygame.image.load("fischleft.png")
				self.image = pygame.transform.scale(self.image, (100, 50))
			elif self.lt == "right":
				self.rect.x -= 8
				self.image = pygame.image.load("fisch.png")
				self.image = pygame.transform.scale(self.image, (100, 50))
				
		else:
			if self.lt == "up":
				self.rect.y += strong
				self.image = pygame.image.load("fischup.png")
				self.image = pygame.transform.scale(self.image, (50, 100))
			elif self.lt == "down":
				self.rect.y -= strong
				self.image = pygame.image.load("fischdown.png")
				self.image = pygame.transform.scale(self.image, (50, 100))
			elif self.lt == "left":
				self.rect.x += strong
				self.image = pygame.image.load("fischleft.png")
				self.image = pygame.transform.scale(self.image, (100, 50))
			elif self.lt == "right":
				self.rect.x -= strong
				self.image = pygame.image.load("fisch.png")
				self.image = pygame.transform.scale(self.image, (100, 50))
				
				
	def update(self):
		if self.leben <= 0:
			self.kill()
		gedrueckt = pygame.key.get_pressed()
		if gedrueckt[pygame.K_w]:
			self.rect.y -= self.speed
			self.lt = "up"
			self.image = pygame.image.load("fischup.png")
			self.image = pygame.transform.scale(self.image, (50, 100))
		elif gedrueckt[pygame.K_s]:
			self.rect.y += self.speed
			self.lt = "down"
			self.image = pygame.image.load("fischdown.png")
			self.image = pygame.transform.scale(self.image, (50, 100))
		elif gedrueckt[K_a]:
			self.rect.x -= self.speed
			self.lt = "left"
			self.image = pygame.image.load("fischleft.png")
			self.image = pygame.transform.scale(self.image, (100, 50))
		elif gedrueckt[K_d]:
			self.rect.x += self.speed
			self.lt = "right"
			self.image = pygame.image.load("fisch.png")
			self.image = pygame.transform.scale(self.image, (100, 50))
			
		self.rect.clamp_ip(pygame.Rect(0, 0, self.F_BREITE, self.F_HOEHE))