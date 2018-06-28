#!/usr/bin/env python3
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk
import cairo
import random
import math

class MouseButtons:
    
    LEFT_BUTTON = 1
    RIGHT_BUTTON = 3
    
    
class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        
        
    def init_ui(self):    

        self.darea = Gtk.DrawingArea()
        self.darea.connect("draw", self.on_draw)
        self.darea.set_events(Gdk.EventMask.BUTTON_PRESS_MASK|Gdk.EventMask.KEY_PRESS_MASK)
        self.add(self.darea)
        
        self.coords = []
                     
        self.darea.connect("button-press-event", self.on_button_press)
        self.darea.connect("key-press-event", self.on_key_release)

        self.set_title("Lines")
        self.resize(300, 200)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, wid, cr):
        cr.set_source_rgb(0, 0, 0)
        cr.set_line_width(0.5)

        objects=['rectangle','arc']
        draw_object=random.choice(objects)
        if draw_object=='rectangle':
            cr.set_source_rgb(0,1,0)
            cr.rectangle(125,10,100,100)
            cr.fill()
        if draw_object=='arc':
            cr.arc(300, 200, 50, math.pi,0)
            cr.set_source_rgb(0.1,0.1,0.1)
            cr.stroke()
        return
        for i in self.coords:
            for j in self.coords:
                
                cr.move_to(i[0], i[1])
                cr.line_to(j[0], j[1]) 
                cr.stroke()

        del self.coords[:]            
                         
                         
    def on_button_press(self, w, e):
        
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.LEFT_BUTTON:
            
            self.darea.queue_draw()           
#            self.coords.append([e.x, e.y])
            
        if e.type == Gdk.EventType.BUTTON_PRESS \
            and e.button == MouseButtons.RIGHT_BUTTON:
            
            self.darea.queue_draw()           
                                                       
    def on_key_release(self,*args):
        print(args)
        pass
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()



