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

    if player.x>800:
        player.x=0
    if player.x<0:
        player.x=0

    
    window.blit(mario,(player.x,player.y))
    window.blit(goomba,(enemy.x,enemy.y))
    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    clock.tick(60)
    pygame.display.update()
pygame.quit()