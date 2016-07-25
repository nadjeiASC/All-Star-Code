from random import*
def setup(): 
    size(500,500)
    background(255,255,255)
x=225
y=225
h=25
w=25
a=randrange(-1,2)
b=randrange(-1,2)
c=randrange(-2,3)
def draw():
    global x
    global y
    global a 
    global b
    global w
    global h
    background(255,255,255)
    fill(255,215,0)
    smooth()
    ellipse(x,y,w,h)
    w=25
    h=25
    if a == 1:
        x+=3
        if x > 486:
            w=10
            a =-1
    elif a == -1:
        x-=3
        if x < 14:
            w=10
            a= +1
    if b == 1:
        y=+3
        if y > 486:
            w=10
            b =-1
    elif b == -1:
        y-=c
        if y < 14:
            w=10
            b =+1

        