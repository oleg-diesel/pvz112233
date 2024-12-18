import pygame  # импортируем всю БИБЛИОТЕКУ pygame
import random
from class_zombie import Zombie # импортировали класс зомби из скрипта
pygame.init()  # инициализация всех модулей Pygame

width, height = 800, 600  # высота и ширина
screen = pygame.display.set_mode((width, height))  # создали окно 800x600

current_frame = 1 # переменная для отслееживания кадра (1 из 3 включительно)
animation_speed = 250 # скорость анимации в милисекундах
sun_fall_time = 0
first_sun_appearance = 0
last_update_time = pygame.time.get_ticks()

zombie_line = [500, 400, 300, 200, 100]
zombie_list = []
for temp in range(100):
    newzombie = Zombie(300, 1,801, random.choice(zombie_line), 5, png=("pictures/zombie1.png"))
    zombie_list.append(newzombie)

batx = 0
baty = 0
sunx = 801
suny = 0


bat = pygame.image.load("pictures/bat-a.png") # загружаем картинку обязательно до цикла
bat = pygame.transform.scale(bat, (75, 75))
bat1 = pygame.image.load("pictures/bat-b.png")
bat1 = pygame.transform.scale(bat1, (45, 75))
bat2 = pygame.image.load("pictures/bat-c.png")
bat2 = pygame.transform.scale(bat2, (75, 75))
little_sun = pygame.image.load("pictures/aaaa.png").convert_alpha()
little_sun = pygame.transform.scale(little_sun, (40, 40))


start = ""
settings = ""
authors = ""
Exit = ""

screens = 1

one_or_two_or_three = 1


pygame.font.init()  # инициализация модуля для работы со шрифтом
my_font = pygame.font.SysFont('Comic Sans MS', 25)  # создаем шрифт для кнопок

white = (255, 255, 255)

# раздел для создания текста


# раздел для создания кнопок

button_start = pygame.Rect(50, 50, 150, 50)  # создаем прямоугольник для кнопки

button_settings = pygame.Rect(50, 150, 150, 50)

button_authors = pygame.Rect(50, 250, 150, 50)

button_exit = pygame.Rect(50, 350, 150, 50)

button_test = pygame.Rect(150, 50, 150, 50)

logic = False

active_time_plus_05_sec = pygame.time.get_ticks() + 250 #считаем время следующей анимации


language_choise = "English"

# игровой цикл

while logic == False:  # создали бесконечный цикл

    for event in pygame.event.get():  # обработка всех событий
        if event.type == pygame.QUIT:  # если событие - выход
            logic = True
        elif event.type == pygame.MOUSEBUTTONUP:
            coordinaty_nazhatiya = event.pos
            xtap = coordinaty_nazhatiya[0]
            ytap = coordinaty_nazhatiya[1]
            if xtap >= 50 and xtap <= 200 and ytap >= 50 and ytap <= 100:
                screens = 2
                sun_fall_time = pygame.time.get_ticks() + 10000 # посчитали во сколько появится солнце
    screen.fill((0, 0, 0))  # заполнить экран черным цветом

    if screens == 1:


        pygame.draw.rect(screen, (125, 125, 125), button_start) # размещаем кнопку

        pygame.draw.rect(screen, (125, 125, 125), button_settings)

        pygame.draw.rect(screen, (125, 125, 125), button_authors)

        pygame.draw.rect(screen, (125, 125, 125), button_exit)

        if language_choise == "Englis":
            start = "Start"
            settings = "Settings"
            authors = "Authors"
            Exit = "Exit"
        else:
            start = "Играть"
            settings = "Настройки"
            authors = "Авторы"
            Exit = "Выйти"

        text_start = my_font.render(start, True, white)  # создаем объекты для текстов

        text_settings = my_font.render(settings, True, white)

        text_authors = my_font.render(authors, True, white)

        text_exit = my_font.render(Exit, True, white)

        screen.blit(text_start, (button_start.x + 32, button_start.y + 10))  # размещаем тексты

        screen.blit(text_settings, (button_settings.x + 12, button_settings.y + 10))

        screen.blit(text_authors, (button_authors.x + 26, button_authors.y + 10))

        screen.blit(text_exit, (button_exit.x + 34, button_exit.y + 10))

    if screens == 2:
        # Работа со временем (считаем паузу)
        active_time = pygame.time.get_ticks()  # текущее время с начала работы приложения
        if active_time >= active_time_plus_05_sec:
            active_time_plus_05_sec += animation_speed
            if one_or_two_or_three >= 2:
                one_or_two_or_three = 0
            one_or_two_or_three += 1
            batx += 20

        if one_or_two_or_three == 1:
            screen.blit(bat, (batx, baty))
        elif one_or_two_or_three == 2:
            screen.blit(bat1, (batx, baty))
        if batx >= 801:
            batx -= 901
            baty += 75
        if baty >= 601:
            baty = 0
        if active_time >= sun_fall_time: # если после нажатия кнопки играть прошло 10 секунд/появление солнца раз в 10 секунд
            sun_fall_time += 10000 # считаем, во сколько будет следующее появление солнца
            sunx = random.randint(50, 750)
            suny = random.randint(50, 500)
        screen.blit(little_sun, (sunx, suny))
        for temp in zombie_list:
            temp.draw(screen)


    pygame.display.update()  # обновить экран (fps)
