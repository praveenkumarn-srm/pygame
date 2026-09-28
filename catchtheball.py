#catch the ball

import pygame 
import random
pygame.init()
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("catch the ball")
font=pygame.font.Font(None,30)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
score=0
ball_x = random.randint(25,WIDTH-25)
ball_y=0
radius=25
width=200
height=30
basket_x=280
basket_y=560
speed=20
x_change=0
y_change=0
ball_speed=10
clock=pygame.time.Clock()
run = True
while run :
    window.fill((RED))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
    
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_change=speed
                y_change=0
                
            if event.key==pygame.K_LEFT:
                x_change=-speed
                y_change=0

            
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                x_change=0
                y_change=0
                
            if event.key==pygame.K_LEFT:
                x_change=0
                y_change=0

    basket_x=basket_x+x_change
    basket_y=basket_y+y_change

    if basket_x<=0:
        basket_x=0               
    if basket_x>WIDTH-width:
        basket_x=WIDTH-width

    ball_y+=ball_speed

    if ball_y+radius>=basket_y:
        if basket_x<=ball_x<=basket_x+width:
            score += 1

            if score%10==0:
                speed+=1
            ball_y=0
            ball_x=random.randint(25,WIDTH-25) 

    if ball_y>HEIGHT:
        ball_y=0
        ball_x=random.randint(25,WIDTH-25)
      

    pygame.draw.circle(window,(GRAY),(ball_x,ball_y),radius) 
    pygame.draw.rect(window,BLACK,(basket_x,basket_y,width,height))
    
    
    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    clock.tick(50)
    pygame.display.update()
pygame.quit()
