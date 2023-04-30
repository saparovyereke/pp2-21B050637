# instead of saving level number my cod saves best and last scores, automatically ,after game over and when you quit in the middle of the game pressing e
# if you want to save result and quit you have to press S to save
# new levels == increased speed, press I after endgame to see all the user_names and results, and U to see only your own result

import pygame
import time
import random
import psycopg2

conn = psycopg2.connect(
    database="snake_game",
    user='lab10_user',
    password='zhasik04',
    host='localhost',
    port= '5432'
)
cursor = conn.cursor()
conn.autocommit = True

cnt0 = 0
user_name = str(input("User name: "))
sql = f"select * from snake_game";
cursor.execute(sql)
info = cursor.fetchall()
for i in range(len(info)):
    if info[i][0]==user_name:
        last_score = info[i][1]
        max_score = info[i][2]
        cnt0+=1
if cnt0==0:
    postgres_insert_query = """ INSERT INTO  snake_game(user_name,last_score, max_score) VALUES (%s,%s,%s)"""
    record_to_insert = (user_name, 0, 0)
    cursor.execute(postgres_insert_query, record_to_insert)
    last_score = 0
    max_score = 0
    print("User "+user_name+" successfully added!");
else:
    print("Welcome " +user_name+" !")


def rand_pair(length,width,food_size):
    food_x=random.randint(food_size+5,length-food_size-5)
    food_y=random.randint(food_size+55,width-food_size-5)
    return (food_x,food_y)

def increase_len(arr):
    arr.append([-50,-50])
    return arr

pygame.init()
pygame.time.delay(500)
clock=pygame.time.Clock()

WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

length, width = 500, 600
FPS = 10
snake_size, food_size = 10, 10
score,level,cnt,num_of_eaten_foods = 0,1,0,0
paused = True
endgame = False
x_change,y_change = snake_size,0
snake_body = [[100,100],[-20,-20],[-20,-20]]
food = rand_pair(length,width,food_size)

