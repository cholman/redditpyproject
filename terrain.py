import pygame, math
from pygame.locals import *
pygame.display.init()

class loadTile():
	'''This should be where the tile is processed into a pygame usable 
	image and a couple other functions we might use related to tiles aswell'''
	def __init__(self, tileImagePath):
		'''Initial atributes of the the image'''
		self.sprite = pygame.image.load(tileImagePath).convert()
		self.sprite.set_colorkey((255,0,255))
		
class biomes():
	'''Contains all the biomes, which are the classes bellow, and each of the tiles in each biome'''
	def __init__(self):
		self.grass = loadTile("sprites/grass.png")
		self.tree = loadTile("sprites/tree.png")
		self.water = loadTile("sprites/water.png")	
	

def blitMap(tiles, mapsize, chunk, screen):
	for xtile in range(0, mapsize): # 
		for ytile in range(0, mapsize):
			if chunk[xtile][ytile] == 'grass':
				screen.blit(tiles.grass.sprite, (xtile*32, ytile*32))
			
			if chunk[xtile][ytile] == 'water':
				screen.blit(tiles.water.sprite, (xtile*32, ytile*32))
				
			if chunk[xtile][ytile] == 'tree':
				screen.blit(tiles.tree.sprite, (xtile*32, ytile*32))

				
def drawMap(surface, chunk, playerCoords):
	playerX, playerY = playerCoords
	surface.blit(chunk, (0-playerX+384, 0-playerY+384))