import pygame, sys

from pygame import sprite

pygame.init()
WIN_WIDTH = 300
WIN_HEIGHT = 200
YELLOW = (255,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
speed = 5
class Sharik_vverh: 
    def __init__(self,surface,color):
        self.surface = surface
        self.color = color
        self.x = 20
        self.y = 45
        self.radius = 30
    def dviz_sueta_vverha(self):
        global speed
        pygame.draw.circle(self.surface , self.color , (self.x,self.y),self.radius)
        self.x += speed
        if self.x > (self.surface.get_width() - self.radius):
            speed = -speed
        if self.x < 0:
            speed = -speed
         
class Sharik_vniz: 
    def __init__(self,surface,color):
        self.surface = surface
        self.color = color
        self.x = 50
        self.y = 50
        self.radius = 30
    def dviz_sueta_niz(self):
        global speed
        pygame.draw.circle(self.surface , self.color , (self.x,self.y),self.radius)
        self.x += speed
        if self.x > (self.surface.get_width() - self.radius):
            speed = -speed
        if self.x < 0:
            speed = -speed
         

surface = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
surf = pygame.Surface((300,100))
surf.fill(YELLOW)
surf_1 = pygame.Surface((300,100))
surf_1.fill(BLUE)

surface.blit(surf,(0,0))
surface.blit(surf_1,(0,100))

sharik_surf = Sharik_vverh(surf,BLACK)
sharik_surf_1 = Sharik_vniz(surf_1,RED)

sueta_vverh = False
sueta_vniz = False
while 1 : 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
        elif i.type == pygame.MOUSEBUTTONUP:
            if 0 < i.pos[0] < WIN_WIDTH and 0 < i.pos[1] < WIN_HEIGHT // 2:
                sueta_vverh = True
                sueta_vniz = False
            elif 0 < i.pos[0] < WIN_WIDTH and WIN_HEIGHT // 2 < i.pos[1] < WIN_HEIGHT: 
                sueta_vniz = True
                sueta_vverh = False
    if sueta_vverh:                             
        surf.fill(YELLOW)
        sharik_surf.dviz_sueta_vverha()
        surface.blit(surf,(0,0))
    elif sueta_vniz:
        surf_1.fill(BLUE)
        sharik_surf_1.dviz_sueta_niz()
        surface.blit(surf_1,(0,100))
    pygame.display.update()
    pygame.time.delay(20)