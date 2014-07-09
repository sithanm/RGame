import os
import Block

def pixel_to_block((x, y)):
	return (x//32, y//32)

class Map(object):
	def __init__(self):
		#load blocks
		with open(os.path.join("world", "map_0.txt"), "r") as fp:
			worldlist = eval(fp.read())
		self.blocks = []
		for line in worldlist:
			newline = []
			for (typ, texture) in line:
				newline += [Block.Block(typ, texture)]
			self.blocks += [newline]

	def canIpass(self, (x, y)):
		return self.blocks[x][y].canIpass()

	def getBlock(self, (x, y)):
		try:
			return self.blocks[x][y]
		except IndexError:
			return None

	def getTexture(self, (x, y)):
		try:
			return self.blocks[x][y].getTexture()
		except IndexError:
			return 0
