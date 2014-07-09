import pygame, sys
from pygame.locals import *

class GUI(object):
	def __init__(self):
		pygame.init()

	def start(self):
		self.clock = pygame.time.Clock()
		self.window = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("R")

		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			self.clock.tick(20)
				