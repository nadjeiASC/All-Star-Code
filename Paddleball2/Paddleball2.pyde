from random import*
def setup(): 
    size(300,500)
    background(255,255,255)
x=225
y=225
# h=25
# w=25
a=randrange(-1,2)
b=randrange(-1,2)
c=randrange(-1,2)
score= 0
w= 150
def draw():
    global score
    global x
    global y
    global a 
    global b
    global w
    global h
    background(255,255,255)
    fill(255,215,0)
    smooth()
    ellipse(x,y,25,25)
    fill(122,122,122)
    if keyPressed == True:
         if (keyCode == LEFT):
            w = w -3
            if w <= 3:
                w = w
    if keyPressed== True:
         if (keyCode == RIGHT):
            w = w + 3
            if w >= 285:
                w =
    rect(w,477,50,20)
    if a == 1:
        x+=3
        if x > 286:
            a = -1
    elif a == -1:
        x-=3
        if x < 14:
            a = +1 
    if b == 1:
        y=y+3
        if y > 505:
            font = loadFont("Corbel-Bold-48.vlw")
            textFont(font, 28)
            text("Game Over", 50,250)
            text("but you get infinte tries =)", 10, 300)
    elif b == -1:
        y-=1
        if y < 9:
            b = + 1    
    if x >= w and x <= w +50 :
        if y >= mouseY and y <= mouseY+ 20:
            b = -1
            print("it hit")
            score = score+1
            print(score)
    text("score:"+ str(score) , 100,100)
    