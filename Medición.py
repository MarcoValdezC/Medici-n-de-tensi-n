

# -*- coding: utf-8 -*- 
""" 
Created on Sun Nov  8 13:26:48 2020 
 
@author: marco 
""" 
 
from pyfirmata 
import Arduino, util from pyfirmata 
import INPUT, OUTPUT 
import time 
import matplotlib.pylab as plt from drawnow import* 
 
def make_figure(): 
    plt.title("lectura de tensión pin A0")     
    plt.ylim(-0.1,6)     
    plt.grid(True)     
    plt.xlabel("Tiempo [ms]")     
    plt.ylabel("Voltaje [V]")     
    plt.plot(t,volt,'ro-',label="Voltaje A0")     
    plt.legend(loc="upper left") 
    plt.ion() port  = 'COM9' 
    board = Arduino(port) 
    it = util.Iterator(board) it.start() 
 
board.digital[13].mode = OUTPUT 
board.analog[0].mode= INPUT 
time.sleep(2) board.analog[0].enable_reporting() 
volt=[] 
t=[] 
ti=0 
for i in range(51):     
    if(i%2 ==0): 
        board.digital[13].write(1)     
    else: 
        board.digital[13].write(0)     
        p = float((board.analog[0].read()))*(5.0) 
    t.append(i)     
    volt.append(p)     
    drawnow(make_figure)     
    plt.pause(0.000001)     
    print("%.1f %.3f" %(ti,p))     
    time.sleep(0.2)     
    ti +=0.2 
    time.sleep(1) 
board.analog[0].disable_reporting() 
board.digital[13].write(0) 
board.exit() 
 
 
fileName = "misDatos.csv" 
myFile = open(fileName,'w') 
myFile.write("t_(s),voltaje_(v) \n") 
for i in range(len(t)-1): 
    myFile.write(str(t[i])+","+str(volt[i])+"\n") 
    myFile.write(str(t[-1])+","+str(volt[-1])) 
myFile.close() 

