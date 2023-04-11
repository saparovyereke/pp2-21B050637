import pygame
import random

pygame.init()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

width, length = 400, 600
screen = pygame.display.set_mode((width,length))
pygame.display.set_caption("Racer game")
screen.fill(WHITE)

clock=pygame.time.Clock()
FPS = 60
score, passed_enemies, num_coins = 0, 0, 0
player_speed, enemy_speed = 5, 5
background = pygame.image.load('asphalt_road.png')
f1 = pygame.font.Font(None, 30)
f2 = pygame.font.Font(None,60)
game_over = f2.render('GAME OVER', True , BLACK)
game_paused = f2.render('Game paused', True, BLACK)
unpause = f1.render('Press u to unpause the game',True, BLACK)
pause = f1.render('Press p to pause the game', True, BLACK)
exit = f1.render('Press e to exit the game', True, BLACK)
restart = f1.render('Press r to restart the game', True , BLACK)
over, paused = False, False


class player_car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car1.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        global score,player_speed,enemy_speed,passed_enemies
        pressed = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed[pygame.K_UP]:
                self.rect.move_ip(0, -player_speed)
        if self.rect.bottom < length:
            if pressed[pygame.K_DOWN]:
                self.rect.move_ip(0,player_speed)
        if self.rect.left > 5:
            if pressed[pygame.K_LEFT]:
                self.rect.move_ip(-player_speed, 0)
        if self.rect.right < width-5:        
            if pressed[pygame.K_RIGHT]:
                self.rect.move_ip(player_speed, 0)


class enemy_car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("car2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,width-40), 0)  
 
    def move(self):
        global score,player_speed,enemy_speed,passed_enemies
        self.rect.move_ip(0,enemy_speed)
        if (self.rect.top > length):
            score += 1
            passed_enemies+=1
            if score%10==0 and score!=0:
                player_speed+=1
            if passed_enemies%10==0 and passed_enemies!=0:
                enemy_speed+=1
            self.rect.top = 0
            self.rect.center = (random.randint(40,width-40), 0)


class coin(pygame.sprite.Sprite):
    def __init__(self,num):
        super().__init__()
        if num==10:
            self.image = pygame.image.load("coin3.png")
        else:
            self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,width-40), -15)  
    def move(self):
        global score,player_speed,enemy_speed,passed_enemies
        self.rect.move_ip(0,5)
        if (self.rect.top > length):
            self.rect.top = 0
            self.rect.center = (random.randint(40,width-40), -15)
    def change_loc(self):
        self.rect.top = 0
        self.rect.center = (random.randint(40,width-40), -15)

num = random.randint(1,10)

P1 = player_car()
E1 = enemy_car()
C1 = coin(num)

coins = pygame.sprite.Group()
coins.add(C1)
enemies = pygame.sprite.Group()
enemies.add(E1)
sprites = pygame.sprite.Group()
sprites.add(C1)
sprites.add(P1)
sprites.add(E1)

running = True

while running:
    
    for event in pygame.event.get():
        
        if event.type==pygame.QUIT:
            running = False

        if event.type==pygame.KEYDOWN:

            if event.key == pygame.K_r:
                score, passed_enemies,num_coins = 0, 0, 0
                player_speed, enemy_speed = 5, 5
                over, paused = False, False
                for entity in sprites:
                    entity.kill()
                P1 = player_car()
                E1 = enemy_car()    
                sprites.add(P1)
                sprites.add(E1)
                enemies.add(E1)
                num = random.randint(1,10)
                C1 = coin(num)
                coins.add(C1)
                sprites.add(C1)


            if event.key == pygame.K_p:
                paused = True

            if event.key == pygame.K_u:
                paused = False
            
            if event.key == pygame.K_e:
                pygame.time.delay(500)
                running = False

    if over == False:

        if paused == False:

            screen.blit(background,(0,0))
            player_score = f1.render('Score: '+str(score), True, BLACK)
            coins_number = f1.render('Coins: '+str(num_coins), True, BLACK)
            screen.blit(coins_number,(300,35))
            screen.blit(player_score,(300,15))

            for entity in sprites:
                screen.blit(entity.image, entity.rect)
                entity.move()
            
            if pygame.sprite.spritecollideany(P1, enemies):
                over = True
            
            if pygame.sprite.spritecollideany(P1, coins):
                if num==10:
                    score+=3
                else:
                    score+=1
                num_coins+=1
                C1.kill()
                num = random.randint(1,10)
                C1 = coin(num)
                coins.add(C1)
                sprites.add(C1)


        else:
            screen.fill(RED)
            screen.blit(player_score,(300,25))
            screen.blit(game_paused,(100,150))
            screen.blit(unpause,(100,200))
            screen.blit(pause,(100,250))
            screen.blit(restart,(100,300))
            screen.blit(exit,(100,350))
    
    else:
        screen.fill(RED)
        screen.blit(game_over,(100,150))
        screen.blit(player_score,(300,25))
        screen.blit(restart,(100,250))
        screen.blit(exit,(100,300))
            
    pygame.display.update()

    clock.tick(60)