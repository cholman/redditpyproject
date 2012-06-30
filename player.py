import pygame
import random, sprites, movement
from pygame.locals import *




# Control Something based on time (do a task every N seconds)
class player:
	def __init__(self, world, mapsize):
		self.sprite = sprites.loadSprite("sprites/player.png")
		self.playerCoords = movement.generateLocation(world, mapsize)
		