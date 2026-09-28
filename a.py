#single ball bouncing 

# import pygame
# pygame.init()
# WIDTH=800
# HEIGHT=600
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# RED=(255,0,0)
# BLUE=(0,0,255)
# GREEN=(0,255,0)
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(128,128,128)

# ball_x=400
# ball_y=300
# speed_x=10
# speed_y=10
# radius=20

# clock=pygame.time.Clock()
# run=True
# while run:
#     window.fill((WHITE))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False

    # ball_x=ball_x+speed_x
    # ball_y=ball_y+speed_y


    # if ball_x<radius:
    #     speed_x=-speed_x
    # if ball_y<radius:
    #     speed_y=-speed_y
    # if ball_x>WIDTH-radius:
    #     speed_x=-speed_x
    # if ball_y>HEIGHT-radius:
    #     speed_y=-speed_y

#     pygame.draw.circle(window,(RED),(ball_x,ball_y),radius)  
#     clock.tick(50)      
#     pygame.display.update()
# pygame.quit()

# _ _ _ _ _ _ _ _ _ _ _

#multiple ball bouncing

# import pygame 
# pygame.init()
# WIDTH=800
# HEIGHT=600
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# title=pygame.display.set_caption("multiple ball bouncing")
# RED=(255,0,0)
# BLUE=(0,0,255)
# GREEN=(0,255,0)
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(128,128,128)


# radius=10
# balls=[
#     {"x":100,"y":100,"color":BLACK,"sx":20,"sy":20},
#     {"x":200,"y":200,"color":BLUE,"sx":10,"sy":10},
#     {"x":300,"y":400,"color":GREEN,"sx":30,"sy":20},
#     {"x":400,"y":100,"color":WHITE,"sx":25,"sy":20},
#     {"x":500,"y":200,"color":GRAY,"sx":15,"sy":5}
# ]


# clock=pygame.time.Clock()
# run=True
# while run:
#     window.fill((RED))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False

#     for ball in balls:
#         pygame.draw.circle(window,ball["color"],(ball["x"],ball["y"]),radius)   
#         ball["x"]=ball["x"]+ball["sx"]
#         ball["y"]=ball["y"]+ball["sy"]

#         if ball["x"]<radius:
#             ball["sx"]=-ball["sx"]
#         if ball["y"]<radius:
#             ball["sy"]=-ball["sy"]
#         if ball["x"]>WIDTH-radius:
#             ball["sx"]=-ball["sx"]
#         if ball["y"]>HEIGHT-radius:
#             ball["sy"]=-ball["sy"]
    


#         clock.tick(100)
#     pygame.display.update()
# pygame.quit()
# _ _ _ _ _ _ _ _ 

#catch the ball

# import pygame 
# import random
# pygame.init()
# WIDTH=800
# HEIGHT=600
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# title=pygame.display.set_caption("catch the ball")
# font=pygame.font.Font(None,30)
# RED=(255,0,0)
# BLUE=(0,0,255)
# GREEN=(0,255,0)
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(128,128,128)
# score=0
# ball_x = random.randint(25,WIDTH-25)
# ball_y=0
# radius=25
# width=200
# height=30
# basket_x=280
# basket_y=560
# speed=20
# x_change=0
# y_change=0
# ball_speed=10
# clock=pygame.time.Clock()
# run = True
# while run :
#     window.fill((RED))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run = False
    
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_RIGHT:
#                 x_change=speed
#                 y_change=0
                
#             if event.key==pygame.K_LEFT:
#                 x_change=-speed
#                 y_change=0

            
#         if event.type==pygame.KEYUP:
#             if event.key==pygame.K_RIGHT:
#                 x_change=0
#                 y_change=0
                
#             if event.key==pygame.K_LEFT:
#                 x_change=0
#                 y_change=0

#     basket_x=basket_x+x_change
#     basket_y=basket_y+y_change

#     if basket_x<=0:
#         basket_x=0               
#     if basket_x>WIDTH-width:
#         basket_x=WIDTH-width

#     ball_y+=ball_speed

#     if ball_y+radius>=basket_y:
#         if basket_x<=ball_x<=basket_x+width:
#             score += 1

