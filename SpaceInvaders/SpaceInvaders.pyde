def setup():
    size(700,700)
    
def grid(startx, starty, XScale, YScale, rowswanted, columnswanted):
   y = 0
   while y < columnswanted:
       x = 0
       while x < rowswanted:
           rectMode(CENTER)
           rect(startx + x*XScale, starty + y*YScale, XScale, YScale)
           x += 1
       if x == rowswanted:
           y += 1
def draw():
    
    grid(100,100,100,100,6 , 5)