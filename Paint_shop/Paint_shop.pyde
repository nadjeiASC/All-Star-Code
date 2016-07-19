from random import *
def setup():
    size(900,900)
    background(255,255,255)
    fill(0,128,0)
    rect(0,0,175,100)
    fill(0,0,255)
    rect(175,0,175,100)
    fill(255,255,0)
    rect(350,0,175,100)
    fill(255,0,0)
    rect(525,0,175,100)
    fill(255,105,180)
    rect(700,0,175,100)
    fill(0,0,0)           
    font = loadFont("ComicSansMS-32.vlw")
    textFont(font, 32)
    text("Clear", 750, 60)
    x = fill(255,255,255)
def draw():
    if mouseButton == LEFT:
        if mouseY<100:
            if mouseX<175:
                fill(0,128,0)
            elif mouseX> 175 and mouseX <350:
                fill(0,0,255)
            elif mouseX> 350 and mouseX< 525:
                fill(255,255,0)
            elif mouseX>525 and mouseX < 700:
                fill(255,0,0)
            elif mouseX > 700:
                fill(255,255,255)
                rect(0,100,900,800)
        else:    
            noStroke()
            rect(mouseX,mouseY,20,20)
    if mouseButton == RIGHT:
        if mouseY>100:
            x = randrange(1,255)
            y = randrange(1,255)
            z = randrange(1,255)
            fill(x,y,z)
            rect(mouseX,mouseY,20,20)

            