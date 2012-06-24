import pygame, time, random
import terrain, sprites, biomes, movement, projectiles
from pygame.locals import *
pygame.init()
Clock = pygame.time.Clock()



# Initiate modules, set the screen and get its size
pygame.init
width, height = (768, 768) # Placeholder, change to what your confortable with
currentChunk = pygame.Surface((width, height))
screen = pygame.display.set_mode((width,height), RESIZABLE)
gamestate = 'ingame'
mousex, mousey = pygame.mouse.get_pos()
playerCoords = (width/2, height/2)
FPS = 75
#Test Area: (Ignore)
class plains():
	grass = terrain.loadTile("sprites/grass.png")
	tree = terrain.loadTile("sprites/tree.png")
	water = terrain.loadTile("sprites/water.png")
dirty_rects = []
mapsize = 24
player = sprites.loadSprite("sprites/player.png")
world = biomes.generateWorld(mapsize) #Problem with this atm - X's are diferent but not Y's...
bullImage = sprites.loadSprite("sprites/bullet.png")
bullets = []



pygame.display.flip()
currentMap = (23, random.randint(0, mapsize-1))
currentX, currentY = currentMap
terrain.drawMap(plains, mapsize, world[currentX][currentY], currentChunk)
terrain.drawChunk(screen, currentChunk)
pygame.display.flip()
fire = 0

while gamestate == 'ingame': # Game loop
	anchorx, anchory = playerCoords
	playerCoords = movement.movePlayer(playerCoords)
	terrain.drawChunk(screen, currentChunk)
	currentX, currentY = currentMap

	
	mouseangle = sprites.calcAngleToMouse(mousex, mousey, playerCoords)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			gamestate = 'quit'

				
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				gamestate = 'quit'
				
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
					
	newplayer = player.rotCenter(mouseangle)
	keys = pygame.key.get_pressed()
	while len(dirty_rects) >= 2:
		dirty_rects.pop(0)
		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_z]:
		fire = 1
		
	if fire == 1:
		if len(bullets) < 1:
			(initialX, initialY) = playerCoords
			initialX += 16
			initialY += 16
			bulletCoords = (initialX, initialY)
			bullets.append(projectiles.Bullet(bulletCoords, mouseangle))
		fire = 0
		
	#Ignore Just to select the current map
	if anchorx >= width -40:
		if currentX + 1 <= mapsize-1:
			for idx, bullet in enumerate(bullets):
				del bullets[idx]
			currentX+= 1
			currentMap = (currentX, currentY)
			playerCoords = (50, anchory)
			terrain.drawMap(plains, mapsize, world[currentX][currentY], currentChunk)
			screen.blit(currentChunk, (0, 0))
			pygame.display.flip()
		
	if anchory >= height -40:
		if currentY + 1 <= mapsize-1:
			for idx, bullet in enumerate(bullets):
				del bullets[idx]
			currentY+= 1
			currentMap = (currentX, currentY)
			playerCoords = (anchorx, 50)
			terrain.drawMap(plains, mapsize, world[currentX][currentY], currentChunk)
			screen.blit(currentChunk, (0, 0))
			pygame.display.flip()
		
	if anchorx <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
		if currentX - 1 >= 0:
			for idx, bullet in enumerate(bullets):
				del bullets[idx]
			currentX-= 1
			currentMap = (currentX, currentY)
			playerCoords = (width-41, anchory) # -k k has to be the same and up in >=
			terrain.drawMap(plains, mapsize, world[currentX][currentY], currentChunk)
			screen.blit(currentChunk, (0, 0))
			pygame.display.flip()
		
	if anchory <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
		if currentY - 1 >= 0:
			for idx, bullet in enumerate(bullets):
				del bullets[idx]
			currentY-= 1
			currentMap = (currentX, currentY)
			playerCoords = (anchorx, height-41) # -k k has to be the same and up in >=
			terrain.drawMap(plains, mapsize, world[currentX][currentY], currentChunk)
			screen.blit(currentChunk, (0, 0))
			pygame.display.flip()
	

		
		
	# Ignore this, just a placeholder to draw the map
	for idx, bullet in enumerate(bullets):
		bullCoords = (bullet.currentX, bullet.currentY)
		#terrain.updateMap(plains, world[currentX][currentY], screen, bullCoords)
		dirty_rects.append(pygame.Rect(bullet.currentX-16, bullet.currentY-16, 32, 32))
		bullet.length += 1
		if bullet.currentY >= width or bullet.currentY <= 16:
			del bullets[idx]

		if bullet.currentX >= width or bullet.currentX <= 16:
			del bullets[idx]
	
	for bullet in bullets:
		bullet.update(bullImage.sprite, screen)	
	screen.blit(newplayer, playerCoords)
	dirty_rects.append(pygame.Rect(anchorx, anchory, 32, 32))
	pygame.display.update(dirty_rects)
	fps = Clock.get_fps()
	Clock.tick(FPS)
	pygame.display.set_caption(str(fps)+" "+str(currentX) +"|" + str(currentY))
	
 # Test
