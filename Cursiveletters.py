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
    motors(1,2,3.5)
    turnBy(-65,"deg")
    
R()