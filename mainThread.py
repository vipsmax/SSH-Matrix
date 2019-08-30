from random import *
from console import fg, bg, fx 
import console
import os 
import render
from matrixLine import MatrixLine
import time  
import coordinateQueue
import threading
import SQLconnector



conn = SQLconnector.connectToSource()
cursor = conn.cursor()
sql = """select p.PlayerID, GamerTag 
from participation p 
join players pl on p.playerID = pl.playerID 
join InterestingPlayers ip on p.PlayerID = ip.playerID 
where Seenin60days = 'active'
order by NEWID ()"""
cursor.execute(sql)
dimensions = render.get_terminal_size_windows()


renderThread = threading.Thread(target=render.beginRenderLoop)
renderThread.start()


os.system("cls")
threadGroup = []
threadGroup.append(renderThread)
for row in cursor.fetchall():
    var = MatrixLine(   row[1],
                        (random()*dimensions[0])-random()*len(row[1]),
                        random()*dimensions[1],
                        random()*1)
    var.start() 
    threadGroup.append(var)
    time.sleep(0.33)
