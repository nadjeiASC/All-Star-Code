from Myro import *
sim= Simulation("Empty Room",500,500,makeColor("yellow"))
sim.setup()
makeRobot("SimScribbler",sim)

def r():
    penDown()
    turnBy(60,"deg")
    motors(1,1,1)
    motors(-1.5,2,4.5)
    forward(1,1)
    motors(1,2,1)
    turnBy(215,"deg")
    motors(.6,.9,2)
    motors(.6,1,1)
    motors(.009,3,3)
    
def e ():
    x=.7
    y=1
    z=4
    turnBy(15,"deg")
    motors (x,y,z)
    turnBy(80,"deg")
    motors (-x,y,z*.5)
    #turnBy(1,"deg")
   # motors (-x,y,z*.3)
    motors (-x*.3,y+1,z*1.5)
def a():
    motors(0, 3, 8.3)# This will make the circle.
    motors(-3, 0, 1.5)# this will make the tail.

forward(1,3)

def L():
    x=0
    penDown()
    motors(0,1,4)
    forward(3,1)
    motors(-1,2,3.8)
    forward(1,3.4)
    motors(0,1,3) 
def y():
    turnBy(65, "deg")
    forward(3,1)
    motors(2, -1, 3)
    forward(3,1)
    motors(-1, 2, 3)
    forward(2,2)
    turnBy(-165, "deg")
    forward(4,2)
    motors(3,0,4)
    forward(3,3)

r()
e()
a()
L()
y()