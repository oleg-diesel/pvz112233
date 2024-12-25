import pygame


class Squares:
    def __init__(self, kol_vo_strok, kol_vo_stolbcov, cell_size):
        self.kol_vo_strok = kol_vo_strok
        self.kol_vo_stolbcov = kol_vo_stolbcov
        self.cell_size = cell_size





    def draw_square(self, screen):
        for strok in range(self.kol_vo_strok):
            for kolichestvo in range(self.kol_vo_stolbcov):
                green_square = pygame.Rect((kolichestvo*self.cell_size)+100, (strok*self.cell_size)+100, self.cell_size, self.cell_size)
                pygame.draw.rect(screen, (0, 255, 0), green_square, 4)