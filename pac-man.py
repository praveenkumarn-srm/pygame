import pygame
import random
import sys
pygame.init()
WIDTH=800
HEIGHT=800
window=pygame.display.set_mode((WIDTH,HEIGHT))
RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(128,128,128)
WHITE=(255,255,255)
BLACK=(0,0,0)

#grid
ROWS=15
COLS=15
CELL=WIDTH//COLS


#maze
maze=[
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
        [1,1,1,1,1,0,0,0,1,0,0,0,1,0,1],
        [1,0,0,0,0,0,1,1,1,0,1,0,1,0,1],
        [1,0,1,0,1,0,1,1,1,0,0,0,0,0,1],
        [1,0,0,0,1,0,0,0,1,0,1,0,1,1,1],
        [1,1,1,0,0,0,1,0,0,0,1,0,0,0,1],
        [1,0,0,0,1,1,1,1,0,1,0,0,1,0,1],
        [1,0,1,1,1,1,0,0,0,0,0,1,0,0,1],
        [1,0,0,0,0,1,0,1,1,1,0,0,0,1,1],
        [1,1,1,1,0,0,0,0,0,1,1,1,0,0,1],
        [1,0,0,0,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,1,1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

#pac man
pac_row, pac_col = 1, 1
dx,dy=0,0
speed=1

#ghost
ghosts=[
    {"row":12,"col":13,"dir":(0,1)},
    {"row":13,"col":1,"dir":(1,0)}
]

def can_move(r,c):
        return maze[r][c] == 0

clock=pygame.time.Clock()
run=True
while run:
    window.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False

#move pac man

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx, dy = 0, -1
            elif event.key == pygame.K_RIGHT:
                dx, dy = 0, 1
            elif event.key == pygame.K_UP:
                dx, dy = -1, 0
            elif event.key == pygame.K_DOWN:
                dx, dy = 1, 0

    new_r = pac_row + dx
    new_c = pac_col + dy
    if can_move(new_r,new_c):
        pac_row, pac_col = new_r, new_c

#MOVE GHOSTS
    for ghost in ghosts:
        gr, gc = ghost["row"], ghost["col"]
        dr, dc = ghost["dir"]

    if can_move(gr + dr, gc + dc):
        ghost["row"] += dr
        ghost["col"] += dc

    else:
        #change directions randomly
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        ghost["dir"] =random.choice(directions)

    #collision with ghost
    for ghost in ghosts:
        if ghost["row"] == pac_row and ghost ["col"] == pac_col:
            print("game over!")
            pygame.quit()
            sys.exit()

#draw maze

    for r in range(ROWS):
        for c in range(COLS):

            if maze[r][c] == 1:
                pygame.draw.rect(window, BLUE, (c*CELL, r*CELL, CELL, CELL))
                
#draw ghosts

    for ghost in ghosts:
        pygame.draw.circle(window,GRAY,(ghost["col"]*CELL + CELL//2, ghost["row"]*CELL + CELL//2),CELL//3)

#draw pac man

    pygame.draw.circle(window, RED, (pac_col*CELL + CELL//2, pac_row*CELL + CELL//2),CELL//3)

    clock.tick(10)
    pygame.display.update()
pygame.quit()