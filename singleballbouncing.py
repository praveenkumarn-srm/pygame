# single ball bouncing 

import pygame
pygame.init()
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)

ball_x=400
ball_y=300
speed_x=10
speed_y=10
radius=20

clock=pygame.time.Clock()
run=True
while run:
    window.fill((WHITE))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    ball_x=ball_x+speed_x
    ball_y=ball_y+speed_y


    if ball_x<radius:
        speed_x=-speed_x
    if ball_y<radius:
        speed_y=-speed_y
    if ball_x>WIDTH-radius:
        speed_x=-speed_x
    if ball_y>HEIGHT-radius:
        speed_y=-speed_y

    pygame.draw.circle(window,(RED),(ball_x,ball_y),radius)  
    clock.tick(50)      
    pygame.display.update()
pygame.quit()
