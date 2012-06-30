import pygame, math, sprites
from pygame.locals import *


# calculate sin and cos to increase speed
SINTABLE = [math.sin(math.radians(angle)) for angle in xrange(360)]
COSTABLE = [math.cos(math.radians(angle)) for angle in xrange(360)]


class Bullet:
	def __init__(self, playerCoords, angle):
		self.sprite = sprites.loadSprite("sprites/bullet.png")
		playerX, playerY = playerCoords
		self.currentX, self.currentY = playerX+16, playerY+16
		self.inScreenX = 768/2
		self.inScreenY = 768/2
		self.angle = angle
		self.length = 0
		self.bulletDamage = 5
		self.inScreen = True
		self.sprite.spriteRot = self.sprite.rotCenter(self.angle)
		
	def update(self, screen, playerCoords):
		self.currentX += -SINTABLE[int(self.angle)] * 10
		self.currentY += -COSTABLE[int(self.angle)] * 10
		playerX, playerY = playerCoords
		anchorX, anchorY = (playerX-768/2, playerY-768/2)
		self.inScreen = False

		if 5 < self.currentX - anchorX < 768 and 5 < self.currentY - anchorY < 768:
			self.inScreen = True
			self.inScreenX = self.currentX - anchorX
			self.inScreenY = self.currentY - anchorY
		if self.inScreen:
			screen.blit(self.sprite.spriteRot, (self.inScreenX, self.inScreenY))