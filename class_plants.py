import pygame
class Plants:
    peashooter_plant = pygame.image.load("pictures/Peashooter_0.png")
    peashooter_plant = pygame.transform.scale(peashooter_plant, (100, 100))
    sunflower_plant = pygame.image.load("pictures/SunFlower_0.png")
    sunflower_plant = pygame.transform.scale(sunflower_plant, (100, 100))
    def __init__(self, hp, damage, name, price, sun_generate, shoots, plant_x, plant_y):
        self.hp = hp
        self.damage = damage
        self.name = name
        self.price = price
        self.sun_generate = sun_generate
        self.shoots = shoots
        self.plant_x = plant_x
        self.plant_y = plant_y
        self.active_Splant_time = pygame.time.get_ticks() + 15000
    def draw(self, screen):
        if self.name == "peashooter":
            screen.blit(Plants.peashooter_plant, (self.plant_x, self.plant_y))
        elif self.name == "sunflower":
            screen.blit(Plants.sunflower_plant, (self.plant_x, self.plant_y))