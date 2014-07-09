import Block

class Map(object):
	def __init__(self):
		#load blocks
		with open("map_0.txt", "r") as fp:
			worldlist = eval(fp.read())
		self.blocks = []
		for line in worldlist:
			newline = []
			for (typ, texture) in line:
				newline += Block(typ, texture)


	def canIpass(self, (x, y)):
		return self.blocks[x][y].canIpass()

	@staticmethod
	def pixel_to_block(self, (x, y)):
		return (x//32, y//32)

	def getBlock(self, (x, y)):
		try:
			return self.blocks[x][y]
		except IndexError:
			return None