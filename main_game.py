from pygame import *

wid, hei = 600, 700


window = display.set_mode((wid, hei))

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    
