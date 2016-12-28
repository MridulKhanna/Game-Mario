import pygame,sys
from pygame.locals import *

pygame.init()

begin=0
top=0
velocity=1
flag=0
fps=250
fireballvelocity=4
firelist=[]

class start():
    def update_start(self):
        startobj=pygame.image.load('start.png')
        startrect=startobj.get_rect()
        startrect.centerx=600
        startrect.centery=300
        canvas.blit(startobj,startrect)

class mario():
    def update_up(self):
        if playerrect.top>cactusrect.bottom:      
            playerrect.top-=velocity 
            
    def update_down(self):
        if playerrect.bottom<firerect.top:
            playerrect.bottom+=velocity 


def update_fireball():
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
        
               
canvas=pygame.display.set_mode((1200,600))
black=(0,0,0)
canvas.fill(black)
pygame.display.set_caption('MARIO')

playerobj=pygame.image.load('maryo.png')
playerrect=playerobj.get_rect()

dragonobj=pygame.image.load('dragon.png')
dragonrect=dragonobj.get_rect()

cactusobj=pygame.image.load('cactus.png')
cactusrect=cactusobj.get_rect()

fireobj=pygame.image.load('fire.png')
firerect=fireobj.get_rect()


fireballobj=pygame.image.load('fireball.png')
fireballobj=pygame.transform.scale(fireballobj,(25,25))
fireballrect=fireballobj.get_rect()
fireballobj1=pygame.image.load('fireball.png')
fireballobj1=pygame.transform.scale(fireballobj1,(15,15))
fireballrect1=fireballobj1.get_rect()

fireballrectlist=[]
fireballrectlist1=[]

s=start()
s.update_start()
m=mario()

mainClock=pygame.time.Clock()


while True:     
    for event in pygame.event.get():
        if event.type==KEYDOWN:          
            if event.key==K_ESCAPE:
                pygame.quit()
                sys.exit()
                    
            if event.key==K_SPACE:
                begin=1
                  
                canvas.fill(black)

                    
                pygame.mixer.music.load('mario_theme.wav')
                pygame.mixer.music.play(-1,0)
                    
                playerrect.centerx=75
                playerrect.centery=300
                    
                dragonrect.centerx=1150
                dragonrect.centery=300

                cactusrect.centerx=600
                cactusrect.centery=25   
                
                firerect.centerx=600
                firerect.centery=575
                          
            if event.key==K_UP:
                top=1
                
            if event.key==K_1:
                fireballobj1=pygame.image.load('fireball.png')
                fireballobj1=pygame.transform.scale(fireballobj1,(15,15))
                fireballrect1=fireballobj1.get_rect()
                fireballrect1.centerx=playerrect.centerx
                fireballrect1.centery=playerrect.centery
                fireballrectlist1.append(fireballrect1)
        
        if event.type==KEYUP:
            if event.key==K_UP:
                if top!=0:
                    top=2
                    
                              
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
            
    if top==1:
        if playerrect.top==cactusrect.bottom:
            begin=0
            top=0
            s.update_start() 
            pygame.mixer.music.load('mario_dies.wav')
            pygame.mixer.music.play(1,0) 
        else:
            m.update_up()

                   
    elif top==2: 
        if playerrect.bottom==firerect.top:
            begin=0
            top=0
            s.update_start()
            pygame.mixer.music.load('mario_dies.wav')
            pygame.mixer.music.play(1,0)
        else:
            m.update_down()    
    
    if begin==1:
        if flag==0:
            if dragonrect.top==cactusrect.bottom:
                flag=1
                update_fireball()
                
            else: 
                dragonrect.top-=velocity
                if dragonrect.top==300 or dragonrect.top==200:
                    update_fireball()
         
        else:
            if dragonrect.bottom==firerect.top:
                flag=0
                update_fireball()
            else:
                dragonrect.bottom+=velocity
                if dragonrect.bottom==300 or dragonrect.bottom==400: 
                    update_fireball() 

        for f in fireballrectlist:
            if f.left!=0:
                f.left-=fireballvelocity
                canvas.blit(fireballobj,f)                        
                
        for f in fireballrectlist:
            if f.left<=0:
                fireballrectlist.remove(f)
                
        for f in fireballrectlist1:
            if f.right!=1200:
                f.right+=fireballvelocity
                canvas.blit(fireballobj1,f)                        
                
        for f in fireballrectlist1:
            if f.right>=1200:
                fireballrectlist1.remove(f)

        for f in fireballrectlist:       
            if playerrect.colliderect(f):
                s.update_start()
                pygame.mixer.music.load('mario_dies.wav')
                pygame.mixer.music.play(1,0)
                begin=0
                break
            
        for f in fireballrectlist1:       
            if dragonrect.colliderect(f):
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
