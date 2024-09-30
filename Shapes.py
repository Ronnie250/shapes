import pgzrun
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill("red")
    w=WIDTH
    h=100
    for i in range (15):
        r1=Rect((100,100),(w,h))
        r1.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(r1,"blue")
        w=w-15
        h=h+15
pgzrun.go()