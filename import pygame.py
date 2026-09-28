import pygame
pygame.init()
WIDTH=1920
HEIGHT=1020

window = pygame.display.set_mode((WIDTH,HEIGHT))
title = pygame.display.set_caption("mario game")
font=pygame.font.Font(None,30)
win=pygame.font.Font(None,30)

RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(128,128,128)
WHITE=(255,255,255)  
BLACK=(0,0,0)
BROWN=(139,69,19)
SKY=(135,206,235)
YELLOW=(255,255,0)
GREEN=(0,255,0)

# player=pygame.Rect()  
# player_change=0
# speed=5
# vel_y=0
# gravity=1
# jump_power=-15

# on_ground=False
# enemy=pygame.Rect()
# e_speed=5

platforms=[
    pygame.Rect(0,970,1920,50),
    pygame.Rect(150,890,150,20),
    pygame.Rect(380,800,150,20),
    pygame.Rect(590,720,150,20),
    pygame.Rect(800,800,900,20),
    pygame.Rect(1750,720,150,20),
    pygame.Rect(1550,650,150,20),
    pygame.Rect(1350,580,150,20),
    pygame.Rect(1000,650,300,20),
    pygame.Rect(1000,580,150,20),
    pygame.Rect(850,500,100,20),
    pygame.Rect(700,530,100,20),
    pygame.Rect(0,530,650,20),
    pygame.Rect(0,460,100,20),
    pygame.Rect(150,390,100,20),
    pygame.Rect(0,320,100,20),
    pygame.Rect(150,250,100,20),
    pygame.Rect(0,180,100,20),
    pygame.Rect(150,120,300,20),
    pygame.Rect(450,180,100,20),
    pygame.Rect(530,180,20,90),
    pygame.Rect(550,250,300,20),
    pygame.Rect(850,250,20,50),
    pygame.Rect(850,300,300,20),
    pygame.Rect(1200,450,600,20),
]

coins=[
    #pygame.Rect(),
]

sun=(1820,100)

clock=pygame.time.Clock()
score=0
run=True
while run:
    window.fill(SKY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for platform in platforms:
        pygame.draw.rect(window,BROWN,platform)

    # for coin in coins:
    #     pygame.draw.circle(window,YELLOW,coin.center,10)

    #pygame.draw.circle(window,YELLOW,(sun),70),
    
    text=font.render(f"score:{score}",True,WHITE)
    window.blit(text,(10,20))
    # clock.tick(60)
    pygame.display.update()
pygame.quit()