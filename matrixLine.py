import threading
import time
import render
import console
from console import fg, bg, fx 

class MatrixLine(threading.Thread):
    
    def __init__(self,string,startX,startY,interval):
        self.string = string 
        self.startX = int(startX)
        self.startY = int(startY)
        
        self.position = 0
        self.interval = interval
        threading.Thread.__init__(self)

    
    def draw(self):

        targetX =   self.startX
        targetY =   self.startY+self.position
        lastY =     self.startY+self.position-1
        lastChar =  self.string[self.position-1:self.position]
        targetChar = self.string[self.position:self.position+1]
        if self.position == 0:
            render.print_at(targetY,targetX,fg.white+targetChar )
            
        elif self.position > len(self.string):
            return False
        else:

            
            render.print_at(lastY,  targetX,fg.green+lastChar   )
            render.print_at(targetY,targetX,fg.white+targetChar )
    
        self.position = self.position + 1
        return True
    

    def run(self): #seperate thread
        while self.draw():
            time.sleep(self.interval)
        self.position = 0
        self.string = " " * len(self.string)
        time.sleep(2)
        while self.draw():
            time.sleep(self.interval)