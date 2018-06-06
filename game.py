from scene import *
import ui
from frog import createFrog
from car import createCar
from game_menu import MenuScene
import math
from log import createLog

class Game (Scene):
	def setup(self):
		width, height = self.size
		self.width = width
		self.height = height
		self.tilesH = 11
		self.tilesW = 0
		self.background_color = 'darkgray'
		self.touchEnabled = True
		
		self.car1 = [0,0,0,0]
		self.car2 = [0,0,0,0]
		
		self.log1 = [0,0,0,0]
		self.log2 = [0,0,0,0]
		
		self.createBCKG()
		self.frog = createFrog(self.tilesW, self.tilesH, self.size)
		self.frog.z_position = 1 
		self.add_child(self.frog)
		self.countdown()
		
		self.blood = SpriteNode()
		self.blood.texture = Texture('blood.PNG')
		self.blood.size = self.size
		self.blood.position = (self.size[0]/2, self.size[1]/2)
		
	def createBCKG(self):
		x = 0
		y = 0
		self.road = Node(parent = self)
		
		while y < self.tilesH:
			x = 0
			self.tilesW = 0
			while x < self.width:
				self.tilesW += 1
			
				tile = SpriteNode()
				
				if y == 0 or y == 5 or y == self.tilesH-1:
					tile.texture = Texture('path.JPG')
				elif y > 5 and y < self.tilesH-1:
					tile.texture = None
					tile.color = '#0f5e9c'	
				else:	
					tile.texture = Texture('road.JPG')
					
				tile.anchor_point= (0,0)
				tile.size = (self.height/self.tilesH,self.height/self.tilesH)
				tile.position = (x,y * self.height/self.tilesH)
				x +=  self.height/self.tilesH
				self.road.z_position = 0
				self.road.add_child(tile) 
			y += 1
	
	def update(self):
		#Manages Countdown in the beginning
		if self.t <= 3:
			x = int(4-self.t)
			self.num.text = str(x)
		elif 3 < self.t < 4:
			self.touchEnabled = True
			self.num.text = 'GO!'
		elif self.t > 4 and self.num != None:
			fadeOut = Action.fade_to(0,.3, TIMING_LINEAR)
			self.num.run_action(fadeOut)
		elif 4.3 < self.t and self.num != None: 	
			self.num.remove_from_parent()
			self.num = None
		
		
		if str(self.frog.parent)[0:9] == '<__main__':
			self.frog.tile = (int(self.frog.position[0]/(self.size[0]/self.tilesW)), int(self.frog.position[1]/(self.size[1]/self.tilesH)))
		elif True == False:
			x = int((self.frog.parent.position[0]+self.frog.position[0])/(self.size[0]/self.tilesW))
			y = int((self.frog.parent.position[1]+self.frog.position[1])/(self.size[1]/self.tilesH))
			self.frog.tile = (x,y)	
		print((self.frog.tile, self.frog.position))
		
		self.createCars()
		self.hitCar()
		
		self.createLogs()
		self.hitLog()		
			
	def touch_began(self, touch):
		self.touch1 = touch
		
		
				

			
	def touch_ended(self, touch):
		if self.touchEnabled == True:
			tx1, ty1 = self.touch1.location
			tx2, ty2 = touch.location
								
			if (tx1 - tx2) >= -10 and (tx1 - tx2) <= 10 and (ty1 - ty2) >= -10 and (ty1 - ty2) <= 10 and self.frog.tile[1] < self.tilesH-1: 
				x,y = self.frog.position
				y += self.height/self.tilesH
				
				move_action = Action.move_to(x,y, 0.05, TIMING_SINODIAL)
				self.frog.run_action(move_action)
			
			elif (tx1 - tx2) < -10 and -90 < (ty1 - ty2) < 90 and self.frog.tile[0] < self.tilesW-1: 		
				x,y = self.frog.position
				x += self.height/self.tilesH
				
				move_action = Action.move_to(x,y, 0.05, TIMING_SINODIAL)
				self.frog.run_action(move_action)
				
			elif (tx1 - tx2) > 10 and -90 < (ty1 - ty2) < 90 and self.frog.tile[0] > 0: 		
				x,y = self.frog.position
				x -= self.height/self.tilesH
				
				move_action = Action.move_to(x,y, 0.05, TIMING_SINODIAL)
				self.frog.run_action(move_action)	
			
				
			elif (ty1 - ty2) > 10 and self.frog.tile[1] > 0: 		
				x,y = self.frog.position
				y -= self.height/self.tilesH
			
				move_action = Action.move_to(x,y, 0.05, TIMING_SINODIAL)
				self.frog.run_action(move_action)
				
							
	def createCars(self):
		for i in range(0,4):
			if self.car1[i] == 0:
				car = createCar(i+1, self.tilesH, self.tilesW, self.size)
				car.z_position = 2
				self.add_child(car)
				self.car1[i] = car
		
		for car in self.car1:
			if car != 0:
				if car.parent == None:
					x = self.car1.index(car)
					self.car1[x] = 0				
		
		for i in range(0,4):
			if self.car1[i] != 0:
				if (self.size[1]/2) -10 < self.car1[i].position[0] < (self.size[1]/2) + 10:  
					if self.car2[i] == 0:
						car = createCar(i+1, self.tilesH, self.tilesW, self.size)
						car.z_position = 2
						self.add_child(car)
						self.car2[i] = car
		
		for car in self.car2:
			if car != 0:
				if car.parent == None:
					x = self.car2.index(car)
					self.car2[x] = 0
					
	def hitCar(self):
		for car in self.car1:
			if car != 0:
				box = Rect(car.position[0], car.position[1], car.size[0], car.size[1])
				if self.frog.frame.intersects(box) and self.frog.tile[1] == car.tile:
					box = None
					self.lose()
					
		for car in self.car2:
			if car != 0:
				box = Rect(car.position[0], car.position[1], car.size[0], car.size[1])
				if self.frog.frame.intersects(box) and self.frog.tile[1] == car.tile:
					box = None
					self.lose()		
					
	def lose(self):
		#Remove Frog from view
		self.frog.position = (-100,-100)
		self.touchEnabled = False
		
		#Add Restart Menu
		
		self.add_child(self.blood)
		self.menu = MenuScene('You Lose', 'You Got X/5', ['New Game'])
		self.present_modal_scene(self.menu)
		
	def menu_button_selected(self, title):
		white = SpriteNode()
		white.color = 'white'
		white.size = (self.size)
		white.position = (self.size[0]/2, self.size[1]/2)
		white.alpha = 0.4
		
		A1 = Action.fade_to(1.5, 0.6, TIMING_LINEAR)
		A2 = Action.fade_to(0, 1.3, TIMING_LINEAR)
		A3 = Action.remove()

		
		flash = Action.sequence(A1,A2,A3)
		
		white.run_action(flash)
		self.add_child(white)
		white.z_position = 3
			
		#Reset Cars
		for car in self.car1:
			if car != 0:
				car.remove_from_parent()
		for car in self.car2:
			if car != 0:
				car.remove_from_parent()	
			
		self.car1 = [0,0,0,0]
		self.car2 = [0,0,0,0]
		
		self.frog.position = (488.73, self.frog.size[1]/4)
		self.dismiss_modal_scene()
		self.blood.remove_from_parent()
		self.countdown()
		
	def countdown(self):
		self.t = 0
		self.touchEnabled = False
		self.num = LabelNode('5')
		self.num.z_position = 4
		self.num.font = ('AvenirNext-HeavyItalic', 250)
		self.num.color = 'red'
		self.num.size = (self.size)
		self.num.position = (self.width/2, self.height/2)
		self.add_child(self.num)
		
	
	def createLogs(self):
		for i in range(0,4):
			if self.log1[i] == 0:
				log = createLog(i+6,self.tilesH, self.size)
				self.add_child(log)
				self.log1[i] = log
		
		for i in range(0,4):
			if self.size[0]/2 - 10 < self.log1[i].position[0]	< self.size[0]/2 + 10:
				if self.log2[i] == 0:
					log = createLog(i+6, self.tilesH, self.size)
					self.add_child(log)
					self.log2[i] = log
			
	
		for log in self.log1:
			if log != 0:
				if log.parent == None:
					x = self.log1.index(log)
					self.log1[x] = 0
					
		for log in self.log2:
			if log != 0:
				if log.parent == None:
					x = self.log2.index(log)
					self.log2[x] = 0
					
	def hitLog(self):
		for log in self.log1:
			if log != 0:
				box = Rect(log.position[0], log.position[1], log.size[0], log.size[1])
				if self.frog.frame.intersects(box) and self.frog.parent != log:
					for square in log.squares:
						squ = Rect(log.position[0] + square.frame[0], log.position[1] + square.frame[1], square.frame[2], square.frame[3])
						if self.frog.frame.intersects(squ):
							self.frog.remove_from_parent()
							log.add_child(self.frog)
						#	self.frog.position = (square.size[0]/2, square.size[1]/4)
							self.frog.z_position = 5
							break

		"""if str(self.frog.parent)[0:9] != '<__main__':
			log = self.frog.parent
			if self.frog.tile[1] != log.tile:
				x,y = self.frog.position
				x += log.position[1]
				y += log.position[1]
				self.frog.remove_from_parent()
				self.frog.position = (x,y)
		"""			
																
													
			
run(Game(), show_fps = True)									
		
