#example file showing basic pygame game loop
import pygame

#pygame setup
pygame.init()
WIDTH=600
HEIGHT=400
screen=pygame.display.set_mode((WIDTH,HEIGHT))
clock=pygame.time.Clock()
running = True

sky_blue = [0,150,255]

#leroy_surface=pygame.Surface((100,50))
#leroy_color=[115,64,14]
#leroy_surface.fill(leroy_color)
leroy_x=300
leroy_y=200
leroy_vx=2
leroy_surface=pygame.image.load('PNG/Round/monkey.png')

#make leroy smaller
leroy_surface=pygame.transform.rotozoom(leroy_surface,0,0.7)

#Make new bird surface to be bullets
leroy_projectile_surface=pygame.image.load('PNG/Round/duck.png')

#scale to be smaller than leroy
leroy_projectile_surface=pygame.transform.rotozoom(leroy_projectile_surface,0, 0.2)

#give x,y position
leroy_projectile_x=leroy_x
leroy_projectile_y=leroy_y

#give a speed
leroy_projectile_vx=10


#make a function to launch projectile
#def shoot_bird():
    #make a new brid

    #put at leroys position

    #bird releases



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
    if leroy_x > 0.9*WIDTH or leroy_x < 0.1*WIDTH:
        leroy_speed*=1
   
    leroy_projectile_x+= leroy_projectile_vx    
        
    #RENDER YOUR GAME HERE 
    #fill screenw color to wiope anythign from last frame
    screen.fill(sky_blue)
    screen.blit(leroy_surface,(leroy_x,leroy_y))
    screen.blit(leroy_projectile_surface,(leroy_projectile_x,leroy_projectile_y))

    
    #Render game here

    #flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)#limits FPS to 60

pygame.quit()