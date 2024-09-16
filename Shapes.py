import pgzrun
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill("red")
    r1=Rect((100,100),(100,100))
    r1.center=WIDTH/2,HEIGHT/2
    screen.draw.filled_rect(r1,"blue")
pgzrun.go()