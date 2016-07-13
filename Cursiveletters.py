from Myro import *
sim= Simulation("Empty Room",500,500,makeColor("yellow"))
sim.setup()
makeRobot("SimScribbler",sim)

def R():
    backward(1,3)
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
    penUp()#self explanatory
    motors(1,2,3.5)#orient robot for next letter
    turnBy(-85,"deg")
R()

def e():
    turnBy(25,"deg")
    motors(.7,1,4)
    turnBy(110,"deg")
    motors (-.7,1,4*.18)
    motors (-.7*.3,1+1,4)
    turnBy(15, "deg")
    forward(2,1)
    turnBy(15,"deg")
#motors(left, right, time): control the left and 
e()
#right motors for a given time (seconds), and then stop.
def a():
    turnBy(-15, "deg")
    motors(0, 3, 8.3)# This will make the circle.
    motors(-3, 0, 1.5)# this will make the tail.
    forward(-1,3)# This makes sure that a don't intersect with the letter previous of a.
    # This was made by Ibrahim
a()
def t():
    motors(-1,2,1.6)
    forward(1,2)
    backward(1,.5)
    turnBy(96,"deg")
    forward(1,1)
    backward(2,1)
    forward(1,1.15)
    turnBy(88)
    motors(-1.5,0.9,1)
t ()
    #This was made by Shuh
def L():
    x=0
    penDown()
    motors(0,1,4)
    forward(3,1)
    motors(-1,2,3.8)
    forward(1,3.4)
    motors(0,1,3)
L()
#made by Taric
#y
def y():
    turnBy(65, "deg")
    forward(3,1)
    motors(2, -1, 3)
    forward(3,1)
    motors(-1, 1.8, 3)
    forward(2,2)
    turnBy(-165, "deg")
    forward(4,2)
    motors(3,0,4)
    forward(3,3)
    # This was made by William
y()