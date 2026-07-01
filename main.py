import pygame
import player
import maze
import pellets

pygame.init()

screen=pygame.display.set_mode((800,600))
clock=pygame.time.Clock()
running= True

while running:
    #1 Events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #2 Updates
    player.update()

    #3 Draw
    screen.fill((0,0,0))
    maze.draw(screen)
    pellets.draw(screen)
    player.draw(screen)

    #4 Display
    pygame.display.update()
    clock.tick(60)

pygame.quit()