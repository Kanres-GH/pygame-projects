import pygame
import sys
 
sc = pygame.display.set_mode((300, 200))

pi = 3.14
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
 
#pygame.draw.rect(sc, WHITE,  (20, 20, 100, 75))      #Рисует прямоугольник
#pygame.draw.rect(sc, LIGHT_BLUE, (150, 20, 100, 75), 8)    #Рисует полый прямоугольник с толщиной

#pygame.draw.line(sc, WHITE, [10, 30], [290, 15], 3)        #Рисует линию с толщиной
#pygame.draw.line(sc, WHITE,  [10, 50], [290, 35])          #Рисует линию
#pygame.draw.aaline(sc, WHITE, [10, 70], [290, 55])         #Рисует сглаженную линию

#pygame.draw.lines(sc, WHITE, True,[[10, 10], [140, 70],[280, 20]], 2)      #Рисует линии с толщиной  (True и False отвечают за то, замыкать ли концы или нет)
#pygame.draw.aalines(sc, WHITE, False,[[10, 100], [140, 170],[280, 110]])   #Рисует сглаженные линии

#pygame.draw.polygon(sc, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]])         #Рисует многоугольник
#pygame.draw.polygon(sc, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])   #Рисует многоугольник
#pygame.draw.aalines(sc, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])     #Рисует замыкающиеся сглаженные линии (Сделать стороны многоугольника гладкими)
 
#pygame.draw.circle(sc, YELLOW, (100, 100), 50)      #Рисует круг с определённым центром и радиусом
#pygame.draw.circle(sc, PINK, (200, 100), 50, 10)    #Рисует окружность с определённым центром, радиусом и толщиной

#pygame.draw.ellipse(sc, GREEN, (10, 50, 280, 100))      #Рисует эллипс (Параметры как и у прямоугольника)

#pygame.draw.arc(sc, WHITE,(10, 50, 280, 100),0, pi)        #Рисует дугу (Указывается прямоугольник, описывающий эллипс, из которого вырезается дуга. Четвертый и пятый аргументы – начало и конец дуги, выраженные в радианах. Нулевая точка справа)
#pygame.draw.arc(sc, PINK,(50, 30, 200, 150),pi, 2*pi, 5)   #Рисует дугу с толщиной



pygame.display.set_caption('HELP ME')
pygame.display.update()

while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(1000)