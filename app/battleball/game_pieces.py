class game_piece:
	def __init__(self):
		self.has_ball = 0
		self.injured = 0
		self.position = {'xpos1':-1, 'ypos1':-1}

	def ball_toggle(self):
		self.has_ball = not self.has_ball

	def place_on_board(self, x, y):
		self.position['xpos1'] = x
		self.position['ypos1'] = y

	def move(self, x, y):
		currx = self.position['xpos1']
		curry = self.position['ypos1']
		self.position['xpos1'] = currx+x
		self.position['ypos1'] = curry+y