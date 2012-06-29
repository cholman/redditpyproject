import random
# Plains (Grass, Water, Tree)

def generateMap(biomeType='plains', size=256, frequencies=2, nodeSize=5):
	biome = [['grass' for x in range(size)] for y in range(size)]
	
		
	for times in range (0, ((size/24)**2)*frequencies): # Place the water fountains which will be the center of each lake
		x = random.randint(nodeSize, size-nodeSize)
		y = random.randint(nodeSize, size-nodeSize)
		biome[x][y] = 'waterSource'
		
	for times in range (0, ((size/24)**2)*frequencies): # Place the tree which will be the center of each forest
		x = random.randint(nodeSize, size-nodeSize)
		y = random.randint(nodeSize, size-nodeSize)
		biome[x][y] = 'forestSource'
		
	biomeCopy = biome
	
	for x in range (0, size-1):
		for y in range (0, size-1):
			if biome[x][y] == 'waterSource':
				for idX in range(-nodeSize, nodeSize):
					for idY in range(-nodeSize, nodeSize):
						if ((idX)**2)+((idY)**2) < nodeSize**2:
							biome[x-idX][y-idY] = 'water'
			if biome[x][y] == 'forestSource':
				for idX in range(-nodeSize, nodeSize):
					for idY in range(-nodeSize, nodeSize):
						if ((idX)**2)+((idY)**2) < nodeSize**2:
							biome[x-idX][y-idY] = 'tree'
							
	return biomeCopy