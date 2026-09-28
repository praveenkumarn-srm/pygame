#baloon pop up
 
import pygame
import random
pygame.init()
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("balloon pop up")
font=pygame.font.Font(None,30)
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
clock=pygame.time.Clock()
balloon_x=random.randint(50,750) 
balloon_y=random.randint(50,550)
radius=25
speed = 20
score=0
run=True
while run:
    clock.tick(5)
    window.fill((RED))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
    

            #if(balloon_x<mouse_x<balloon_x+radius and balloon_y<mouse_y<balloon_y+radius):
            distance= ((mouse_x - balloon_x)**2 + (mouse_y - balloon_y)**2)**0.5

            if distance <= radius:
                score+=1
                balloon_x=random.randint(50,750) 
                balloon_y=random.randint(50,550)

    balloon_x+=speed


    pygame.draw.circle(window,BLACK,(balloon_x,balloon_y),radius)

    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    pygame.display.update()
pygame.quit()

# max score = 40