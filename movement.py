import pygame
from pygame.locals import *


def movePlayer(coords, speed=2, screenxy=(768, 768)):
	playerX, playerY = coords
	screenX, screenY = screenxy
	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w]:
		playerY -= speed
	if keys[pygame.K_s]:
		playerY += speed
	if keys[pygame.K_a]:
		playerX -= speed
	elif keys[pygame.K_d]:
		playerX += speed
		
	if playerX >= screenX - 32 or playerX <= 0:
		playerX, playerY = coords
	
	if playerY >= screenY - 32 or playerY <= 0:
		playerX, playerY = coords
		
	newCoords = (playerX, playerY)
	return newCoords
		