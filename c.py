# import pygame
# pygame.init()
# WIDTH=800
# HEIGHT=600

# window=pygame.display.set_mode((WIDTH,HEIGHT))
# image=pygame.image.load(r"C:\Users\User\pygame\among_us.png")

# row=0
# col=0

# RED=(255,0,0)
# BLUE=(0,0,255)
# GRAY=(128,128,128)
# WHITE=(255,255,255)
# #paddle
# paddle=pygame.Rect(400,550,100,30)
# print(paddle)
# paddlee_change=0
# paddle_speed=10

# #ball
# ball = pygame.Rect(390,300,20,20)
# speed_x=5
# speed_y=-5

# #bricks
# bricks=[]
# for row in range (5):
#     for col in range (10):
#         brick = pygame.Rect(col * 80 + 5, row * 30 + 5, 70, 20)
#         bricks.append(brick)

# clock=pygame.time.Clock()
# run=True
# while run:
#     for event in pygame.event.get():
#         if event.type==pygame.QUIT:
#             run=False

#     ball.x += speed_x
#     ball.y += speed_y     

#     pygame.draw.rect(window,BLUE,paddle)

#     pygame.draw.ellipse(window, WHITE, ball)

    
#     for brick in bricks:
#         pygame.draw.rect(window,RED,brick)
            

#     clock.tick(30)
#     pygame.display.update()
# pygame.quit()


# import pygame
# import random
# import sys
# pygame.init()
# WIDTH=800
# HEIGHT=800
# window=pygame.display.set_mode((WIDTH,HEIGHT))
# RED=(255,0,0)
# BLUE=(0,0,255)
# GRAY=(128,128,128)
# WHITE=(255,255,255)
# BLACK=(0,0,0)

# #grid
# ROWS=15
# COLS=15
# CELL=WIDTH//COLS


# #maze
# maze=[
#         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
#         [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
#         [1,1,1,1,1,0,0,0,1,0,0,0,1,0,1],
#         [1,0,0,0,0,0,1,1,1,0,1,0,1,0,1],
#         [1,0,1,0,1,0,1,1,1,0,0,0,0,0,1],
#         [1,0,0,0,1,0,0,0,1,0,1,0,1,1,1],
#         [1,1,1,0,0,0,1,0,0,0,1,0,0,0,1],
#         [1,0,0,0,1,1,1,1,0,1,0,0,1,0,1],
#         [1,0,1,1,1,1,0,0,0,0,0,1,0,0,1],
#         [1,0,0,0,0,1,0,1,1,1,0,0,0,1,1],
#         [1,1,1,1,0,0,0,0,0,1,1,1,0,0,1],
#         [1,0,0,0,0,1,1,1,1,1,1,1,1,0,1],
#         [1,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
#         [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
#         [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# ]

# #pac man
# pac_row, pac_col = 1, 1
# dx,dy=0,0
# speed=1

# #ghost
# ghosts=[
#     {"row":12,"col":13,"dir":(0,1)},
#     {"row":13,"col":1,"dir":(1,0)}
# ]

# def can_move(r,c):
#         return maze[r][c] == 0

# clock=pygame.time.Clock()
# run=True
# while run:
#     window.fill(BLACK)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run=False

# #move pac man

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 dx, dy = 0, -1
#             elif event.key == pygame.K_RIGHT:
#                 dx, dy = 0, 1
#             elif event.key == pygame.K_UP:
#                 dx, dy = -1, 0
#             elif event.key == pygame.K_DOWN:
#                 dx, dy = 1, 0

#     new_r = pac_row + dx
#     new_c = pac_col + dy
#     if can_move(new_r,new_c):
#         pac_row, pac_col = new_r, new_c

# #MOVE GHOSTS
#     for ghost in ghosts:
#         gr, gc = ghost["row"], ghost["col"]
#         dr, dc = ghost["dir"]

#     if can_move(gr + dr, gc + dc):
#         ghost["row"] += dr
#         ghost["col"] += dc

