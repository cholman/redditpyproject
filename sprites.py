import pygame, math
from pygame.locals import *


class loadSprite():
	'''This should be where the sprite is processed into a pygame usable 
	image and a couple other functions we might use related to sprites aswell'''
	def __init__(self, spriteImagePath):
		'''Initial atributes of the the image'''
		self.sprite = pygame.image.load(spriteImagePath).convert()
		self.sprite.set_colorkey((255,0,255))

	def rotCenter(self, angle):
		'''rotate the sprite while keeping its center and size'''
		orig_rect = self.sprite.get_rect()
		rot_image = pygame.transform.rotate(self.sprite, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		return rot_image
	

def calcAngleToMouse(mousex, mousey, anchor):
	x, y = anchor
	mouseangle = 0
	if x >= mousex:
		mouseangle = math.degrees(math.atan2((mousey - y), (x - mousex)) / math.pi * 2.0)
            
	if x < mousex:
		mouseangle = math.degrees(math.atan2((mousey - y), (x - mousex)) / math.pi * 3.0)
		
	if mouseangle > 360:
		moueangle = mouseangle - 360
		
	mouseangle += 90
	return mouseangle
