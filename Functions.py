from Myro import *
init("sim")
def square():
    i=0
    while i < 4:
        turnBy(90,"deg")
        forward(1,1)
        i=i+1
penDown()        
square()  