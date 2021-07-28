import pygame
import sys
import random, time
 
FPS = 60
titles = ['1', '2', '3', '4', '5']
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

pygame.display.update()

while True:
    pygame.display.set_caption(str(random.randint(1, 100)))

    clock.tick(FPS)

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    pygame.display.update()