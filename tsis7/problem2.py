import pygame

pygame.init()

pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096) #for better quality

scaled_and_icy=["top_Shy_Away.mp3","top_Saturday.mp3","top_Formidable.mp3","top_Good_Day.mp3","top_Mulberry_Street.mp3","top_Bounce_Man.mp3","top_Choker.mp3","top_Never_Take_It.mp3","top_The_Outside.mp3","top_No_Chances.mp3"]

screen=pygame.display.set_mode((500,500))

screen.fill((255,255,255))

def play_album(album,i):

    pygame.mixer.music.load(album[i])
    pygame.mixer.music.play()

running = True

while running:
    for event in pygame.event.get():                    # 1) Press a to play the album, starts from the first song 
        if event.type==pygame.QUIT:                     # 2) Press p to pause the music
            running = False                             # 3) Press u to unpause the music, starts the music where it paused
        if event.type==pygame.KEYDOWN:                  # 4) Press n to play next song,if it is last song it will play the first one
            if event.key==pygame.K_a:                   # 5) Press s to stop playing song,in order to start press m,n or s
                pos=0                                   # 6) Press b to play song before,if it is the first song it will play the last one
                play_album(scaled_and_icy,pos)         
            if event.key==pygame.K_p:
                pygame.mixer.music.pause()
            if event.key==pygame.K_u:
                pygame.mixer.music.unpause()
            if event.key==pygame.K_s:
                pygame.mixer.music.stop()
                pos=0
            if event.key==pygame.K_n:
                if pos<(len(scaled_and_icy)-1):
                    pos+=1
                    play_album(scaled_and_icy,pos)
                else:
                    pos=0
                    play_album(scaled_and_icy,pos)
            if event.key==pygame.K_b:
                if pos>0:
                    pos-=1
                    play_album(scaled_and_icy,pos)
                else:
                    pos=len(scaled_and_icy)-1
                    play_album(scaled_and_icy,pos)
    
    pygame.display.flip()