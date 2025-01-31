import pygame  # импортируем всю БИБЛИОТЕКУ pygame
import random
from class_zombie import Zombie # импортировали класс зомби из скрипта
from class_squares import Squares
from class_plants import Plants
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
for temp in range(1):
    newzombie = Zombie(300, 1,1500, random.choice(zombie_line), 0.017, png=("pictures/zombie1.png"))
    zombie_list.append(newzombie)

setka_kol_vo_ravno_1 = Squares(5, 7, 100)

regular_plant = Plants(6, 1, "pictures/Peashooter_0.png", "peashoter", 100, False, 100, 100)

batx = 0
baty = 0
sunx = 801
suny = 0


little_sun = pygame.image.load("pictures/aaaa.png").convert_alpha()
little_sun = pygame.transform.scale(little_sun, (100, 100))
chose_tab = pygame.image.load("pictures/ChooserBackground.png")
chose_tab = pygame.transform.scale(chose_tab, (800, 100))
peashoter_card = pygame.image.load("pictures/card_peashooter.png")
sunflower_card = pygame.image.load("pictures/card_sunflower.png")

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
active = False

active_time_plus_05_sec = pygame.time.get_ticks() + 250 #считаем время следующей анимации


language_choise = "English"

# игровой цикл

while logic == False:  # создали бесконечный цикл

    for event in pygame.event.get():  # обработка всех событий
        if event.type == pygame.QUIT:  # если событие - выход
            logic = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coordinaty_nazhatiya = event.pos
            xtap = coordinaty_nazhatiya[0]
            ytap = coordinaty_nazhatiya[1]
            if screens == 1:
                if xtap >= 50 and xtap <= 200 and ytap >= 50 and ytap <= 100:
                    screens = 2
                sun_fall_time = pygame.time.get_ticks() + 10000 # посчитали во сколько появится солнце
            elif screens == 2:
                if xtap >= 125 and xtap <= 190 and ytap >= 7 and ytap <=72 and active != True:
                    print("вы нажали на карточку горохострела!")
                    active = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:  # Проверяем, нажата ли "Z"
                active = False
                print("вы отменили выбор карточки!")
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

        setka_kol_vo_ravno_1.draw_square(screen)
        # Работа со временем (считаем паузу)
        active_time = pygame.time.get_ticks()  # текущее время с начала работы приложения
        if active_time >= sun_fall_time: # если после нажатия кнопки играть прошло 20 секунд/появление солнца раз в 20 секунд
            sun_fall_time += 20000 # считаем, во сколько будет следующее появление солнца
            sunx = random.randint(50, 700)
            suny = random.randint(50, 500)
        screen.blit(little_sun, (sunx, suny))
        for temp in zombie_list:
            temp.move()
            temp.draw(screen)
        regular_plant.draw(screen)
        screen.blit(chose_tab, (0, 0))
        screen.blit(peashoter_card, (125, 7))
        screen.blit(sunflower_card, (215, 7))


    pygame.display.update()  # обновить экран (fps)
