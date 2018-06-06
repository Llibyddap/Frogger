from scene import *

class createCar (Node):
	def __init__(self, type, tilesH, tilesW,size):
		
		self.sceneSize = size
		print(self.sceneSize)
		self.type = type
		self.tilesH = tilesH
		self.tilesW = tilesW
		self.size = (self.sceneSize[1]/self.tilesH * 1.97, self.sceneSize[1]/self.tilesH)
		
		
		if type == 1:
			texture = Texture('car1.PNG')
			self.anchor_point = (0,0)
			speed = 5
		elif type == 2:
			texture = Texture('car2.PNG')
			self.size = (-self.size[0] * 1.75, self.size[1] * 1.75)
			self.anchor_point = (0,0)
			offset = -22
			speed = 8
		elif type == 3:
			texture = Texture('car3.PNG')
			self.size = (self.size[0] * 1.15, self.size[1] * 1.15)
			self.anchor_point = (0,0)
			speed = 6
		elif type == 4:
			texture = Texture('car4.PNG')
			self.anchor_point = (0,0)
			self.size = (-self.size[0],self.size[1])
			speed = 2
			offset = 0
		
		self.tile = type
			
		if type == 1 or type == 3:			
			self.position = (0-self.size[0],self.sceneSize[1]/self.tilesH * (self.type))
			move = Action.move_to(self.sceneSize[0],self.position[1], speed, TIMING_LINEAR)
			remove = Action.remove()
		elif type == 2 or type == 4:
			self.position = (self.sceneSize[0] - self.size[0],(self.sceneSize[1]/self.tilesH * (self.type) + offset))
			move = Action.move_to(0 ,self.position[1], speed, TIMING_LINEAR)
			remove = Action.remove()	
		
		
		
		
		car = SpriteNode()
		car.texture = texture
		car.position = (0,0)
		car.size = self.size
		car.anchor_point = (0,0)
		self.add_child(car)
		
		print((self.size[1], self.tilesH, self.type))
		
		
		sequence = Action.sequence(move, remove)
		self.run_action(sequence)
			
			
			
			
