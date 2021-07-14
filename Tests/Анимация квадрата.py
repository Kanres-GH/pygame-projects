import pygame
import sys
 
FPS = 60
WIN_WIDTH = 400
WIN_HEIGHT = 100
WHITE = (255, 255, 255)
ORANGE = (255, 150, 100)
 
clock = pygame.time.Clock()
sc = pygame.display.set_mode(
    (WIN_WIDTH, WIN_HEIGHT))
 

a = 50
x = 0
y = WIN_HEIGHT // 4
 
while True:
    while x <= WIN_WIDTH - a:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        sc.fill(WHITE)

        pygame.draw.rect(sc, ORANGE,  (x, y, a, a))

        pygame.display.update()
        x += 3
    
        clock.tick(FPS)
    while x >= 0:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
        sc.fill(WHITE)
        pygame.draw.rect(sc, ORANGE,  (x, y, a, a))
        pygame.display.update()
        x -= 3
    
        clock.tick(FPS)