#             if score%10==0:
#                 speed+=1
#             ball_y=0
#             ball_x=random.randint(25,WIDTH-25) 

#     if ball_y>HEIGHT:
#         ball_y=0
#         ball_x=random.randint(25,WIDTH-25)
      

#     pygame.draw.circle(window,(GRAY),(ball_x,ball_y),radius) 
#     pygame.draw.rect(window,BLACK,(basket_x,basket_y,width,height))
    
    
#     text=font.render(f"score:{score}",True,WHITE)
#     window.blit(text,(10,20))
#     clock.tick(50)
#     pygame.display.update()
# pygame.quit()

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

#baloon pop up
 
# import pygame
# import random
# pygame.init()
# WIDTH=800
# HEIGHT=600
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# title=pygame.display.set_caption("balloon pop up")
# font=pygame.font.Font(None,30)
# RED=(255,0,0)
# BLUE=(0,0,255)
# GREEN=(0,255,0)
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(128,128,128)
# clock=pygame.time.Clock()
# balloon_x=random.randint(50,750) 
# balloon_y=random.randint(50,550)
# radius=25
# speed = 20
# score=0
# run=True
# while run:
#     clock.tick(5)
#     window.fill((RED))
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False
    
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             mouse_x,mouse_y=pygame.mouse.get_pos()
    

#             #if(balloon_x<mouse_x<balloon_x+radius and balloon_y<mouse_y<balloon_y+radius):
#             distance= ((mouse_x - balloon_x)**2 + (mouse_y - balloon_y)**2)**0.5

#             if distance <= radius:
#                 score+=1
#                 balloon_x=random.randint(50,750) 
#                 balloon_y=random.randint(50,550)

#     balloon_x+=speed


#     pygame.draw.circle(window,BLACK,(balloon_x,balloon_y),radius)

#     text=font.render(f"score:{score}",True,WHITE)
#     window.blit(text,(10,20))
#     pygame.display.update()
# pygame.quit()

#max score = 40

#_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  

#multiple baloon pop up

# import pygame
# import random
# pygame.init()
# WIDTH=800
# HEIGHT=600
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# title=pygame.display.set_caption("multiple balloon pop up")
# font=pygame.font.Font(None,30)
# RED=(255,0,0)
# BLUE=(0,0,255)
# GREEN=(0,255,0)
# WHITE=(255,255,255)
# BLACK=(0,0,0)
# GRAY=(128,128,128)
# speed=10
# radius=25
# balloons=[
#     {"x":random.randint(50,750),"y":random.randint(50,550),"color":BLACK},
#     {"x":random.randint(50,750),"y":random.randint(50,550),"color":BLUE},
#     {"x":random.randint(50,750),"y":random.randint(50,550),"color":GREEN},
#     {"x":random.randint(50,750),"y":random.randint(50,550),"color":WHITE},
#     {"x":random.randint(50,750),"y":random.randint(50,550),"color":GRAY,}
#  ]

# clock=pygame.time.Clock()
# score=0
# run=True
# while run:
#     window.fill((RED))

#     for balloon in balloons:
#                 pygame.draw.circle(window,balloon["color"],(balloon["x"],balloon["y"]),radius)
#                 balloon["y"]+=speed
#                 if balloon["y"]>HEIGHT-radius:
#                    balloon["y"]=0

#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False

    
#         if event.type==pygame.MOUSEBUTTONDOWN:
#             mouse_x,mouse_y=pygame.mouse.get_pos()
       
            
    
#             for balloon in balloons:
#                 distance= ((mouse_x - balloon["x"])**2 + (mouse_y - balloon["y"])**2)**0.5
#                 if distance <= radius:
                    
#                     score+=1
#                     balloon["x"]=random.randint(50,750) 
#                     balloon["y"]=random.randint(50,550)

    
    
#     text=font.render(f"score:{score}",True,WHITE)
#     window.blit(text,(10,20))
#     clock.tick(10)
#     pygame.display.update()
# pygame.quit()

#max score = 17

#_ _ _ _ _ _ _ _ _ _  _

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
