  
fillVal = color(126)


def draw():
    fill(fillVal)
    rect(25, 25, 50, 50)


def keyPressed():
  global fillVal
    if key == CODED:
        if keyCode == UP:
            fillVal = 255
        elif keyCode == DOWN:
            fillVal = 0
    else:
        fillVal = 126