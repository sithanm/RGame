class Player(object):
	def __init__(self,x_pos,y_pos):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.run_state=0
		self.run_speed=5
		self.coord_direction=0 #2=stay_right, 1=right, -1=left, -2=stay_left
		self.jump_boolean = False
		self.jump_value = 10
		self.jump_speed = 10
		self.image_state=0

	def jump_start(self):
		self.jump_boolean=True
		self.jump_value=self.jump_speed




	def step(self):
		if self.jump_boolean==True:
			self.y_pos-=self.jump_value
			self.jump_value-=2

		if self.coord_direction==1 or self.coord_direction==-1:
			self.x_pos+=self.run_speed*self.coord_direction			#x_Bewegung


		self.run_state=(self.run_state+1)%3



	def leftKeyPressed(self):
		self.coord_direction=-1

	def rightKeyPressed(self):
		self.coord_direction=1

	def spaceKeyPressed(self):
		self.jump_start()

	def rightKeyReleased(self):
		self.coord_direction=2

	def leftKeyReleased(self):
		self.coord_direction=-2






	def get_Pos(self):
		return self.x_pos, self.y_pos


	def get_img_ID(self):
		if self.coord_direction==2:
			self.image_state=0
		elif self.coord_direction==-2:
			self.image_state=3
		elif self.coord_direction==1:
			self.image_state=self.run_state
		elif self.coord_direction==-1:
			self.image_state=self.run_state+3
		return self.image_state


