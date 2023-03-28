import pygame
import time
#initialize pygame
pygame.init()

clock=pygame.time.Clock()

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#outpoot screen
length=600
width=600
screen=pygame.display.set_mode((length,width))

#main loop
running = True
radius1=int(input("Enter radius of circle:\n"))
x1_coordinate=int(input("Enter your x coordinate(NOTE IT MUST BE LESS THAN RADIUS):\n"))
y1_coordinate=int(input("Enter your y coordinate(NOTE IT MUST BE LESS THAN RADIUS):\n"))

while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        if y1_coordinate+radius1+20<width:
            y1_coordinate+=20
        else:
            y1_coordinate=width-radius1
            
    if  pressed[pygame.K_UP]:
        if y1_coordinate-radius1>20:
            y1_coordinate-=20
        else:
            y1_coordinate=radius1
            
    if pressed[pygame.K_RIGHT]:
        if x1_coordinate+radius1+20<length:
            x1_coordinate+=20
        else:
            x1_coordinate=length-radius1
            
    if pressed[pygame.K_LEFT]:
        if x1_coordinate-radius1>20:
            x1_coordinate-=20
        else:
            x1_coordinate=radius1
        
    screen.fill(WHITE)    
    
    pygame.draw.circle(screen,RED,(x1_coordinate,y1_coordinate),radius1)

    pygame.display.flip()

    clock.tick(60)