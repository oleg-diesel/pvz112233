import pygame

class Plants:
    def __init__(self, hp, damage, picture, name, price, sun_generate, plant_x, plant_y):
        self.hp = hp
        self.damage = damage
        self.picture = pygame.image.load(picture).convert_alpha()
        self.picture = pygame.transform.scale(self.picture, (100, 100))
        self.name = name
        self.price = price
        self.sun_generate = sun_generate


    def draw(self, screen):
        screen.blit(self.picture, (100, 100))