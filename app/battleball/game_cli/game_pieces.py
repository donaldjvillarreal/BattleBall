import random

class game_piece:
	def __init__(self, roll_size, psize):
		self.has_ball = 0
		self.injured = 0
		self.position = {'xpos':-1, 'ypos':-1}
		if(psize==2):
			self.position['ypos2'] = -2
		self.roll_size = roll_size
		self.psize = psize

	def ball_toggle(self):
		self.has_ball = not self.has_ball

	def place_on_board(self, x, y):
		self.position['xpos'] = x
		self.position['ypos'] = y
		if(self.psize==2):
			self.position['ypos2'] = y+1

	def move(self, x, y):
		self.position['xpos'] = self.position['xpos']+x
		self.position['ypos'] = self.position['ypos']+y
		if(self.psize==2):
			self.position['ypos2'] = self.position['ypos2']+y

	def injury(self, severity):
		self.injured = severity

	def roll(self):
		return random.randint(1,self.roll_size)