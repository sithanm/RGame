import pygame, sys, os
from pygame.locals import *
import Player

class GUI(object):
	def __init__(self):
		pygame.init()
		self.load_images()
		self.player = Player.Player(100, 100)


	def load_images(self):
		self.img_player = []
		for i in ["R_0.png", "R_1.png", "R_2.png", "R_3.png", "R_4.png", "R_5.png"]:
			self.img_player += [pygame.image.load(os.path.join("GUI", "images", i))]

	def start(self):
		self.clock = pygame.time.Clock()
		self.window = pygame.display.set_mode((640, 480))
		pygame.display.set_caption("R")

		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT:
						self.player.rightKeyPressed()
					elif event.key == K_LEFT:
						self.player.leftKeyPressed()
				elif event.type == KEYUP:
					if event.key == K_RIGHT:
						self.player.rightKeyReleased()
					elif event.key == K_LEFT:
						self.player.leftKeyReleased()

			self.player.step()
			#draw player
			img = self.player.get_img_ID()
			self.window.blit(self.img_player[img], self.player.get_Pos())

			pygame.display.update()
			self.clock.tick(20)
				