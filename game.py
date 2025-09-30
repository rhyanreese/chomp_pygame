#example file showing basci pygame game loop
import pygame

#pygame setup
pygame.init()
screen=pygame.display.set_mode((600,400))
clock=pygame.time.Clock()
running=True

while running:
    #poll for events
    #pygame.QUIT event manes user clikec X to exit
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    #fill screenw color to wiope anythign from last frame
    screen.fill((0,150,150))
    
    #Render game here

    #flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)#limits FPS to 60

pygame.quit()