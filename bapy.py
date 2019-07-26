#!/usr/bin/python3
import random
import pygame
import os
from pygame.locals import *
from subprocess import Popen,PIPE,STDOUT
import time

class pykids:

        def __init__(self):
                self._running=True
                self._display_surf=None
                self.geom=['rect','circ']
                self.posY=0
                self.posX=0
                self.espeak=None
                self.cache_word=''
                self.time=0

        def on_init(self):
                pygame.init()
                self._running=True
                self.lastkey=None
                info=pygame.display.Info()
                self.width,self.height=info.current_w,info.current_h
                if self.width>2047:
                        self.width=int(self.width/2)
                self.size=self.width,self.height

                self.screen=pygame.display.set_mode(self.size)
                self._display_surf=pygame.display.set_mode(self.size,pygame.HWSURFACE)

        def on_event(self,event):
                if event.type==pygame.QUIT:
                        self._running=False
                if event.type==pygame.KEYDOWN:
                        self.lastkey=event.unicode
                if event.type==pygame.KEYUP:
                        if event.key == pygame.K_BACKSPACE:
                                self._clear_screen()
                        elif event.key == pygame.K_RETURN:
                                self.espeak=Popen(['espeak','-s 120',self.cache_word.encode()],stdout=PIPE,stdin=PIPE,stderr=PIPE)
                                self.cache_word=''
                        else:
                                self.posY=0
                                self.on_key(event)
                if event.type==pygame.MOUSEBUTTONUP:
                        if event.button<4:
                                self.posY=0
                        self.on_click(event)

        def on_click(self,event):
                (posx,posy)=event.pos
                width=random.randint(0,2)
                color=self._pick_color()
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
                        sizeX=random.randint(0,(self.width-posx))
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
                posx=random.randint(0,self.width)
                posy=random.randint(0,self.height)
                size=random.randint(0,self.height)
                color=self._pick_color()
                while posx+size>self.width or posx<0:
                        posx=random.randint(0,self.width)
                        size=random.randint(0,self.height)
                while posy+size>self.height or posy<0:
                        posy=random.randint(0,self.height)
                        size=random.randint(0,self.height)
                font=pygame.font.SysFont('roboto',size)
                f=font.render(self.lastkey,False,color,None)
                self._display_surf.blit(f,(posx,posy))
#                self.espeak.communicate(input=self.lastkey.encode())
#                self.espeak.stdin.write(self.lastkey.encode())
                self.cache_word+=self.lastkey
                pygame.display.flip()

        def _pick_color(self):
                colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
                min_bright=0
                while colorr+colorb+colorg<min_bright:
                        colorr,colorb,colorg=random.randint(0,255),random.randint(0,255),random.randint(0,255)
                color=(colorr,colorb,colorg)
                return(color)

        def _clear_screen(self):
                color=self._pick_color()
                pygame.draw.rect(self.screen,color,[0,0,self.width,self.height],0)
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
