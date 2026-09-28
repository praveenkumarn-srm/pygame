#multiple ball bouncing

import pygame 
pygame.init()
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("multiple ball bouncing")
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)


radius=10
balls=[
    {"x":100,"y":100,"color":BLACK,"sx":20,"sy":20},
    {"x":200,"y":200,"color":BLUE,"sx":10,"sy":10},
    {"x":300,"y":400,"color":GREEN,"sx":30,"sy":20},
    {"x":400,"y":100,"color":WHITE,"sx":25,"sy":20},
    {"x":500,"y":200,"color":GRAY,"sx":15,"sy":5}
]


clock=pygame.time.Clock()
run=True
while run:
    window.fill((RED))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    for ball in balls:
        pygame.draw.circle(window,ball["color"],(ball["x"],ball["y"]),radius)   
        ball["x"]=ball["x"]+ball["sx"]
        ball["y"]=ball["y"]+ball["sy"]

        if ball["x"]<radius:
            ball["sx"]=-ball["sx"]
        if ball["y"]<radius:
            ball["sy"]=-ball["sy"]
        if ball["x"]>WIDTH-radius:
            ball["sx"]=-ball["sx"]
        if ball["y"]>HEIGHT-radius:
            ball["sy"]=-ball["sy"]
    


        clock.tick(100)
    pygame.display.update()
pygame.quit()