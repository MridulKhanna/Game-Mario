import pygame,sys
from pygame.locals import *

pygame.init()          #for starting the process

begin=0
top=0
velocity=1
flag=0
fps=250                 #frames per second
fireballvelocity=4
firelist=[]             

class start():
    def update_start(self):
        startobj=pygame.image.load('start.png')
        startrect=startobj.get_rect()
        startrect.centerx=600                           #adjust the position of the starting image on the screen
        startrect.centery=300
        canvas.blit(startobj,startrect)                 #blit the starting image on the canvas

class mario():
    def update_up(self):
        if playerrect.top>cactusrect.bottom:            
            playerrect.top-=velocity                    #if player is below the cactus,move the player in upward direction
            
    def update_down(self):
        if playerrect.bottom<firerect.top:
            playerrect.bottom+=velocity                 #if player is above the cactus,move the player in downward direction


def update_fireball():                                  #leave the fireball of the dragon
    fireballobj=pygame.image.load('fireball.png')
    fireballobj=pygame.transform.scale(fireballobj,(25,25))
    fireballrect=fireballobj.get_rect()
    fireballrect.centerx=dragonrect.centerx
    fireballrect.centery=dragonrect.centery
    fireballrectlist.append(fireballrect)
    
def collision(playerrect,f):
    if playerrect.colliderect(f):
        s.update_start()
        pygame.mixer.music.load('mario_dies.wav')
        pygame.mixer.music.play(1,0)
        return False
    else:
        return True
        
               
canvas=pygame.display.set_mode((1200,600))         #set the boundary dimensions of the game
black=(0,0,0)
canvas.fill(black)                                 #fill the background with black colour
pygame.display.set_caption('MARIO')                #set the caption for the game

playerobj=pygame.image.load('maryo.png')           #load the image of mario player
playerrect=playerobj.get_rect()                    #rect objects are used to manipulate each area in the form of rectangle

dragonobj=pygame.image.load('dragon.png')
dragonrect=dragonobj.get_rect()

cactusobj=pygame.image.load('cactus.png')
cactusrect=cactusobj.get_rect()

fireobj=pygame.image.load('fire.png')
firerect=fireobj.get_rect()


fireballobj=pygame.image.load('fireball.png')
fireballobj=pygame.transform.scale(fireballobj,(25,25))           #adjust the size of fireball
fireballrect=fireballobj.get_rect()
fireballobj1=pygame.image.load('fireball.png')
fireballobj1=pygame.transform.scale(fireballobj1,(15,15))
fireballrect1=fireballobj1.get_rect()

fireballrectlist=[]
fireballrectlist1=[]

s=start()                       #create object of start class
s.update_start() 
m=mario()                       #create object of mario class

mainClock=pygame.time.Clock()


while True:     
    for event in pygame.event.get():           #capture or get the event
        if event.type==KEYDOWN:                #on pressing the key
            if event.key==K_ESCAPE:
                pygame.quit()                  #when escape button is pressed the game ends
                sys.exit()
                    
            if event.key==K_SPACE:
                begin=1                        #on pressing the space button the game starts
                  
                canvas.fill(black)             #remove the starting image and fill the background with black colour

                    
                pygame.mixer.music.load('mario_theme.wav')          #load the music i.e. mario theme
                pygame.mixer.music.play(-1,0)                       #start the playback of the music
                    
                playerrect.centerx=75
                playerrect.centery=300
                    
                dragonrect.centerx=1150
                dragonrect.centery=300

                cactusrect.centerx=600
                cactusrect.centery=25   
                
                firerect.centerx=600
                firerect.centery=575
                          
            if event.key==K_UP:                   #when arrow up key is pressed
                top=1
                
            if event.key==K_1:                    #on pressing key '1',the player fires the fireballs
                fireballobj1=pygame.image.load('fireball.png')
                fireballobj1=pygame.transform.scale(fireballobj1,(15,15))
                fireballrect1=fireballobj1.get_rect()
                fireballrect1.centerx=playerrect.centerx
                fireballrect1.centery=playerrect.centery
                fireballrectlist1.append(fireballrect1)
        
        if event.type==KEYUP:                      #on releasing the key
            if event.key==K_UP:                    #when arrow up key is released
                if top!=0:
                    top=2
                    
                              
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
            
    if top==1:
        if playerrect.top==cactusrect.bottom:      #if the player hits the cactus
            begin=0
            top=0
            s.update_start() 
            pygame.mixer.music.load('mario_dies.wav')
            pygame.mixer.music.play(1,0) 
        else:
            m.update_up()

                   
    elif top==2: 
        if playerrect.bottom==firerect.top:         #if the player hits the fire
            begin=0
            top=0
            s.update_start()
            pygame.mixer.music.load('mario_dies.wav')
            pygame.mixer.music.play(1,0)
        else:
            m.update_down()    
    
    if begin==1:
        if flag==0:
            if dragonrect.top==cactusrect.bottom:      #when the dragon hits the cactus
                flag=1
                update_fireball()
                
            else: 
                dragonrect.top-=velocity              #move the dragon in upward direction
                if dragonrect.top==300 or dragonrect.top==200:
                    update_fireball()
         
        else:
            if dragonrect.bottom==firerect.top:        #when the dragon hits the fire
                flag=0
                update_fireball()
            else:
                dragonrect.bottom+=velocity            #move the dragon in downward direction
                if dragonrect.bottom==300 or dragonrect.bottom==400: 
                    update_fireball() 

        for f in fireballrectlist:
            if f.left!=0:
                f.left-=fireballvelocity               #move the dragon fireballs in left direction
                canvas.blit(fireballobj,f)                        
                
        for f in fireballrectlist:
            if f.left<=0:
                fireballrectlist.remove(f)        #as soon as the fireball goes beyond the left boundary, remove it from the list
                
        for f in fireballrectlist1:
            if f.right!=1200:
                f.right+=fireballvelocity           #move the player fireballs in right direction
                canvas.blit(fireballobj1,f)                        
                
        for f in fireballrectlist1:
            if f.right>=1200:
                fireballrectlist1.remove(f)      #as soon as the fireball goes beyond the right boundary, remove it from the list

        for f in fireballrectlist:       
            if playerrect.colliderect(f):           #when the dragon fireball hits the player
                s.update_start()
                pygame.mixer.music.load('mario_dies.wav')
                pygame.mixer.music.play(1,0)
                begin=0
                break
            
        for f in fireballrectlist1:       
            if dragonrect.colliderect(f):           #when the player fireball hits the dragon
                s.update_start()
                pygame.mixer.music.load('mario_dies.wav')
                pygame.mixer.music.play(1,0)
                begin=0
                break
                
        if begin==1:
            pygame.display.update()           
            canvas.fill(black)
            canvas.blit(playerobj,playerrect)  
            canvas.blit(dragonobj,dragonrect) 
            canvas.blit(cactusobj,cactusrect)
            canvas.blit(fireobj,firerect)
            
    mainClock.tick(fps)           
    pygame.display.update()
