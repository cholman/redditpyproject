import pygame
import random, math, sprites, time, movement, timedevents
from pygame.locals import *

# calculate sin and cos to increase speed
SINTABLE = [math.sin(math.radians(angle)) for angle in xrange(360)]
COSTABLE = [math.cos(math.radians(angle)) for angle in xrange(360)]



# Control Something based on time (do a task every N seconds)
class zombie:
	def __init__(self, world, mapsize, sprite):
		self.sprite = sprite
		self.currentX, self.currentY = movement.generateLocation(world, mapsize)
		self.chasingPlayer = False
		self.angle = 0
		self.inScreen = False
		self.health = 100
		self.hpBar = pygame.Surface((50, 5))
		pygame.draw.rect(self.hpBar, (255, 0, 0), (-1, 0, self.health/2, 5))
		self.attackSpeed = timedevents.vars(1)
		self.sprite.spriteRot = self.sprite.rotCenter(self.angle)
		
	def normalizeVector(self, playerCoords):
		playerX, playerY = playerCoords
		vectorLength = math.sqrt((playerX-self.currentX)**2 + (playerY-self.currentY)**2)
		xLength = math.fabs(playerX - self.currentX)
		yLength = math.fabs(playerY - self.currentY)
		xNorm = 0
		yNorm = 0
		if xLength != 0:
			xNorm = xLength / vectorLength
		if yLength != 0:
			yNorm = yLength / vectorLength
		return xNorm, yNorm
	
	
	def enemyAI(self, playerCoords, worldMap, smellRange=13, chaseRange=17, walkSpeed=2, chaseSpeed=3, mapsize=256):
		playerX, playerY = playerCoords
		# Determine wether the zombie should starting or stop chasing
		if (((self.currentX - playerX))**2)+((self.currentY - playerY))**2 < (smellRange*32)**2:
			self.chasingPlayer = True
		if (((self.currentX - playerX))**2)+((self.currentY - playerY))**2 > (chaseRange*32)**2:
			self.chasingPlayer = False
			
		if self.chasingPlayer == True:
			xSpeed, ySpeed = self.normalizeVector(playerCoords)
			xSpeed = xSpeed * chaseSpeed
			ySpeed = ySpeed * chaseSpeed
			if self.currentX < playerX and self.currentX+xSpeed+32 < mapsize*32:
				if worldMap[int((self.currentX+32+xSpeed)/32)][int((self.currentY+16)/32)] == 'grass':
					self.currentX += xSpeed
			if self.currentY < playerY and self.currentY+ySpeed+32 < mapsize*32:
				if worldMap[int((self.currentX+16)/32)][int((self.currentY+ySpeed+32)/32)] == 'grass':
					self.currentY += ySpeed
			if self.currentX > playerX:
				if worldMap[int((self.currentX-xSpeed)/32)][int((self.currentY+16)/32)] == 'grass':
					self.currentX -= xSpeed
			if self.currentY > playerY:
				if worldMap[int((self.currentX+16)/32)][int((self.currentY-ySpeed)/32)] == 'grass':
					self.currentY -= ySpeed
		anchorX, anchorY = (playerX-768/2, playerY-768/2)
		if self.inScreen == True:
			self.angle = sprites.calcAngleToMouse((playerX, playerY), (self.currentX, self.currentY))
			self.sprite.spriteRot = self.sprite.rotCenter(self.angle)
		self.inScreen = False

		
		if -32 < self.currentX - anchorX < 768 and -32 < self.currentY - anchorY < 768:
			self.inScreenX = self.currentX - anchorX
			self.inScreenY = self.currentY - anchorY
			self.inScreen = True
			
	def update(self):
		
		self.hpBar.fill((0,0,0))
		pygame.draw.rect(self.hpBar, (255, 0, 0), (-1, 0, self.health/2, 5))
	
	def draw(self, surface):
		if self.inScreen == True:
			surface.blit(self.sprite.spriteRot, (self.inScreenX, self.inScreenY))
			surface.blit(self.hpBar,(self.inScreenX-9, self.inScreenY-15))
		
		