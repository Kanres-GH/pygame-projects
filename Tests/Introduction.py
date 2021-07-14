# здесь подключаются модули
import pygame
import sys
import random
 
# здесь определяются константы,
# классы и функции
FPS = 60
 
# здесь происходит инициация,
# создание объектов
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()

 
# главный цикл
while True:
 
    # задержка
    clock.tick(FPS)
 
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
 
    # --------
    # изменение объектов
    # --------
 
    # обновление экрана
    pygame.display.update()