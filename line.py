
import render
import console
from console import fg, bg, fx 

class matrixLine:
    
    def __init__(self,string,startX,startY,interval):
        self.string = string 
        self.startX = startX
        self.startY = startY
        self.position = 0
        self.interval = interval
    
    def draw(self):
        if self.position == 0:
            render.print_at(self.startX,self.startY+self.position,fg.white+self.string[self.position:1]+fg.black)
        else: 
            render.print_at(self.startX,self.startY+self.position-1,fg.green+self.string[self.position-1:1]+fg.black)
            render.print_at(self.startX,self.startY+self.position,fg.green+self.string[self.position1:1]+fg.black)
 
        self.position = self.position + 1