#!/usr/bin/python3
import random
import pygame
import os
from pygame.locals import *


class pykids:

	def __init__(self):
		self._running=True
		self._display_surf=None
		self.geom=['rect','circ']
		self.posY=0
		self.posX=0

	def on_init(self):
		pygame.init()
		self._running=True
		self.lastkey=None
		info=pygame.display.Info()
		self.weight,self.height=info.current_w,info.current_h
		if self.weight>2047:
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
			self.posY=0
			self.on_key(event)
		if event.type==pygame.MOUSEBUTTONUP:
			if event.button<4:
				self.posY=0
			self.on_click(event)

	def on_click(self,event):
		(posx,posy)=event.pos
		colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		while colorr+colorb+colorg<50:
			colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		color=(colorr,colorb,colorg)
		width=random.randint(0,2)
		if event.button==4 or event.button==5:
			width=random.randint(10,20)
			inc=1
			if event.button==4:
				inc=-1
			if self.posY and (self.posX==posx or abs(self.posX-posx)<3):
				self.posY+=inc
			else:
				self.posY=posy
				self.posX=posx
			pygame.draw.line(self.screen,color,[posx,self.posY],[posx,self.posY+1],width)
		else:
			figure=random.choice(self.geom)
			sizeX=random.randint(0,(self.weight-posx))
			sizeY=random.randint(0,(self.height-posy))
			if figure=='rect':
				pygame.draw.rect(self.screen,color,[posx,posy,sizeX,sizeY],width)
			if figure=='circ':
				try:
					pygame.draw.ellipse(self.screen,color,[posx,posy,sizeX,sizeY],width)
				except:
					pass
		pygame.display.flip()
				
	def on_key(self,event):
		posx=random.randint(0,self.weight)
		posy=random.randint(0,self.height)
		colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		while colorr+colorb+colorg<50:
			colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
		color=(colorr,colorb,colorg)
		size=random.randint(0,self.height)
		while posx+size>self.weight or posx<0:
			posx=random.randint(0,self.weight)
			size=random.randint(0,self.height)
		while posy+size>self.height or posy<0:
			posy=random.randint(0,self.height)
			size=random.randint(0,self.height)
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
		while (self._running):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__=="__main__":
	game=pykids()
	game.on_execute()