import pygame
from pygame.locals import *


def movePlayer(coords, mapsize, speed=2, screenxy=(768, 768)):
	playerX, playerY = coords
	screenX, screenY = screenxy
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w]:
		if playerY > 0:
			playerY -= speed
	if keys[pygame.K_s]:
		if playerY < 32*(mapsize-1):
			playerY += speed
	if keys[pygame.K_d]:
		if playerX < 32*(mapsize-1):
			playerX += speed
	elif keys[pygame.K_a]:
		if playerX > 0:
			playerX -= speed
		
		
	newCoords = (playerX, playerY)
	return newCoords
		