screen = pygame.display.set_mode((length,width))
pygame.display.set_caption("Snake game")
f1 = pygame.font.Font(None, 30)
f2 = pygame.font.Font(None,60)
text1 = f1.render('Score: '+str(score), True, BLACK)
text2 = f1.render('Level: '+str(level), True, BLACK)
text3 = f2.render('Game Over', True, BLACK)
text4 = f1.render('Press p to pause, and press u to unpause the game', True, BLACK)
text5 = f1.render('Press e to exit the game', True, BLACK)
text6 = f1.render('Press r to restart the game', True, BLACK)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                if y_change==-snake_size: 
                    x_change = 0
                    y_change = -snake_size
                else:
                    x_change = 0
                    y_change = snake_size
            
            if event.key == pygame.K_UP:
                if y_change == snake_size: 
                    x_change = 0
                    y_change = snake_size
                else:
                    x_change = 0
                    y_change = -snake_size
            
            if event.key == pygame.K_RIGHT:
                if x_change==-snake_size: 
                    y_change = 0
                    x_change = -snake_size
                else:
                    y_change = 0
                    x_change = snake_size

            if event.key == pygame.K_LEFT:
                if x_change == snake_size: 
                    y_change = 0
                    x_change = snake_size
                else:
                    y_change = 0
                    x_change = -snake_size
            
            if event.key == pygame.K_SPACE:
                increase_len(snake_body)

            if event.key == pygame.K_r:
                snake_body = [[100,100],[-20,-20],[-20,-20]]
                food = rand_pair(length,width,food_size)
                x_change,y_change = snake_size,0
                FPS = 10
                score,level,num_of_eaten_foods,cnt = 0,1,0,0
                sql = f"select * from snake_game";
                cursor.execute(sql)
                info = cursor.fetchall()
                for i in range(len(info)):
                    if info[i][0]==user_name:
                        last_score = info[i][1]
                        max_score = info[i][2]
                text2 = f1.render('Level: '+str(level), True, BLACK)
                text1 = f1.render('Score: '+str(score), True, BLACK)
                paused = True
                endgame = False
            
            if event.key == pygame.K_s:
                sql = f"select * from snake_game where user_name =\'{user_name}\' and last_score=\'{last_score}\' and max_score = \'{max_score}\'"
                cursor.execute(sql)
                info = cursor.fetchall()
                if score > max_score:
                    max_score1 = score
                else:
                    max_score1 = max_score       
                sql_update = f"Update snake_game set last_score =\'{score}\', max_score = \'{max_score1}\' where last_score=\'{last_score}\' and max_score = \'{max_score}\';" 
                cursor.execute(sql_update)
                running = False
            
            if event.key == pygame.K_i and endgame == True:    
                paused = False
                sql = f"select * from snake_game";
                cursor.execute(sql)
                info = cursor.fetchall()
                print(info)
                sql = None

            if event.key == pygame.K_p:
                paused = False

            if event.key == pygame.K_u:
                paused = True

            if event.key == pygame.K_e:
                sql = f"select * from snake_game where user_name =\'{user_name}\' and last_score=\'{last_score}\' and max_score = \'{max_score}\'"
                cursor.execute(sql)
                info = cursor.fetchall()
                if score > max_score:
                    max_score1 = score
                else:
                    max_score1 = max_score       
                sql_update = f"Update snake_game set last_score =\'{score}\', max_score = \'{max_score1}\' where last_score=\'{last_score}\' and max_score = \'{max_score}\';" 
                cursor.execute(sql_update)
                running = False

            if event.key == pygame.K_u and endgame == True:    
                paused = False
                sql = f"select * from snake_game";
                cursor.execute(sql)
                info = cursor.fetchall()
                for i in range(len(info)):
                    if info[i][0]==user_name:
                        print(info[i][0]+" has best score: "+str(info[i][2])+", and the latest score is: "+str(info[i][1]))
                sql = None

    if endgame == False:
        if paused:
            for i in range(len(snake_body)-1,0,-1):
                snake_body[i][0] = snake_body[i-1][0]
                snake_body[i][1] = snake_body[i-1][1]
            snake_body[0][0]+=x_change
            snake_body[0][1]+=y_change      

            if food[0]==snake_body[0][0] and food[1]==snake_body[0][1]:
                food=rand_pair(length,width)

            for i in range(len(snake_body)):
                for j in range(len(snake_body)):
                    if i!=j  and snake_body[i][0] == snake_body[j][0] and snake_body[i][1] == snake_body[j][1]:
                        endgame = True
                        
            screen.fill(GREEN)
           
            if num_of_eaten_foods%5==0 and num_of_eaten_foods!=0 and food2!=[-100,-100]:
                pygame.draw.rect(screen,(145,170,216),(food2[0],food2[1],2*food_size,2*food_size))
                pygame.draw.rect(screen,WHITE,(food[0],food[1],food_size,food_size))
                cnt+=1
                if cnt<150:
                    if ((snake_body[0][0]>=food2[0] and snake_body[0][0]-2*snake_size <= food2[0]) and (snake_body[0][1]>=food2[1] and snake_body[0][1]-2*snake_size <= food2[1])) or ((snake_body[0][0]+2*snake_size>=food2[0] and snake_body[0][0] <= food2[0]) and (snake_body[0][1]+2*snake_size>=food2[1] and snake_body[0][1] <= food2[1])):
                        pygame.mixer.music.load("EatSound.ogg")
                        pygame.mixer.music.play()
                        score+=2
                        num_of_eaten_foods+=1
                        increase_len(snake_body)
                        text1 = f1.render('Score: '+str(score), True, BLACK)
                        food = rand_pair(length,width,food_size)
                        food2 =[-100,-100]
                        cnt=0
                else:
                    food2 =[-100,-100]
                    cnt=0

            else:
                pygame.draw.rect(screen,WHITE,(food[0],food[1],food_size,food_size))

            pygame.draw.rect(screen,WHITE,(0,0,length,50))

            for i in range(len(snake_body)):
            # appending coordinates and sizes of rect and constantly outputing rect
                nums = []
                nums.append(snake_body[i][0])
                nums.append(snake_body[i][1])
                nums.append(snake_size)
                nums.append(snake_size)

                if i == 0:
                    pygame.draw.rect(screen,BLUE,nums)
                else:
                    pygame.draw.rect(screen,RED,nums)

            pygame.draw.line(screen,BLACK,(0,50),(length,50),2)
            pygame.draw.line(screen,BLACK,(0,width-2),(length,width-2),2)
            pygame.draw.line(screen,BLACK,(0,0),(0,width),2)
            pygame.draw.line(screen,BLACK,(length-2,0),(length-2,width),2)
            pygame.draw.line(screen,BLACK,(0,0),(length,0),2)

            if ((snake_body[0][0]>=food[0] and snake_body[0][0]-snake_size <= food[0]) and (snake_body[0][1]>=food[1] and snake_body[0][1]-snake_size <= food[1])) or ((snake_body[0][0]+snake_size>=food[0] and snake_body[0][0] <= food[0]) and (snake_body[0][1]+snake_size>=food[1] and snake_body[0][1] <= food[1])):
                pygame.mixer.music.load("EatSound.ogg")
                pygame.mixer.music.play()
                food = rand_pair(length,width,food_size)
                food2 = rand_pair(length,width,2*food_size)
                score+=1
                num_of_eaten_foods+=1
                increase_len(snake_body)
                if (score)%10==0 and score!=0:
                    FPS+=5
                    level+=1
                    text2 = f1.render('Level: '+str(level), True, BLACK)
                text1 = f1.render('Score: '+str(score), True, BLACK)
            
            if snake_body[0][0]>=length-2-snake_size or snake_body[0][1]>=width-2-snake_size or snake_body[0][0]<=0 or snake_body[0][1]<=50:
                endgame = True    
            
            screen.blit(text1, (50, 12))
            screen.blit(text2, (350, 12))

        else:
            screen.fill(RED)
            screen.blit(text4,(5,150))
            screen.blit(text5,(5,250))
            screen.blit(text6,(5,350))
            
    else:
        screen.fill(RED)
        screen.blit(text3,(125,200))
        screen.blit(text5,(125,300))
        screen.blit(text6,(125,350))
        sql = f"select * from snake_game where user_name =\'{user_name}\' and last_score=\'{last_score}\' and max_score = \'{max_score}\'"
        cursor.execute(sql)
        info = cursor.fetchall()
        if score > max_score:
            max_score1 = score
        else:
            max_score1 = max_score       
        sql_update = f"Update snake_game set last_score =\'{score}\', max_score = \'{max_score1}\' where last_score=\'{last_score}\' and max_score = \'{max_score}\';" 
        cursor.execute(sql_update)
        
    pygame.display.flip()

    clock.tick(FPS)