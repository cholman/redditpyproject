import random

# Plains (Grass, Water, Tree)

def generateBiome(biomeType='plains', size=10, frequencies=[3, 1, 1]):
	print('gotcha')
	biome = [['grass' for x in range(size)] for y in range(size)]
	if biomeType == 'plains':
		tiles = []
		if frequencies[0] != 0:
			for times in range(0, frequencies[0]):
				tiles.append('grass')
		if frequencies[1] != 0:
			for times in range(0, frequencies[1]):
				tiles.append('water')
		if frequencies[2] != 0:
			for times in range(0, frequencies[2]):
				tiles.append('tree')
		
		for x in range (0, size):
			for y in range (0, size):
				biome[x][y] = tiles[random.randint(0,len(tiles)-1)]

	return biome
		
def generateWorld(mapsize):
	world = [[None]*mapsize]*mapsize 
	frequencies = [5, 1, 3]
	for x in range(0, mapsize):
		for y in range(0, mapsize):
			world[x][y] = generateBiome('plains', mapsize, frequencies)
	
	return world