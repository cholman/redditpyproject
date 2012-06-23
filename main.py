import pygame, time
import terrain, sprites, biomes, movement
from pygame.locals import *
pygame.init()
Clock = pygame.time.Clock()



# Initiate modules, set the screen and get its size
pygame.init
width, height = (768, 768) # Placeholder, change to what your confortable with
screen = pygame.display.set_mode((width,height), RESIZABLE)
playgame = True
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

	


pygame.display.flip()
currentMap = (1, 1)
currentX, currentY = currentMap
terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
pygame.display.flip()
while playgame == True: # Game loop
	anchorx, anchory = playerCoords
	playerCoords = movement.movePlayer(playerCoords)
	
	currentX, currentY = currentMap
	terrain.updateMap(plains, world[currentX][currentY], screen, playerCoords)

	
	mouseangle = sprites.calcAngleToMouse(mousex, mousey, playerCoords)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			playgame = False

				
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				playgame = False
				
		elif event.type == MOUSEMOTION:
			mousex, mousey = event.pos
					
	newplayer = player.rotCenter(mouseangle)
	if len(dirty_rects) >= 2:
		dirty_rects.pop(0)
		
		
		
	#Ignore Just to select the current map
	if anchorx >= width -40:
		currentX+= 1
		currentMap = (currentX, currentY)
		playerCoords = (50, anchory)
		terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
		pygame.display.flip()
		
	if anchory >= height -40:
		currentY+= 1
		currentMap = (currentX, currentY)
		playerCoords = (anchorx, 50)
		terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
		pygame.display.flip()
	

		
		
	# Ignore this, just a placeholder to draw the map
	
	screen.blit(newplayer, playerCoords)
	dirty_rects.append(pygame.Rect(anchorx, anchory, 32, 32))
	pygame.display.update(dirty_rects)
	fps = Clock.get_fps()
	Clock.tick(FPS)
	pygame.display.set_caption(str(fps)+" "+str(currentX) +"|" + str(currentY))
	#print(str(currentX)+str(currentY))
	if world[0][1] == world[1][1]:
		print('True')
 # Test
