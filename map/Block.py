class Block(object):
	def __init__(self, typ, texture):
		self.typ_block=typ #alles geraden(+0) durchgehen, alle ungerade nicht durchgehen
		self.texture_block=texture
		self.x_pos_block
		self.y_pos_block


	def getPos(self):
		return self.x_pos_block, self.y_pos_block

	def canIpass(self):
		if self.typ_block%2 == 0:
			return 0
		else:
			return 1


	def setTyp(self, typ):
		self.typ_block=typ

	def setTexture(self, texture):
		self.texture_block = texture

