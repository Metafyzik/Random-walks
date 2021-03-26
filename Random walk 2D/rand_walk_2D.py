"""2D random walk simulation in pygame."""

import pygame
import random

rows = 100
w = 1200
sizeBtwn = w // rows
start_pos = (480,480)
curr_pos = start_pos
mov_opts = ((0,sizeBtwn),(0,-sizeBtwn),(sizeBtwn,0),(-sizeBtwn,0))
line_to_draw = [start_pos]

# Intializing widnow 
pygame.init()
win = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Random walk")

def drawGrid(w, rows, surface):
    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(win, (0,0,0), (x,0),(x,w) , 2)
        pygame.draw.line(win, (0,0,0), (0,y),(w,y) , 2)

def movChoice (start_pos=start_pos,line_to_draw =line_to_draw):
    choice = random.choice(mov_opts)
    curr_pos = (start_pos[0] + choice[0], start_pos[1] + choice[1])
    line_to_draw.append(curr_pos)

    return line_to_draw, curr_pos

def drawMov(line_to_draw=line_to_draw):
    for item in range (1,len(line_to_draw)):
        x1 = line_to_draw[item-1][0]
        y1 = line_to_draw[item-1][1]

        x2 = line_to_draw[item][0]
        y2 = line_to_draw[item][1]

        pygame.draw.line(win, (242, 231, 80), (x1,y1),(x2,y2), 3 ) 

#"head" is a current position represented on the grid by circle
def drawHead(curr_pos=curr_pos): 
    head_x = int(curr_pos[0])
    head_y = int(curr_pos[1])

    pygame.draw.circle(win, (217, 160, 54),(head_x,head_y) , 5)
    
#drawing starting position of the walk represented by a black circle
def drawStart (start_pos=start_pos): 
    start_x = int(start_pos[0])
    start_y = int(start_pos[1])

    pygame.draw.circle(win, (13, 13, 13),(start_x,start_y) , 5)

run = True

# Main loop
while run:
    pygame.time.delay(500)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((140, 103, 35))
    drawGrid(w,rows,win)

    line_to_draw, curr_pos = movChoice(curr_pos)
    drawMov(line_to_draw)
    drawHead(curr_pos)
    drawStart()
    print("STEPS:",len(line_to_draw)-1)
    pygame.display.update()

pygame.quit()
