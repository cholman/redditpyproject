import pygame, random
from pygame.locals import *


def movePlayer(coords, mapsize, worldMap, speed=3, screenxy=(768, 768)):
	playerX, playerY = coords
	screenX, screenY = screenxy
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w]:
		if playerY > 0:
			if worldMap[(playerX+16)/32][(playerY-speed)/32] == 'grass':
				playerY -= speed
	if keys[pygame.K_s]:
		if playerY < 32*(mapsize-1):
			if playerY+speed+32 < mapsize*32:
				if worldMap[(playerX+16)/32][(playerY+speed+32)/32] == 'grass':
					playerY += speed
	if keys[pygame.K_d]:
		if playerX < 32*(mapsize-1):
			if playerX+speed+32 < mapsize*32:
				if worldMap[(playerX+speed+32)/32][(playerY+16)/32] == 'grass':
					playerX += speed
	elif keys[pygame.K_a]:
		if playerX > 0:
			if worldMap[(playerX-speed)/32][(playerY+16)/32] == 'grass':
				playerX -= speed
		
		
	newCoords = (playerX, playerY)
	return newCoords
		
def generateLocation(world, mapsize):
	locX, locY = (random.randint(0,(mapsize-1)*32),random.randint(0,(mapsize-1)*32))
	while world[locX/32][locY/32] != 'grass':
		locX, locY = (random.randint(0,(mapsize-1)*32-16),random.randint(0,(mapsize-1)*32-16))

	return (locX, locY)
	
def colision(obj1, obj1Mid, obj2, obj2Mid, range):
	if (((obj1.currentX + obj1Mid - obj2.currentX + obj2Mid))**2)+((obj1.currentY +obj1Mid - obj2.currentY + obj2Mid))**2 <= (range)**2:
		return True
	else:
		return False