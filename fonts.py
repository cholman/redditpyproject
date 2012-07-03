import pygame
pygame.font.init()


class UI:
	def __init__(self):
		self.size = 20
		self.anonymousPro = pygame.font.Font('AnonymousPro.ttf', self.size)
		self.strings = {}
		self.strings['hp'] = 'Hitpoints'
		self.strings['notar'] = 'NO TARGET'
		self.strings['dead'] = 'YOU ARE DEAD... GAME WILL RESTART IN 5 SECONDS...'
		
		self.images = {}
		for string in self.strings:
			self.images[string] = self.anonymousPro.render(self.strings[string], 1, (153, 131, 67))