#     else:
#         #change directions randomly
#         directions = [(0,1),(0,-1),(1,0),(-1,0)]
#         ghost["dir"] =random.choice(directions)

#     #collision with ghost
#     for ghost in ghosts:
#         if ghost["row"] == pac_row and ghost ["col"] == pac_col:
#             print("game over!")
#             pygame.quit()
#             sys.exit()

# #draw maze

#     for r in range(ROWS):
#         for c in range(COLS):

#             if maze[r][c] == 1:
#                 pygame.draw.rect(window, BLUE, (c*CELL, r*CELL, CELL, CELL))
                
# #draw ghosts

#     for ghost in ghosts:
#         pygame.draw.circle(window,GRAY,(ghost["col"]*CELL + CELL//2, ghost["row"]*CELL + CELL//2),CELL//3)

# #draw pac man

#     pygame.draw.circle(window, RED, (pac_col*CELL + CELL//2, pac_row*CELL + CELL//2),CELL//3)

#     clock.tick(10)
#     pygame.display.update()
# pygame.quit()

import pygame
import sys
pygame.init()
WIDTH=800
HEIGHT=600


window = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.display.set_caption("mini mario game")
font=pygame.font.Font(None,30)
win=pygame.font.Font(None,30)
background=pygame.image.load(r"C:\Users\User\pygame\background.jpg")
background=pygame.transform.scale(background,(WIDTH,HEIGHT))
mario=pygame.image.load(r"C:\Users\User\pygame\mario.jpg")
mario=pygame.transform.scale(mario,(40,50))
goomba=pygame.image.load(r"C:\Users\User\pygame\goomba.jpg")
goomba=pygame.transform.scale(goomba,(40,50))

RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(128,128,128)
WHITE=(255,255,255)
BLACK=(0,0,0)
BROWN=(139,69,19)
SKY=(135,206,235)
YELLOW=(255,255,0)
GREEN=(0,255,0)

player=pygame.Rect(100,500,40,50)
player_change=0
speed=5
vel_y=0
gravity=1
jump_power=-15

on_ground=False
enemy=pygame.Rect(500,500,40,50)
e_speed=5

platforms=[
    pygame.Rect(0,550,800,50),
    pygame.Rect(200,450,150,20),
    pygame.Rect(450,380,150,20),
    pygame.Rect(650,300,100,20)
]

coins=[
    pygame.Rect(260,410,20,20),
    pygame.Rect(510,340,20,20),
    pygame.Rect(690,260,20,20)
]

clock=pygame.time.Clock()
score=0
run=True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -speed

            if event.key == pygame.K_RIGHT:
                player_change = speed

            if event.key == pygame.K_SPACE and on_ground:
                vel_y = jump_power
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player_change = 0

            if event.key == pygame.K_RIGHT:
                player_change = 0

    player.x = player.x + player_change

    vel_y = vel_y + gravity
    player.y = player.y + vel_y

    on_ground = False

    for platform in platforms:

        if player.colliderect(platform):

            if vel_y > 0:
                player.bottom = platform.top
                vel_y = 0
                on_ground = True

    for coin in coins[:]:

        if player.colliderect(coin):

            coins.remove(coin)

            score = score + 1

    enemy.x += e_speed

    if enemy.x <= 400 or enemy.x >= 700:
        e_speed *= -1

    if player.colliderect(enemy):

        text = font.render("GAME OVER", True, RED)

        win.blit(text, (280, 200))

        pygame.display.update()

        pygame.time.delay(2000)

        pygame.quit()
        sys.exit()

    window.blit(background,(0,0))

    for platform in platforms:
        pygame.draw.rect(window,BROWN,platform)

    for coin in coins:
        pygame.draw.circle(window,YELLOW,coin.center,10)

    pygame.draw.rect(window,RED,(enemy))

    
    window.blit(mario,(player.x,player.y))
    window.blit(goomba,(enemy.x,enemy.y))
    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    clock.tick(60)
    pygame.display.update()
pygame.quit()