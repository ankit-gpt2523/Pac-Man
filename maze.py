import pygame

walls = [
    pygame.Rect(100, 100, 600, 20),
    pygame.Rect(100, 100, 20, 160),
    pygame.Rect(100,340,20,160),
    pygame.Rect(680, 100, 20, 160),
    pygame.Rect(680,340,20,160),
    pygame.Rect(100, 480, 600, 20),

    pygame.Rect(250, 220, 300, 20),
    pygame.Rect(250, 340, 300, 20),
]

def draw(screen):
    for wall in walls:
        pygame.draw.rect(screen, (0, 0, 255), wall)