import pygame
import random

class Zombie: # создали класс, название всегда с большей буквы
    def __init__(self,hp,damage,x, y, speed, png): # настроили КОНСТРУКТОР класса( добовили параметры объекта
        self.x = x # сохранили параметры класса в переменные(до 12 стр)
        self.y = y
        self.hp = hp
        self.damage = damage
        self.speed = speed
        self.png = pygame.image.load("pictures/zombie1.png")
        self.png = pygame.transform.scale(self.png, (60, 100))



    def move(self): # создали МЕТОД для движения
        if self.x >= 50:
            self.x -= self.speed

    def draw(self, screen): # создали МЕТОД отображения зомби
        screen.blit(self.png, (self.x, self.y))