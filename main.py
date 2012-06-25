import pygame, time, random
import terrain, sprites, biomes, movement, projectiles
from pygame.locals import *
pygame.display.init()


class main():
	def __init__(self):
		'''Load the game core game'''
		pygame.init
		self.Clock = pygame.time.Clock()
		self.width, self.height = (768, 768) 														# Screen width and height :: (Not changeable without having errors)
		self.dirtyRects = [] 
		self.screen = pygame.display.set_mode((self.width,self.height), RESIZABLE)						    # Setting up the window where the game will be displayed :: (Not changeable)
		self.gamestate = 'ingame' 																	# Determines in what game state the client starts
		self.mouseCoords = pygame.mouse.get_pos()													# Determines the initial mouse coordinates
		self.FPS = 75																					# Determines the max FPS the client can achieve :: (No point going over the screen refresh rate, but changeable)
		self.player = sprites.loadSprite("sprites/player.png")
		self.bullImage = sprites.loadSprite("sprites/bullet.png")
		
		
		
		
		
	def loadSprites(self):
		self.player = sprites.loadSprite("sprites/player.png")
		self.bullImage = sprites.loadSprite("sprites/bullet.png")
		
		
		
		
		
		
	def loadWorld(self):
		'''Load the game's world'''
		self.mapsize = 24																			# Determines the number of chunks per map side (mapsize*mapsize) is the world's number of chunks :: (Changeable)
		self.biomesize = 24																			# Determines the nubmer of tiles per map side (biomesize*biomesize) is the biome's number of tiles :: (Changeable but not bellow 24)
		self.world = biomes.generateWorld(self.mapsize, self.biomesize) 											# Generate a new world :: (Mapsize veriable is changeable, but not this)
		self.currentMap = (23, random.randint(0, self.mapsize-1))
		self.currentChunk = pygame.Surface((self.width, self.height))											# Create the surface where the chunk tiles being displayed will be stored :: (Not changeable)
		self.playerCoords = (self.width/2, self.height/2)														# Sets the initial player coordinate :: (Changeable, aslong as they are within the limits)
		self.biomes = terrain.biomes()																# The list of available types of biomes
		self.bullets = []																			# Set up a list that will contain the bullets
		self.currentX, self.currentY = self.currentMap
		terrain.drawMap(self.biomes, self.mapsize, self.world[self.currentX][self.currentY], self.currentChunk)
		terrain.drawChunk(self.screen, self.currentChunk)
		pygame.display.flip()
		self.fire = 0
		
		

	def updateIngame(self):
		self.anchorx, self.anchory = self.playerCoords
		self.playerCoords = movement.movePlayer(self.playerCoords)
		terrain.drawChunk(self.screen, self.currentChunk)
		self.mouseangle = sprites.calcAngleToMouse(self.mouseCoords, self.playerCoords)
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gamestate = 'quit'

					
				
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.gamestate = 'quit'
					
			elif event.type == MOUSEMOTION:
				self.mouseCoords = event.pos
						
		self.newplayer = self.player.rotCenter(self.mouseangle)
		self.keys = pygame.key.get_pressed()
		while len(self.dirtyRects) >= 2:
			self.dirtyRects.pop(0)
			
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_z]:
			self.fire = 1
			
		if self.fire == 1:
			if len(self.bullets) < 1:
				(initialX, initialY) = self.playerCoords
				initialX += 16
				initialY += 16
				bulletCoords = (initialX, initialY)
				self.bullets.append(projectiles.Bullet(bulletCoords, self.mouseangle))
			self.fire = 0
		
		
		
		
		if self.anchorx >= self.width -40:
			if self.currentX + 1 <= self.mapsize-1:
				for idx, bullet in enumerate(self.bullets):
					del self.bullets[idx]
				self.currentX+= 1
				self.currentMap = (self.currentX, self.currentY)
				self.playerCoords = (50, self.anchory)
				terrain.drawMap(self.biomes, self.mapsize, self.world[self.currentX][self.currentY], self.currentChunk)
				self.screen.blit(self.currentChunk, (0, 0))
				pygame.display.flip()
		
		if self.anchory >= self.height -40:
			if self.currentY + 1 <= self.mapsize-1:
				for idx, bullet in enumerate(self.bullets):
					del self.bullets[idx]
				self.currentY+= 1
				self.currentMap = (self.currentX, self.currentY)
				self.playerCoords = (self.anchorx, 50)
				terrain.drawMap(self.biomes, self.mapsize, self.world[self.currentX][self.currentY], self.currentChunk)
				self.screen.blit(self.currentChunk, (0, 0))
				pygame.display.flip()
			
		if self.anchorx <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
			if self.currentX - 1 >= 0:
				for idx, bullet in enumerate(self.bullets):
					del self.bullets[idx]
				self.currentX-= 1
				self.currentMap = (self.currentX, self.currentY)
				self.playerCoords = (self.width-41, self.anchory) # -k k has to be the same and up in >=
				terrain.drawMap(self.biomes, self.mapsize, self.world[self.currentX][self.currentY], self.currentChunk)
				self.screen.blit(self.currentChunk, (0, 0))
				pygame.display.flip()
			
		if self.anchory <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
			if self.currentY - 1 >= 0:
				for idx, bullet in enumerate(self.bullets):
					del self.bullets[idx]
				self.currentY-= 1
				self.currentMap = (self.currentX, self.currentY)
				self.playerCoords = (self.anchorx, self.height-41) # -k k has to be the same and up in >=
				terrain.drawMap(self.biomes, self.mapsize, self.world[self.currentX][self.currentY], self.currentChunk)
				self.screen.blit(self.currentChunk, (0, 0))
				pygame.display.flip()
		

			
			
		# Ignore this, just a placeholder to draw the map
		for idx, bullet in enumerate(self.bullets):
			bullCoords = (bullet.currentX, bullet.currentY)
			#terrain.updateMap(plains, world[currentX][currentY], screen, bullCoords)
			self.dirtyRects.append(pygame.Rect(bullet.currentX-16, bullet.currentY-16, 32, 32))
			bullet.length += 1
			if bullet.currentY >= self.width or bullet.currentY <= 16:
				del self.bullets[idx]

			if bullet.currentX >= self.width or bullet.currentX <= 16:
				del self.bullets[idx]
		
		for bullet in self.bullets:
			bullet.update(self.bullImage.sprite, self.screen)	
		self.screen.blit(self.newplayer, self.playerCoords)
		self.dirtyRects.append(pygame.Rect(self.anchorx, self.anchory, 32, 32))
		pygame.display.update(self.dirtyRects)
		self.fps = self.Clock.get_fps()
		self.Clock.tick(self.FPS)
		pygame.display.set_caption(str(self.fps)+" "+str(self.currentX) +"|" + str(self.currentY))
	


game = main()
if game.gamestate == 'ingame':
	game.loadSprites()
	game.loadWorld()
	
	while game.gamestate == 'ingame':
		game.updateIngame()
		