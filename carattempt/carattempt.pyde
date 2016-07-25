from random import*
#wheel colors
green = color(0,128,0)
blue = color(0,0,255)
red = color(255,0,0)
yellow = color(255,255,0)
black = color(0,0,0)
aqua = color( 0,255,255)
setting = 1
color_ = 1
def setWheelColor(color_):
    global green
    global blue
    global red
    global yellow
    global black
    global aqua
    if color_ == 1:
        fill(green)
    elif color_ ==2:
        fill(blue)
    elif color_ == 3:
        fill(red)
    elif color_ == 4:
        fill(yellow)
    elif color_ == 5:
        fill(black)
    elif color_ == 6:
        fill(aqua)
    noStroke()
    rect(40, 100, 10, 150)
    ellipse(45, 100, 40, 40)
    ellipse(45, 250, 40, 40)
    rect(340, 100, 10, 150)
    ellipse(345, 100, 40, 40)
    ellipse(345, 250, 40, 40)
def setup():
    size(600, 600)
    background(255, 255, 255)
def draw():
    global green
    global blue
    global red
    global yellow
    global black
    global aqua
    global color_
    # if keyPressed == True:
    #     if keyCode == SHIFT:
    #         if setting == 4:
    #             setting = 1
    #             goToSetting()
    #         else:
    #             setting += 1
    if keyPressed == True:
        if keyCode == UP:
            if color_ == 6:
                color_ = 1
                setWheelColor(color_)
            else:
                color_ += 1
                setWheelColor(color_)
        if keyCode == DOWN:
            if color_ == 1:
                color_ = 6
                setWheelColor(color_)
            else:
                color_ -= 1
                setWheelColor(color_)
        if key == 'r' or key == 'R':
            bodytype=rect
            print("Rectangle")
        if key == 'c' or key == 'C':
            bodytype = ellipse
        if key == 't' or key == 'T':
            bodytype = triangle    
    # bodytype(300,300,24,24)
    def bodytype(x,y,width,length):
        bodytype(x,y,width,length)
    bodytype(300,300,24,24)