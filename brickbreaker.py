import pygame
pygame.init()
WIDTH=800
HEIGHT=600

window=pygame.display.set_mode((WIDTH,HEIGHT))
image=pygame.image.load(r"C:\Users\User\pygame\among_us.png")

row=0
col=0

RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(128,128,128)
WHITE=(255,255,255)
GREEN=(0,255,0)
#paddle
paddle=pygame.Rect(400,550,100,30)
print(paddle.x)
paddle_change=0
paddle_speed=10

#ball
ball = pygame.Rect(390,300,20,20)
speed_x=5
speed_y=-5

#bricks
bricks=[]
for row in range (5):
    for col in range (10):
        brick = pygame.Rect(col * 80 + 5, row * 30 + 5, 70, 20)
        bricks.append(brick)

clock=pygame.time.Clock()
run=True
while run:
    window.fill(BLUE)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                paddle_change=paddle_speed
                y_change=0
                
            if event.key==pygame.K_LEFT:
                paddle_change=-paddle_speed
                y_change=0

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                paddle_change=0
                y_change=0
                
            if event.key==pygame.K_LEFT:
                paddle_change=0
                y_change=0
    
    paddle.x=paddle.x+paddle_change
    if paddle.left < 0:
        paddle.left=0
    if paddle.right > 800:
        paddle.right=800
    ball.x += speed_x
    ball.y += speed_y
    if ball.x<800:
        speed_x=-speed_x
    if ball.y<0:
        speed_y=-speed_y
    if ball.x>WIDTH-800:
        speed_x=-speed_x
    if ball.y>HEIGHT-0:
        run=False

    if ball.colliderect(paddle):
        speed_y=speed_y*-1

    for brick in bricks[:]:
        if ball.colliderect(brick):
            speed_y=speed_y*-1
            bricks.remove(brick)

    pygame.draw.rect(window,GREEN,paddle)

    pygame.draw.ellipse(window, WHITE, ball)

    
    for brick in bricks:
        pygame.draw.rect(window,RED,brick)
            

    clock.tick(30)
    pygame.display.update()
pygame.quit()