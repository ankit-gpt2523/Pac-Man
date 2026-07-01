import pygame
import maze 
import pellets

x=400
y=300
speed=5
radius=30
direction="right"
mouth=15
mouth_speed=1

#PACMAN MOUTH OPENING-CLOSING MOVEMENT
def mouth_movement(mouth,mouth_speed):
    mouth+=mouth_speed
    if mouth>=15:
        mouth_speed=-1
    if mouth<=0:
        mouth_speed=1
    return mouth,mouth_speed

#PACMAN MOVEMENT ACTIONS
def update():
    global x,y,direction,mouth,mouth_speed
    old_x=x
    old_y=y
    keys=pygame.key.get_pressed()

    #1 Movement
    if keys[pygame.K_RIGHT]:
        mouth,mouth_speed=mouth_movement(mouth,mouth_speed)
        x+=speed
        direction="right"
    if keys[pygame.K_LEFT]:
        mouth,mouth_speed=mouth_movement(mouth,mouth_speed)
        x-=speed
        direction="left"
    if keys[pygame.K_UP]:
        mouth,mouth_speed=mouth_movement(mouth,mouth_speed)
        y-=speed
        direction="up"
    if keys[pygame.K_DOWN]:
        mouth,mouth_speed=mouth_movement(mouth,mouth_speed)
        y+=speed
        direction="down"
    #2 Boundary
    if x>800-radius:
        x=800-radius
    if x<radius:
        x=radius
    if y<radius:
        y=radius
    if y>600-radius:
        y=600-radius

    #3 Collision
    player_rect = pygame.Rect(
    x - radius,
    y - radius,
    radius * 2,
    radius * 2
    )
    for wall in maze.walls:
        if player_rect.colliderect(wall):
            x=old_x
            y=old_y
    
    #4 Pellets
    pellets.update(player_rect)

#PACMAN FACE DRAWING
def draw(screen):
    pygame.draw.circle(screen,(255,255,0),(x,y),radius)
    if direction=="right":
        pygame.draw.polygon(screen,(0,0,0),[(x,y),(x+radius,y-mouth),(x+radius,y+mouth)])
        pygame.draw.circle(screen, (0,0,0), (x, y - 10), 5)
    if direction=="left":
        pygame.draw.polygon(screen,(0,0,0),[(x,y),(x-radius,y-mouth),(x-radius,y+mouth)])
        pygame.draw.circle(screen, (0,0,0), (x, y -10), 5)    
    if direction=="up":
        pygame.draw.polygon(screen,(0,0,0),[(x,y),(x-mouth,y-radius),(x+mouth,y-radius)])
        pygame.draw.circle(screen, (0,0,0), (x - 10, y), 5)
    if direction=="down":
        pygame.draw.polygon(screen,(0,0,0),[(x,y),(x-mouth,y+radius),(x+mouth,y+radius)])
        pygame.draw.circle(screen, (0,0,0), (x + 10, y), 5)
