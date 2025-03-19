import pygame
import random

class Zombie: # создали класс, название всегда с большей буквы
    zombie_picture = pygame.image.load("pictures/zombie1.png")
    zombie_picture = pygame.transform.scale(zombie_picture, (100, 100))
    def __init__(self,hp,damage,x, y, speed): # настроили КОНСТРУКТОР класса( добовили параметры объекта
        self.x = x # сохранили параметры класса в переменные(до 12 стр)
        self.y = y
        self.hp = hp
        self.damage = damage
        self.speed = speed

    def move(self): # создали МЕТОД для движения
        if self.x >= 50:
            self.x -= self.speed

    def draw(self, screen): # создали МЕТОД отображения зомби
        screen.blit(Zombie.zombie_picture, (self.x, self.y))