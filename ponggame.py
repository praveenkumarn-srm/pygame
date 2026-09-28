#pong game

import pygame
pygame.init()
#window variables
WIDTH=800
HEIGHT=600
window=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("pong game")
font=pygame.font.Font(None,30)
font1=pygame.font.Font(None,30)
#color variables
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)
hit_sound=pygame.mixer.Sound(r"C:\Users\User\Downloads\lordsonny-rock-cinematic-161648 (1).mp3")
#rectangle and circle variables
ball_x=400
ball_y=300
radius=20
width=15
height=100
right_paddle_x=780
right_paddle_y=200
right_paddle_change=0
width2=15
height2=100
left_paddle_x=5
left_paddle_y=200
left_paddle_change=0
speed=10
speed_x=5
speed_y=5
clock=pygame.time.Clock()
left_score=0
right_score=0
run=True
while run:
    window.fill(RED)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                left_paddle_change=-speed
                
            if event.key==pygame.K_s:
                left_paddle_change=speed
                
            if event.key==pygame.K_UP:
                right_paddle_change=-speed
                
            if event.key==pygame.K_DOWN:
                right_paddle_change=speed
                     
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w or event.key==pygame.K_s:
                left_paddle_change=0

            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                right_paddle_change=0

        

    ball_x=ball_x+speed_x
    ball_y=ball_y+speed_y

    if (right_paddle_x <= ball_x + radius <= right_paddle_x + width and
        right_paddle_y <= ball_y <= right_paddle_y + height):
        speed_x = -speed_x
        hit_sound.play()
    if (left_paddle_x <= ball_x - radius <= left_paddle_x + width2 and
        left_paddle_y <= ball_y <= left_paddle_y + height2):
        speed_x = -speed_x
        hit_sound.play()

    if ball_y<radius:
        speed_y=-speed_y
    if ball_y>HEIGHT-radius:
        speed_y=-speed_y
    if ball_x<radius:
        speed_x=-speed_x
        right_score+=1
    if ball_x>WIDTH-radius:
        speed_x=-speed_x
        left_score+=1

    if right_paddle_y<0:
        right_paddle_y=0
    if right_paddle_y>HEIGHT-height:
        right_paddle_y=HEIGHT-height

    if left_paddle_y<0:
        left_paddle_y=0
    if left_paddle_y>HEIGHT-height2:
        left_paddle_y=HEIGHT-height2   

    left_paddle_y=left_paddle_y+left_paddle_change
    right_paddle_y=right_paddle_y+right_paddle_change


    pygame.draw.circle(window,BLACK,(ball_x,ball_y),radius)
    pygame.draw.rect(window, BLUE, (right_paddle_x, right_paddle_y, width, height))
    pygame.draw.rect(window, BLUE, (left_paddle_x, left_paddle_y, width2, height2))

    clock.tick(30)
    text=font.render(f"right score:{right_score}",True,WHITE)
    window.blit(text,(650,20))
    text1=font.render(f"left score:{left_score}",True,WHITE)
    window.blit(text1,(10,20))
    pygame.display.update()
pygame.quit()
