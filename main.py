import pygame, time, random
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
currentMap = (23, random.randint(0, mapsize-1))
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
		if currentX + 1 <= mapsize-1:
			currentX+= 1
			currentMap = (currentX, currentY)
			playerCoords = (50, anchory)
			terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
			pygame.display.flip()
		
	if anchory >= height -40:
		if currentY + 1 <= mapsize-1:
			currentY+= 1
			currentMap = (currentX, currentY)
			playerCoords = (anchorx, 50)
			terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
			pygame.display.flip()
		
	if anchorx <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
		if currentX - 1 >= 0:
			currentX-= 1
			currentMap = (currentX, currentY)
			playerCoords = (width-41, anchory) # -k k has to be the same and up in >=
			terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
			pygame.display.flip()
		
	if anchory <= 5: # Grace 5 pix to let the player swap maps / Change later according to speed
		if currentY - 1 >= 0:
			currentY-= 1
			currentMap = (currentX, currentY)
			playerCoords = (anchorx, height-41) # -k k has to be the same and up in >=
			terrain.drawMap(plains, mapsize, world[currentX][currentY], screen)
			pygame.display.flip()
	

		
		
	# Ignore this, just a placeholder to draw the map
	
	screen.blit(newplayer, playerCoords)
	dirty_rects.append(pygame.Rect(anchorx, anchory, 32, 32))
	pygame.display.update(dirty_rects)
	fps = Clock.get_fps()
	Clock.tick(FPS)
	pygame.display.set_caption(str(fps)+" "+str(currentX) +"|" + str(currentY))
	
 # Test
