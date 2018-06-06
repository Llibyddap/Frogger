# Ethan Armstrong
# w.ethan.armstrong@gmail.com
# explosion33
# June 5, 2018

from scene import *
from random import randint

class createLog(Node):
	def __init__(self, tile, tiles, size):
		self.tilesS = tiles
		self.offset = 40
		self.z_position = 0.8
		self.sizeS = size
		self.tile = tile
		self.squares = []
		self.logSize = 4  #randint(1,4)
		self.anchor_point = (0,0)
		self.isLog = True
		if self.logSize == 1:
			pass
		elif self.logSize == 2:
			pass
		elif self.logSize == 3:
			pass
		elif self.logSize == 4:		
			self.size = (((self.sizeS[1]/self.tilesS) * 414/114) + self.offset, self.sizeS[1]/self.tilesS)
			
		if self.tile == 6:
			self.rowSpeed = 10
		if self.tile == 7:
			self.rowSpeed = 4
		if self.tile == 8:
			self.rowSpeed = 7	
		if self.tile == 9:
			self.rowSpeed = 6	
		
		if self.tile == 6 or self.tile == 8:
			self.position = (0 - self.size[0], (self.sizeS[1]/self.tilesS) * self.tile)
			moveAction = Action.move_to(self.sizeS[0], self.position[1], self.rowSpeed,TIMING_LINEAR)
		
		elif self.tile == 7 or self.tile == 9:
			self.position = (self.sizeS[0], (self.sizeS[1]/self.tilesS) * self.tile)
			moveAction = Action.move_to(0 - self.size[0], self.position[1], self.rowSpeed, TIMING_LINEAR)
			
		r = Action.remove()
		
		self.Action = Action.sequence(moveAction, r)
		
		self.addLog()
		self.addSpots()
						
		self.run_action(self.Action)
	
	def addLog(self):
		log = SpriteNode()
		log.texture = Texture('logBIG.PNG')
		log.size = self.size
		log.z_position = 0.9
		log.anchor_point = (0,0)
		self.add_child(log)	
				
	def addSpots(self):
		for i in range(0, self.logSize):
			box = SpriteNode()
			box.color = 'white'
			box.alpha = 0.5
			box.size = (self.size[1], self.size[1])
			box.anchor_point = (0, 0)
			box.z_position = 2
			box.position = (0 + (self.size[0]/4 * i), 0)
			self.add_child(box)
			self.squares.append(box)	
