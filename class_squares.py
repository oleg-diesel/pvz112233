import pygame


class Squares:
    def __init__(self, kol_vo_strok, kol_vo_stolbcov, cell_size, cell_status):
        self.kol_vo_strok = kol_vo_strok
        self.kol_vo_stolbcov = kol_vo_stolbcov
        self.cell_size = cell_size
        self.cells_list = [] # 1 пустой список для клеток
        self.cell_status = cell_status # 3 параметр "занятости" клетки
        self.cell_active_list = []

    def create_square(self):
        self.cell_active_list = []
        for strok in range(self.kol_vo_strok):
            for kolichestvo in range(self.kol_vo_stolbcov):
                green_square = pygame.Rect((kolichestvo*self.cell_size)+100, (strok*self.cell_size)+100, self.cell_size, self.cell_size)
                self.cells_list.append(green_square)

    def draw_square(self, screen):
        for cell in self.cells_list:
            pygame.draw.rect(screen, (0, 255, 0), cell, 4)