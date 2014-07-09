class Block(object):
	def __init__(self, typ, texture):
		self.typ_block=typ #0=durchgehen, 1=nicht durchgehen
		self.texture_block=texture
		self.x_pos_block = 0
		self.y_pos_block = 0


	def getPos(self):
		return self.x_pos_block, self.y_pos_block

	def canIpass(self):
		return self.typ_block   #!!!! nachbessern, sehr unsauber, da typ_block noch andere Werte in Zukunft bekommen wird!!!!


	def setTyp(self, typ):
		self.typ_block=typ

	def setTexture(self, texture):
		self.texture_block = texture

	def getTexture(self):
		return self.texture_block
