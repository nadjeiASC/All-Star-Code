bullets = []
shot_rate = 0
bullet = False
bullet_x = 0 
bullet_y = 480
x_pos = 20
y_pos = 175
def setup():
    size(500,600)
    


x = 40
y =50
def draw():
    global shot_rate
    global alien
    global y
    global x
    global bullet
    global bullet_x
    global bullet_y
    global x_pos
    global y_pos
    global alien1
    global alien2
    global alien3
    global alien4
    global alien5
    img = loadImage("space.jpg")
    background(255, 255, 255)
    image(img,0,0)
    fill(0,255,0)
    alien = loadImage("Alien.png")
    alien1 = image(alien,50,y,30,30)
    alien2 = image(alien,150,y,30,30)
    alien3 = image(alien,250,y,30,30)
    alien4 = image(alien,350,y,30,30)
    alien5 = image(alien,450,y, 30, 30)
    noFill()
    ship = loadImage("Main.png")
    image(ship,x, 530, 100, 100)
    if keyPressed and (keyCode == LEFT):
        x -= 10
    if keyPressed and (keyCode == RIGHT):
        x += 10 
    s = second()
    if s % 4 == 0:
        y=y+1
    if keyPressed and (keyCode == UP):
        bullets.append([x, 550])

    bulletSpawn()
    
    print(bullets)
def bulletSpawn():
    global alien1
    fill(255, 255, 0)
    font = loadFont("Baby-blocks-48.vlw")
    textFont(font, 20)
    text("Lives", 10, 590)
    text("Score", 400, 590)
    for i in range(len(bullets)):
        fill(0)
        bullets[i][1] -= 2
        ellipse(bullets[i][0],bullets[i][1],5,10)
        if bullets[i][1] >= y+30 and bullets[i][1] <= y+30  and bullets[i][0] <= x+30 and bullets[i][0] >= x+30 :
            del alien1