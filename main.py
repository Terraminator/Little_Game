import pygame, sys, fisch, wand, block, bigbubble, item, gras, welcome, bullet, enemy
from time import sleep

F_BREITE, F_HOEHE = 1000, 600

pygame.init()
fenster = pygame.display.set_mode((F_BREITE, F_HOEHE))
pygame.display.set_caption("Game")
sprites = pygame.sprite.Group()
welcome = welcome.Welcome(F_BREITE, F_HOEHE)
sprites.add(welcome)
sprites.draw(fenster)
pygame.display.flip()
sleep(5)
welcome.kill()

gras1 = gras.Gras(F_BREITE, F_HOEHE)
gras2 = gras.Gras(F_BREITE, F_HOEHE)
gras3 = gras.Gras(F_BREITE, F_HOEHE)
fisch = fisch.Fisch(F_BREITE, F_HOEHE)
enemy1 = enemy.Enemy(F_BREITE, F_HOEHE)
enemy2 = enemy.Enemy(F_BREITE, F_HOEHE)
enemy3 = enemy.Enemy(F_BREITE, F_HOEHE)
block1 = block.Block(F_BREITE, F_HOEHE)
block2 = block.Block(F_BREITE, F_HOEHE)
block3 = block.Block(F_BREITE, F_HOEHE)
block4 = block.Block(F_BREITE, F_HOEHE)
block5 = block.Block(F_BREITE, F_HOEHE)
block6 = block.Block(F_BREITE, F_HOEHE)
wand = wand.Wand(F_BREITE, F_HOEHE)
item = item.Item(F_BREITE, F_HOEHE)
bigbubble = bigbubble.Bigbubble(0, 0)
bullet = bullet.Bullet(F_BREITE, F_HOEHE)
sprites.add(fisch)
sprites.add(gras1)
sprites.add(gras2)
sprites.add(gras3)
sprites.add(enemy1)
sprites.add(enemy2)
sprites.add(enemy3)
sprites.add(block1)
sprites.add(block2)
sprites.add(block3)
sprites.add(block4)
sprites.add(block5)
sprites.add(block6)
sprites.add(wand)
sprites.add(item)
uhr = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	for sprite in sprites:
		if pygame.sprite.collide_rect(fisch, block1) or pygame.sprite.collide_rect(fisch, block2) or pygame.sprite.collide_rect(fisch, block3) or pygame.sprite.collide_rect(fisch, block4) or pygame.sprite.collide_rect(fisch, block5) or pygame.sprite.collide_rect(fisch, block6):
			fisch.block(None)
		if pygame.sprite.collide_rect(fisch, wand) and wand.alive == True:
			fisch.block(None)
		try:
			if pygame.sprite.collide_rect(bigbubble, block1) or pygame.sprite.collide_rect(bigbubble, block2) or pygame.sprite.collide_rect(bigbubble, block3) or pygame.sprite.collide_rect(bigbubble, block4) or pygame.sprite.collide_rect(bigbubble, block5) or pygame.sprite.collide_rect(bigbubble, block6):
				lol = True
			else:
				lol = False
			if lol == True and bigbubble.alive == True:
				fisch.block(4)
			if pygame.sprite.collide_rect(bigbubble, wand) and wand.alive == True and bigbubble.alive == True:
				fisch.block(4)
		except:
			pass
		if pygame.sprite.collide_rect(fisch, item) and item.alive == True:
			bigbubble.start(F_BREITE, F_HOEHE)
			sprites.add(bigbubble)
			bigbubble.alive = True
			fisch.kill()
			sprites.add(fisch)
			gras1.kill()
			gras2.kill()
			gras3.kill()
			sprites.add(gras1)
			sprites.add(gras2)
			sprites.add(gras3)
			block1.kill()
			block2.kill()
			block3.kill()
			block4.kill()
			block5.kill()
			block6.kill()
			sprites.add(block1)
			sprites.add(block2)
			sprites.add(block3)
			sprites.add(block4)
			sprites.add(block5)
			sprites.add(block6)
			wand.kill()
			sprites.add(wand)
			item.kill()
			item.alive = False
			
			
	if pygame.sprite.collide_rect(bullet, block1) or pygame.sprite.collide_rect(bullet, block2) or pygame.sprite.collide_rect(bullet, block3) or pygame.sprite.collide_rect(bullet, block4) or pygame.sprite.collide_rect(bullet, block5) or pygame.sprite.collide_rect(bullet, block6):
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
	if pygame.sprite.collide_rect(bullet, wand) and wand.alive == True:
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
			
	fenster.fill((0, 255, 255))
	rb = bullet.rect.right
	lb = bullet.rect.left
	ob = bullet.rect.top
	ub = bullet.rect.bottom
	if lb == 0 or ub == F_HOEHE or rb == F_BREITE or ob == 0:
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
	if bullet.alive == False:
		bullet.kill()
	if bullet.alive == True:
		sprites.add(bullet)
		fisch.kill()
		sprites.add(fisch)
		gras1.kill()
		gras2.kill()
		gras3.kill()
		sprites.add(gras1)
		sprites.add(gras2)
		sprites.add(gras3)
		block1.kill()
		block2.kill()
		block3.kill()
		block4.kill()
		block5.kill()
		block6.kill()
		sprites.add(block1)
		sprites.add(block2)
		sprites.add(block3)
		sprites.add(block4)
		sprites.add(block5)
		sprites.add(block6)
		wand.kill()
		sprites.add(wand)
		if item.alive == True:
			item.kill()
			sprites.add(item)
		
	if pygame.sprite.collide_rect(bullet, enemy1) and enemy1.alive == True and bullet.alive == True:
		enemy1.kill()
		enemy1.alive = False
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
		bullet.kill()
	if pygame.sprite.collide_rect(bullet, enemy2) and enemy2.alive == True and bullet.alive == True:
		enemy2.kill()
		enemy2.alive = False
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
		bullet.kill()
	if pygame.sprite.collide_rect(bullet, enemy3) and enemy3.alive == True and bullet.alive == True:
		enemy3.kill()
		enemy3.alive = False
		bullet.rect.center = fisch.rect.center
		bullet.lt = None
		bullet.alive = False
		bullet.kill()
	if bigbubble.alive == True:
		if pygame.sprite.collide_rect(bigbubble, enemy1) and enemy1.alive == True and bigbubble.alive == True:
			enemy1.kill()
			enemy1.alive = False
		if pygame.sprite.collide_rect(bigbubble, enemy2) and enemy2.alive == True and bigbubble.alive == True:
			enemy2.kill()
			enemy2.alive = False
		if pygame.sprite.collide_rect(bigbubble, enemy3) and enemy3.alive == True and bigbubble.alive == True:
			enemy3.kill()
			enemy3.alive = False
	if pygame.sprite.collide_rect(fisch, enemy1) and enemy1.alive == True:
		fisch.leben -= 1
	if pygame.sprite.collide_rect(fisch, enemy2) and enemy2.alive == True:
		fisch.leben -= 1
	if pygame.sprite.collide_rect(fisch, enemy3) and enemy3.alive == True:
		fisch.leben -= 1
		
	if bullet.gp == True:
		bullet.rect.center = fisch.rect.center
		bullet.gp = False
		
	sprites.update()
	bullet.update()
	try:
		bigbubble.rect.center = fisch.rect.center
	except:
		pass
		
	if enemy1.alive == False and enemy2.alive == False and enemy3.alive == False:
		print("Victory")
		pygame.quit()
		sys.exit()
	if fisch.leben <= 0:
		print("Game Over")
		pygame.quit()
		sys.exit()
	
	sprites.draw(fenster)
	
	pygame.display.flip()
	uhr.tick(30)