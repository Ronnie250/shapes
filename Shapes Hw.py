import pgzrun
WIDTH = 300
HEIGHT = 300
def draw():
    screen.fill("red")
    # r1=Rect((300,100),(100,100))
    # r2=Rect((300.100),(100,100))
    # screen.draw.filled_rect(r1,"blue")
    # screen.draw.filled_rect(r2,"blue")
    r1=Rect((50,50),(100,100))
    screen.draw.filled_rect(r1,"blue")
    r2=Rect((150,150),(100,100))
    screen.draw.filled_rect(r2,"blue")
pgzrun.go()