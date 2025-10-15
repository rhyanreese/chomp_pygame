#example file showing basic pygame game loop
import pygame

#pygame setup
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
print(type(screen))
clock=pygame.time.Clock()
running = True

class Leroy:
    def __init__(self,x=0,y=0):
        self.image=pygame.image.load('PNG/Round/monkey.png')
        self.surface=pygame.transform.rotozoom(self.image,0,0.7)
        self.x=x
        self.y=y
        self.vx=0
        self.vy=0

    def draw(self,screen_surface):
        """"Draw leroy at his x,y on provided surface"""
        screen_surface.blit(self.surface,(self.x,self.y))


#make an instance of leroy
player=Leroy(200,300)

sky_blue = [0,150,255]

while running:
    #poll for events
    #pygame.QUIT event means user clicks X to exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        leroy_projectile_x=leroy_x
           #UPDAte PLAYERS
   
   
        
    #RENDER YOUR GAME HERE 
    #fill screenw color to wiope anythign from last frame
    

    
    #Render game here

    #flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)#limits FPS to 60

pygame.quit()
