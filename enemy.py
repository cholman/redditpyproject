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
		
	def enemyAI(self, playerCoords, worldMap, smellRange=13, chaseRange=17, walkSpeed=2, chaseSpeed=3, mapsize=256):
		playerX, playerY = playerCoords
		# Determine wether the zombie should starting or stop chasing
		if (((self.currentX - playerX))**2)+((self.currentY - playerY))**2 < (smellRange*32)**2:
			self.chasingPlayer = True
		if (((self.currentX - playerX))**2)+((self.currentY - playerY))**2 > (chaseRange*32)**2:
			self.chasingPlayer = False
			
		if self.chasingPlayer == True:
			if self.currentX < playerX and self.currentX+chaseSpeed+32 < mapsize*32:
				if worldMap[(self.currentX+32+chaseSpeed)/32][(self.currentY+16)/32] == 'grass':
					self.currentX += chaseSpeed
			if self.currentY < playerY and self.currentY+chaseSpeed+32 < mapsize*32:
				if worldMap[(self.currentX+16)/32][(self.currentY+chaseSpeed+32)/32] == 'grass':
					self.currentY += chaseSpeed
			if self.currentX > playerX:
				if worldMap[(self.currentX-chaseSpeed)/32][(self.currentY+16)/32] == 'grass':
					self.currentX -= chaseSpeed
			if self.currentY > playerY:
				if worldMap[(self.currentX+16)/32][(self.currentY-chaseSpeed)/32] == 'grass':
					self.currentY -= chaseSpeed
		anchorX, anchorY = (playerX-768/2, playerY-768/2)
		if self.inScreen == True:
			self.angle = sprites.calcAngleToMouse((playerX, playerY), (self.currentX, self.currentY))
			self.sprite.spriteRot = self.sprite.rotCenter(self.angle)
		self.inScreen = False

		
		if -32 < self.currentX - anchorX < 768 and -32 < self.currentY - anchorY < 768:
			self.inScreenX = self.currentX - anchorX
			self.inScreenY = self.currentY - anchorY
			self.inScreen = True
			
	def update(self, surface):
		if self.inScreen == True:
			surface.blit(self.sprite.spriteRot, (self.inScreenX, self.inScreenY))
			surface.blit(self.hpBar,(self.inScreenX-9, self.inScreenY-15))
		self.hpBar.fill((0,0,0))
		pygame.draw.rect(self.hpBar, (255, 0, 0), (-1, 0, self.health/2, 5))
		
		
		