bullets = []
alienalive=[True,True,True,True,True]


shot_rate = 0
bullet = False
bullet_x = 0 
bullet_y = 480
x_pos = 20
y_pos = 175
def setup():
    size(500,600)
    
def bulletSpawn():
    fill(255, 0, 0)
    font = loadFont("Baby-blocks-48.vlw")
    textFont(font, 20)
    text("Lives", 10, 590)
    for i in range(len(bullets)):
        fill(0)
        bullets[i][1] -= 2
        ellipse(bullets[i][0],bullets[i][1],5,10)
        if (bullets[i][1]) >= y and (bullets[i][0]) >= x and (bullets[i][1]) <= y +15 and(bullets[i][0]) <= x+15 :
            print("hit")
x = 40
y =50

def draw():
    global alien1
    global shot_rate
    global alien
    global y
    global x
    global bullet
    global bullet_x
    global bullet_y
    global x_pos
    global y_pos
    background(255, 255, 255)
    fill(0,255,0)
    for i in range (5):
        if (bullets[i][1]) >= y and (bullets[i][0]) >= x and (bullets[i][1]) <= y +15 and(bullets[i][0]) <= x+15 :
        rect(100*i+50,y,30,30)

    noFill()
    ellipse(x, 550, 30, 30)
    if keyPressed and (keyCode == LEFT):
        x -= 10
    if keyPressed and (keyCode == RIGHT):
        x += 10 
    
    s = second()
    if s % 20 == 0:
        y=y+1
    """if keyPressed and (keyCode == UP) and shot_rate > 60:
            bullets.append([x_pos + 15, 480])
            shot_rate = 0"""
    
    if keyPressed and (keyCode == UP):
        bullets.append([x, 550])

    bulletSpawn()
    
    print(bullets)