# Ethan Armstrong
# w.ethan.armstrong@gmail.com
# explosion33
# June 5, 2018

from scene import *

class createFrog (Node):
	def __init__(self,tilesW,tilesH,sceneSize):
		self.size = (sceneSize[1] * 0.75/tilesH, sceneSize[1] * 0.75/tilesH)
		self.anchor_point = (0, 0)
		frog = SpriteNode('frog.PNG')
		frog.anchor_point = (0,0)
		frog.size = self.size
		self.add_child(frog)
		self.position = (488.73, self.size[1]/4)
		self.tile = ((self.position[0]/(sceneSize[0]/tilesW)), int(self.position[1]/(sceneSize[1]/tilesH)))
		print(self.tile)			
