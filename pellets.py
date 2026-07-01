import pygame

pellets = []

for x in range(50, 751, 50):
    for y in range(33,99,37):
        pellets.append((x, y))
    for y in range(533,599,37):
        pellets.append((x, y))
for x in range(250,501,50):
    for y in range(153,199,37):
        pellets.append((x, y))
    for y in range(393,499,37):
        pellets.append((x, y))


def draw(screen):
    for pellet in pellets:
        pygame.draw.circle(screen, (255, 255, 255), pellet, 4)

def update(player_rect):
    global pellets

    for pellet in pellets[:]:
        pellet_rect = pygame.Rect(pellet[0] - 4,pellet[1] - 4,8,8)

        if player_rect.colliderect(pellet_rect):
            pellets.remove(pellet)