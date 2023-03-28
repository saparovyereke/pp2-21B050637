import pygame
import time

#initialize pygame
pygame.init()

#outpoot screen
length=1000
width=1000
screen=pygame.display.set_mode((length,width))

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

#rotation w.r.t smth
def rotate(surf, image, pos, originPos, angle):
    
    # calcaulate the axis aligned bounding box of the rotated image
    w, h       = image.get_size()
    box        = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(angle) for p in box]
    min_box    = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box    = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

    # calculate the translation of the pivot 
    pivot        = pygame.math.Vector2(originPos[0], -originPos[1])
    pivot_rotate = pivot.rotate(angle)
    pivot_move   = pivot_rotate - pivot

    # calculate the upper left origin of the rotated image
    origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

    # get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)

    # rotate and blit the image
    surf.blit(rotated_image, origin)

    # draw rectangle around the image
    #pygame.draw.rect (surf, (255, 0, 0), (*origin, *rotated_image.get_size()),2)

background=pygame.image.load("clock.jpg")
minute_hand=pygame.image.load("minute_hand.png")
second_hand=pygame.image.load("second_hand.png")
seconds=-1
minutes=-1

#main loop

running = True

while running:
    
    #exit from game
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

    #counts minutes and seconds
    pygame.time.delay(1000)

    seconds+=1

    if seconds%60==0:
    
        minutes+=1
    
    #output clock
    screen.fill(WHITE)

    screen.blit(background,(150,200))

    rotate(screen,second_hand,(560,495),(0,0),157-6*seconds)

    rotate(screen,minute_hand,(560,495),(0,0),133-(6)*(minutes))
    
    pygame.display.flip()