import pygame, time, random
import terrain, sprites, biomes, movement, projectiles, enemy, math
from pygame.locals import *
pygame.display.init()


class main():
	def __init__(self):
		'''Load the game core game'''
		pygame.init
		self.Clock = pygame.time.Clock()
		self.width, self.height = (968, 768) 														# Screen width and height :: (Not changeable without having errors)
		self.screen = pygame.display.set_mode((self.width,self.height), RESIZABLE)						    # Setting up the window where the game will be displayed :: (Not changeable)
		self.gamestate = 'ingame' 																	# Determines in what game state the client starts
		self.mouseCoords = pygame.mouse.get_pos()													# Determines the initial mouse coordinates
		self.FPS = 75																					# Determines the max FPS the client can achieve :: (No point going over the screen refresh rate, but changeable)
		self.player = sprites.loadSprite("sprites/player.png")
		self.bullImage = sprites.loadSprite("sprites/bullet.png")
		
		
		
		
		
	def loadSprites(self):
		self.player = sprites.loadSprite("sprites/player.png")
		self.bullImage = sprites.loadSprite("sprites/bullet.png")
		
	def loadUI(self):
		self.currentUI = pygame.Surface((200, 768))	
		self.uiBackground = sprites.loadSprite("sprites/uibackground.png")
		self.currentUI.blit(self.uiBackground.sprite, (0,0))
		
		
		
		
		
	def loadWorld(self):
		'''Load the game's world'''
		self.mapsize = 256																			# Determines the number of chunks per map side (mapsize*mapsize) is the world's number of tiles :: (Changeable)
		self.world = biomes.generateMap() 															# Generate a new world :: (Mapsize veriable is changeable, but not this)
		self.currentChunk = pygame.Surface((32*self.mapsize, 32*self.mapsize))					    # Create the surface where the chunk tiles being displayed will be stored :: (Not changeable)
		self.playerCoords = movement.generateLocation(self.world, self.mapsize)			# Sets the initial player coordinate :: (Changeable, aslong as they are within the limits)
		self.zombie = enemy.zombie(movement.generateLocation(self.world, self.mapsize))#self.playerCoords)
		self.biomes = terrain.biomes()																# The list of available types of biomes
		self.bullets = []																			# Set up a list that will contain the bullets
		self.zombies = []
		terrain.blitMap(self.biomes, self.mapsize, self.world, self.currentChunk)
		terrain.drawMap(self.screen, self.currentChunk, (0,0))
		self.midCoords = ((self.width-200)/2, self.height/2)
		pygame.display.flip()
		self.fire = 0

		
		

	def updateIngame(self):
		self.screen.fill((0,0,0))
		self.anchorx, self.anchory = self.playerCoords
		self.zombie.enemyAI(self.playerCoords, self.world)
		self.playerCoords = movement.movePlayer(self.playerCoords, self.mapsize, self.world)
		terrain.drawMap(self.screen, self.currentChunk, self.playerCoords)
		self.mouseangle = sprites.calcAngleToMouse(self.mouseCoords, self.midCoords)
		
		
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
			
		self.keys = pygame.key.get_pressed()
		if self.keys[pygame.K_z]:
			self.fire = 1
			
		if self.fire == 1:
			if len(self.bullets) < 1:
				(initialX, initialY) = self.midCoords
				initialX += 16
				initialY += 16
				bulletCoords = (initialX, initialY)
				self.bullets.append(projectiles.Bullet(bulletCoords, self.mouseangle))
			self.fire = 0
		

			
			
		for idx, bullet in enumerate(self.bullets):
			bullCoords = (bullet.currentX, bullet.currentY)
			bullet.length += 1
			if bullet.currentY >= self.width or bullet.currentY <= 16:
				del self.bullets[idx]
				continue

			if bullet.currentX >= self.width or bullet.currentX <= 16:
				del self.bullets[idx]
		
		for bullet in self.bullets:
			bullet.update(self.bullImage.sprite, self.screen)	
		self.screen.blit(self.newplayer, self.midCoords)
		self.zombie.update(self.screen)
		self.screen.blit(self.currentUI, (768, 0))
		self.fps = self.Clock.get_fps()
		self.Clock.tick(self.FPS)
		playerX, playerY = self.playerCoords
		caption = 'Fps: ' + str(math.floor(self.fps)) + ' | Player:(' + str(playerX/32) + ',' + str(playerY/32) + ')  | Zombie:(' + str(self.zombie.currentX/32) + ',' + str(self.zombie.currentY/32) + ') |  Chasing: ' + str(self.zombie.chasingPlayer)
		pygame.display.set_caption(caption)
		pygame.display.flip()
	


game = main()
if game.gamestate == 'ingame':
	game.loadUI()
	game.loadSprites()
	game.loadWorld()
	
	while game.gamestate == 'ingame':
		game.updateIngame()
		