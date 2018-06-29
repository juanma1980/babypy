#!/usr/bin/python3
import random
import pygame
import os
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

class pykids:

	def __init__(self):
		self._running=True
		self._display_surf=None
#		self.size=self.weight,self.height=640,400
		self.geom=['rect','circ']
		self.colors=[WHITE,BLUE,GREEN,RED]

	def on_init(self):
		pygame.init()
		self._running=True
		self.lastkey=None
		info=pygame.display.Info()
		print(info)
		self.weight,self.height=info.current_w,info.current_h
		self.weight=int(self.weight/2)
		self.size=self.weight,self.height

		self.screen=pygame.display.set_mode(self.size)
		self._display_surf=pygame.display.set_mode(self.size,pygame.HWSURFACE)
	
	def on_event(self,event):
		if event.type==pygame.QUIT:
			self._running=False
		if event.type==pygame.KEYDOWN:
			self.lastkey=event.unicode
		if event.type==pygame.KEYUP:
			self.on_key(event)
		if event.type==pygame.MOUSEBUTTONUP:
			self.on_click(event)

	def on_click(self,event):
		(posx,posy)=event.pos
		figure=random.choice(self.geom)
#		color=random.choice(self.colors)
		colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		while colorr+colorb+colorg<50:
			colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		color=(colorr,colorb,colorg)
		sizeX=random.randint(0,(self.weight-posx))
		sizeY=random.randint(0,(self.height-posy))
		width=random.randint(0,10)
		if figure=='rect':
			pygame.draw.rect(self.screen,color,[posx,posy,sizeX,sizeY],width)
		if figure=='circ':
			pygame.draw.ellipse(self.screen,color,[posx,posy,sizeX,sizeY],width)
		pygame.display.flip()
				
	def on_key(self,event):
		posx=random.randint(0,self.weight)
		posy=random.randint(0,self.height)
		colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		while colorr+colorb+colorg<50:
			colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		color=(colorr,colorb,colorg)
#		color=random.choice(self.colors)
		size=random.randint(0,self.height)
		while posx+size>self.weight or posx<0:
			posx=random.randint(0,self.weight)
			size=random.randint(0,self.height)
#			posx=posx-size
		while posy+size>self.height or posy<0:
			posy=random.randint(0,self.height)
			size=random.randint(0,self.height)
#			posy=posy-size
		print("Screen %sX%s"%(self.size))
		print("Posx: %s Posy: %s Size: %s"%(posx,posy,size))
		font=pygame.font.SysFont('roboto',size)
		f=font.render(self.lastkey,False,color,None)
		self._display_surf.blit(f,(posx,posy))
		pygame.display.flip()

	def on_loop(self):
		pass

	def on_render(self):
		pass

	def on_cleanup(self):
		pygame.quit()
	
	def on_execute(self):
		if self.on_init()==False:
				self._running=False
#		self.screen.display.fill(BLACK)
		while (self._running):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__=="__main__":
	game=pykids()
	game.on_execute()
