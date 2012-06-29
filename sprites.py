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
	

def calcAngleToMouse((mousex, mousey), anchor):
	x, y = anchor
	mouseangle = 0
	if x >= mousex:
		mouseangle = math.degrees(float(math.atan2((mousey - y), (x - mousex))))
   	
	if x < mousex:
		mouseangle = math.degrees(float(math.atan2((mousey - y), (x - mousex))))
		
	mouseangle += 90
	return mouseangle
	

