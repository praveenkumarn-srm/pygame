#multiple baloon pop up

import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("multiple balloon pop up")
font=pygame.font.Font(None,30)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
speed=10
radius=25
balloons=[
    {"x":random.randint(50,750),"y":random.randint(50,550),"color":BLACK},
    {"x":random.randint(50,750),"y":random.randint(50,550),"color":BLUE},
    {"x":random.randint(50,750),"y":random.randint(50,550),"color":GREEN},
    {"x":random.randint(50,750),"y":random.randint(50,550),"color":WHITE},
    {"x":random.randint(50,750),"y":random.randint(50,550),"color":GRAY,}
 ]

clock=pygame.time.Clock()
score=0
run=True
while run:
    window.fill((RED))

    for balloon in balloons:
                pygame.draw.circle(window,balloon["color"],(balloon["x"],balloon["y"]),radius)
                balloon["y"]+=speed
                if balloon["y"]>HEIGHT-radius:
                   balloon["y"]=0

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

    
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
       
            
    
            for balloon in balloons:
                distance= ((mouse_x - balloon["x"])**2 + (mouse_y - balloon["y"])**2)**0.5
                if distance <= radius:
                    
                    score+=1
                    balloon["x"]=random.randint(50,750) 
                    balloon["y"]=random.randint(50,550)

    
    
    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    clock.tick(10)
    pygame.display.update()
pygame.quit()

#max score = 17
