import pygame

walls = [
    pygame.Rect(100, 100, 200, 20),
    pygame.Rect(100, 100, 20, 200),
    pygame.Rect(300, 100, 20, 200),
    pygame.Rect(100, 300, 220, 20),
]

def draw(screen):
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 255), wall)