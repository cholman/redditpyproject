import pygame, time, random, sys
import terrain, sprites, biomes, movement, projectiles, enemy, math, timedevents, player
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
		self.bullImage = sprites.loadSprite("sprites/bullet.png")
		
		
		
		
	# Loading Functions :: Where the starting objects should be loaded.	
	def loadFont(self)
	def loadUI(self):
		self.currentUI = pygame.Surface((200, 768))	
		self.uiBackground = sprites.loadSprite("sprites/uibackground.png")
		self.currentUI.blit(self.uiBackground.sprite, (0,0))
		
	def loadWorld(self):
		'''Load the game's world'''
		
		self.mapsize = 256																			# Determines the number of chunks per map side (mapsize*mapsize) is the world's number of tiles :: (Changeable)
		self.world = biomes.generateMap() 															# Generate a new world :: (Mapsize veriable is changeable, but not this)
		self.currentChunk = pygame.Surface((32*self.mapsize, 32*self.mapsize))					    # Create the surface where the chunk tiles being displayed will be stored :: (Not changeable)
		self.zombieSpawner = timedevents.vars(2)
		self.player = player.player(self.world, self.mapsize)
		self.zombieSpawner.doFunction(enemy.zombie, self.world, self.mapsize)
		self.biomes = terrain.biomes()																# The list of available types of biomes
		self.bullets = []																			# Set up a list that will contain the bullets
		self.zombies = []
		terrain.blitMap(self.biomes, self.mapsize, self.world, self.currentChunk)
		terrain.drawMap(self.screen, self.currentChunk, (0,0))
		self.midCoords = ((self.width-200)/2, self.height/2)
		pygame.display.flip()
		self.firingTimer = timedevents.vars(0.2)
		
		
		
		
		
		
	# Updating Funtions :: Where the update of each seperate game component should be updated (UI, AI'S)
	
	def updateIngame(self):
	
		if  self.zombieSpawner.determineTF() and len(self.zombies) < 50:
			self.zombies.append(self.zombieSpawner.doFunction(enemy.zombie, self.world, self.mapsize))
		self.screen.fill((0,0,0))
		self.anchorx, self.anchory = self.player.playerCoords
		for zombie in self.zombies:
			zombie.enemyAI(self.player.playerCoords, self.world)
		self.player.playerCoords = movement.movePlayer(self.player.playerCoords, self.mapsize, self.world)
		terrain.drawMap(self.screen, self.currentChunk, self.player.playerCoords)
		self.mouseangle = sprites.calcAngleToMouse(self.mouseCoords, self.midCoords)
		
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.gamestate = 'quit'
		
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					self.gamestate = 'quit'
					
			elif event.type == MOUSEMOTION:
				self.mouseCoords = event.pos
						
		self.newplayer = self.player.sprite.rotCenter(self.mouseangle)
			
		self.keys = pygame.key.get_pressed()
		(button1, button2, button3) = pygame.mouse.get_pressed()
		if button1 == 1:
			if self.firingTimer.determineTF():
				self.bullets.append(projectiles.Bullet(self.player.playerCoords, self.mouseangle))
		

		for bullet in self.bullets:
			bullet.update(self.screen, self.player.playerCoords)		
			
		for idx, bullet in enumerate(self.bullets):
			if bullet.inScreen == False:
				del self.bullets[idx]

		

		self.screen.blit(self.newplayer, self.midCoords)
		for zombie in self.zombies:
			zombie.update(self.screen)
		self.screen.blit(self.currentUI, (768, 0))
		self.fps = self.Clock.get_fps()
		self.Clock.tick(self.FPS)
		caption = 'Fps: ' + str(math.floor(self.fps)) + ' | Player:(' + str(self.anchorx/32) + ',' + str(self.anchory/32) + ')  | ZombieCount ' + str(len(self.zombies)) + ' | Firing speed: ' + str(self.firingTimer.seconds)
		pygame.display.set_caption(caption)
		pygame.display.flip()
	
	def updateUI(self):
		pass


		
		
		
		
		
# Game Sequence / Loop:
		
game = main()
if game.gamestate == 'ingame':
	game.loadUI()
	game.loadWorld()
	
	
	while game.gamestate == 'ingame':
		game.updateIngame()
		