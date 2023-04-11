import pygame
import math

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

width = 500
height = 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
FPS = 45

prev, cur ,draw, position= None, None, 'drawing', None
color = BLACK
screen.fill(WHITE)

running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                draw = "eraser"
            if event.key == pygame.K_r:
                draw = "rectangle"
            if event.key == pygame.K_d:
                draw = "drawing"
            if event.key == pygame.K_c:
                draw = "circle"
            if event.key == pygame.K_s:
                draw = "square"
            if event.key == pygame.K_t:
                draw = "right_triangle"
            if event.key == pygame.K_l:
                draw = "equilateral"
            if event.key == pygame.K_h:
                draw = "rhombus"
            
            if event.key == pygame.K_1:
                color = RED
            if event.key == pygame.K_2:
                color = GREEN
            if event.key == pygame.K_3:
                color = BLUE
            if event.key == pygame.K_0:
                color = BLACK
    
    if draw == "drawing":
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.line(screen, color , prev, cur, 2)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None
    
    if draw == "eraser":
        if event.type == pygame.MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEMOTION:
            cur = pygame.mouse.get_pos()
        if prev:
            pygame.draw.line(screen, WHITE , prev, cur, 10)
            prev = cur
        if event.type == pygame.MOUSEBUTTONUP:
            prev = None

    if draw == 'circle':
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position == "up":
            radius = ((x-x1)**2+(y-y1)**2)**0.5
            pygame.draw.circle(screen, color, (x,y), radius , 2)
            position = None
        
    if draw == "rectangle":
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position == "up":
            if x < x1 and y < y1: 
                pygame.draw.rect(screen,color,((x,y,x1-x,y1-y)),2)
            elif x < x1 and y > y1:
                pygame.draw.rect(screen,color, (x,y1,x1-x,y-y1),2)
            elif x > x1 and y > y1:
                pygame.draw.rect(screen,color,(x1,y1,x-x1,y-y1),2)
            else:
                pygame.draw.rect(screen,color,(x1,y,x-x1,y1-y),2)
            position =None
    
    if draw == "square":
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position == "up":
            if x < x1 and y < y1:
                if x1-x>y1-y: 
                    pygame.draw.rect(screen,color,((x,y,x1-x,x1-x)),2)
                else:
                    pygame.draw.rect(screen,color,((x,y,y1-y,y1-y)),2)
            elif x < x1 and y > y1:
                if x1-x>y-y1:
                    pygame.draw.rect(screen,color,((x,y1,x1-x,x1-x)),2)
                else:
                    pygame.draw.rect(screen,color,((x,y1,y-y1,y-y1)),2)
            elif x > x1 and y > y1:
                if x-x1>y-y1:
                    pygame.draw.rect(screen,color,(x1,y1,x-x1,x-x1),2)
                else:
                    pygame.draw.rect(screen,color,(x1,y1,y-y1,y-y1),2)
            else:
                if x-x1 > y1-y:
                    pygame.draw.rect(screen,color,(x1,y,x-x1,x-x1),2)
                else:
                    pygame.draw.rect(screen,color,(x1,y,y1-y,y1-y),2)
            position =None
    
    if draw == "rhombus":
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position=="up":
            B = (x/2+x1/2, y)
            D = (x1, y/2+y1/2)
            E = (x/2+x1/2, y1)
            F = (x, y/2+y1/2)
            pygame.draw.polygon(screen,color,[B,D,E,F],2)
            position =None
    
    if draw == "right_triangle":
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position == "up":
            if x < x1 and y < y1: 
                pygame.draw.polygon(screen,color,[(x,y),(x1,y1),(x,y1)],2)
            elif x < x1 and y > y1:
                pygame.draw.polygon(screen,color,[(x,y),(x1,y1),(x,y1)],2)
            elif x > x1 and y > y1:
                pygame.draw.polygon(screen,color,[(x,y),(x1,y1),(x,y1)],2)
            else:
                pygame.draw.polygon(screen,color,[(x,y),(x1,y1),(x,y1)],2)
            position =None
    
    if draw == "equilateral":
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y =pygame.mouse.get_pos()
            position = "down"
        if event.type == pygame.MOUSEBUTTONUP:
            x1, y1 =pygame.mouse.get_pos()
            position = "up"
        if position=="up":
            height_of_triangle = abs(x-x1)*math.sin(math.pi/3)+y
            A = ((x + (x1-x)/2), y)
            B = (x, height_of_triangle)
            C = (x1, height_of_triangle)
            pygame.draw.polygon(screen,color,[A,B,C],2)
            position =None
    
    pygame.display.flip()

    clock.tick(45)

pygame.quit()