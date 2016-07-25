from random import *
def setup():
    size(150,150)
    grid(150,150,15,15)

def grid(width, height, XScale, YScale):
   background(255, 255, 255)
   x = 0
   while x < width:
       line(0, x + YScale, width, x + YScale)
       x += YScale
   x = 0
   while x < height:
       line(x + XScale, 0, x + XScale, height) 
       x += XScale
def draw():
    if mouseX <= 15 and mouseY <= 15 and mouseX >= 0 and mouseX >= 0:
        if mousePressed and mouseButton == LEFT:
            fill(255,0,0) 
            rect(0,0,15,15)
    if mouseX <= 60 and mouseY <= 90 and mouseX >= 45 and mouseX >= 75:
        if mousePressed and mouseButton == LEFT:
            fill(255,0,0) 
            rect(45,75,15,15)            
    if mouseX <= 75 and mouseY <= 90 and mouseX >= 60 and mouseX >= 75:
        if mousePressed and mouseButton == LEFT:
            fill(255,0,0) 
            rect(60,75,15,15)            
    if mouseX <= 90 and mouseY <= 90 and mouseX >= 75 and mouseX >= 75:
        if mousePressed and mouseButton == LEFT:
            fill(255,0,0) 
            rect(75,75,15,15)                        