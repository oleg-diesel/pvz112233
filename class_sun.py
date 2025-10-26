import pygame

class Suns:
    regular_sun = pygame.image.load("pictures/aaaa.png")
    regular_sun = pygame.transform.scale(regular_sun, (100, 100))
    sunflower_sun = pygame.image.load("pictures/sunflower_sun.png")

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        self.Rrect = pygame.Rect(self.x, self.y, 100, 95)
    def draw(self, screen):
        if self.name == "regular_sun":
            screen.blit(Suns.regular_sun, (self.x, self.y))
        elif self.name == "sunflower_sun":
            screen.blit(Suns.sunflower_sun, (self.x, self.y))