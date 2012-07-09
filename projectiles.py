import pygame, math, sprites
from pygame.locals import *


# calculate sin and cos to increase speed
SINTABLE = [math.sin(math.radians(angle)) for angle in xrange(360)]
COSTABLE = [math.cos(math.radians(angle)) for angle in xrange(360)]


class Bullet:
	def __init__(self, playerCoords, velocity = 10):
		self.sprite = sprites.loadSprite("sprites/bullet.png")
		playerX, playerY = playerCoords
		self.currentX, self.currentY = playerX+16, playerY+16
		self.inScreenX = 768/2
		self.inScreenY = 768/2
		self.length = 0
		self.bulletDamage = 5
		self.inScreen = True
		self.velocity = 10
		self.determinedPath = 0
		
	def normalizeVector(self, mouseCoords, anchorX, anchorY):
		mouseX, mouseY = mouseCoords
		mouseX, mouseY = anchorX+mouseX, anchorY+mouseY
		vectorLength = math.sqrt((mouseX-self.currentX)**2 + (mouseY-self.currentY)**2)
		xLength = mouseX - self.currentX
		yLength = mouseY - self.currentY
		xNorm = 0
		yNorm = 0
		if xLength != 0:
			xNorm = xLength / vectorLength
		if yLength != 0:
			yNorm = yLength / vectorLength
		return xNorm, yNorm
		
		
	def update(self, playerCoords, mouseCoords):
		playerX, playerY = playerCoords
		anchorX, anchorY = (playerX-768/2, playerY-768/2)
		if self.determinedPath == 0:
			self.xSpeed, self.ySpeed = self.normalizeVector(mouseCoords, anchorX, anchorY)
			self.xSpeed = self.xSpeed * self.velocity
			self.ySpeed = self.ySpeed * self.velocity
			self.determinedPath = 1
		if self.determinedPath == 1:
			self.currentX += self.xSpeed
			self.currentY += self.ySpeed

		self.inScreen = False

		if 5 < self.currentX - anchorX < 768 and 5 < self.currentY - anchorY < 768:
			self.inScreen = True
			self.inScreenX = self.currentX - anchorX
			self.inScreenY = self.currentY - anchorY
			
	def draw(self, screen):
		if self.inScreen:
			screen.blit(self.sprite.sprite, (self.inScreenX, self.inScreenY))
			
		