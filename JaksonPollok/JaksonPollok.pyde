from random import*
def setup():
    size(500,500)


def draw():
    x=randrange(1,30)
    a=randrange(1,256)
    b=randrange(256)
    c=randrange(256)
    fill(a,b,c)
    quad(mouseX+10, mouseY-10, mouseX+30, mouseY-20, mouseX+50, mouseY+90, mouseX+30,mouseY-76)
    ellipse(mouseX,mouseY,x,x)
    ellipse(mouseX+20,mouseY+15,x,x)
    rect(mouseX-30,mouseY+40,x,x)