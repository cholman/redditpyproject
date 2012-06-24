import pygame, math
from pygame.locals import *


# calculate sin and cos to increase speed
SINTABLE = [math.sin(math.radians(angle)) for angle in xrange(360)]
COSTABLE = [math.cos(math.radians(angle)) for angle in xrange(360)]


class Bullet:
	def __init__(self, (initialX, initialY), angle):
		self.currentX = initialX
		self.currentY = initialY
		self.angle = angle
		self.length = 0

		
	def update(self, image, screen):
		self.currentX += -SINTABLE[int(self.angle)] * 10
		self.currentY += -COSTABLE[int(self.angle)] * 10
		screen.blit(image, (self.currentX, self.currentY))