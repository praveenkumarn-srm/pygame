import pygame
pygame.init()
window = pygame.display.set_mode((600,500))
pygame.display.set_caption('basic window')
run = True
RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
WHITE=(255,255,255)
BLACK=(0,0,0)
GRAY=(128,128,128)

triangle=(300,200),(250,250),(350,250)
rectangle=(300,250,100,70)


font=pygame.font.SysFont(None,50,bold=True,italic=True)
image=pygame.image.load(r"C:\Users\User\pygame\among_us.png")
image=pygame.transform.scale(image,(100,100))

img_x = 300
img_y = 250
speed = 10
x_change = 0
y_change = 0
clock = pygame.time.Clock()
while run:
    window.fill(RED)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    text=font.render('score',False,WHITE)
    img_x=img_x+x_change
    img_y=img_y+y_change
    window.blit(text,(10,10))
    pygame.draw.circle(window,GRAY,(300,250),50,2)
    pygame.draw.line(window,BLACK,(250,200),(450,200),10)
    pygame.draw.line(window,BLACK,(450,100),(450,200),10)
    pygame.draw.line(window,BLACK,(250,100),(450,200),10)
    pygame.draw.polygon(window,GRAY,triangle)
    pygame.draw.rect(window,GRAY,rectangle)
    window.blit(image,(img_x,img_y))
    clock.tick(10)
    
    
    
    pygame.display.update()

pygame.quit()

