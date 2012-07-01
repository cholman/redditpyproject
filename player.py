import pygame
import random, sprites, movement
from pygame.locals import *




# Control Something based on time (do a task every N seconds)
class player:
	def __init__(self, world, mapsize):
		self.sprite = sprites.loadSprite("sprites/player.png")
		self.health = 100
		self.playerCoords = movement.generateLocation(world, mapsize)
		self.currentX, self.currentY = self.playerCoords
		self.hpBar = pygame.Surface((100, 10))
		pygame.draw.rect(self.hpBar, (255, 0, 0), (-1, 0, self.health, 10))
		self.lastHit = -1
		
	def update(self):
		self.hpBar.fill((0,0,0))
		pygame.draw.rect(self.hpBar, (255, 0, 0), (-1, 0, self.health, 10))
		