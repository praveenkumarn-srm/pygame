#moving

import pygame
pygame.init()
WIDTH=800
HEIGHT=600
img_width=75
img_height=75

window=pygame.display.set_mode((WIDTH,HEIGHT))
image=pygame.image.load(r"C:\Users\User\pygame\among_us.png")
image=pygame.transform.scale(image,(img_width,img_height))

RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(128,128,128)

img_x=400
img_y=300
speed=10
x_change=0
y_change=0

clock=pygame.time.Clock()
run=True
while run:
    window.fill(RED)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_change=speed
                y_change=0
                
            if event.key==pygame.K_LEFT:
                x_change=-speed
                y_change=0

            if event.key==pygame.K_UP:
                y_change=-speed
                x_change=0

            if event.key==pygame.K_DOWN:
                y_change=speed
                x_change=0  
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                x_change=0
                y_change=0
                
            if event.key==pygame.K_LEFT:
                x_change=0
                y_change=0
                
            if event.key==pygame.K_UP:
                y_change=0
                x_change=0
                
            if event.key==pygame.K_DOWN:
                y_change=0
                x_change=0    
    if img_x<0:
        img_x=0               
    if img_y<0:
        img_y=0
    if img_x>WIDTH-img_width:
        img_x=WIDTH-img_width
    if img_y>HEIGHT-img_height:
        img_y=HEIGHT-img_height
    img_x=img_x+x_change
    img_y=img_y+y_change


    window.blit(image,(img_x,img_y))
    clock.tick(30)
    pygame.display.update()
pygame.quit()


















