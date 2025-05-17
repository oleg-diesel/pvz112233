import pygame  # импортируем всю БИБЛИОТЕКУ pygame
import random
from class_zombie import Zombie # импортировали класс зомби из скрипта
from class_squares import Squares
from class_plants import Plants
pygame.init()  # инициализация всех модулей Pygame

width, height = 800, 600  # высота и ширина
screen = pygame.display.set_mode((width, height))  # создали окно 800x600


cell_active_list = []
check = 0
sunflower_list = []
peashooter_list = []
kolichestvo_solnc = "0" # переменная для подсчета количества солнц


current_frame = 1 # переменная для отслееживания кадра (1 из 3 включительно)
animation_speed = 250 # скорость анимации в милисекундах
sun_fall_time = 0
first_sun_appearance = 0
last_update_time = pygame.time.get_ticks()

zombie_line = [500, 400, 300, 200, 100]
zombie_list = []
for temp in range(20):
    newzombie = Zombie(10, 1,random.randint(1500, 15000), random.choice(zombie_line), 0.017)
    zombie_list.append(newzombie)


setka_kol_vo_ravno_1 = Squares(5, 7, 100, False)
setka_kol_vo_ravno_1.create_square()

batx = 0
baty = 0
sunx = 801
suny = 0


little_sun = pygame.image.load("pictures/aaaa.png").convert_alpha()
little_sun = pygame.transform.scale(little_sun, (100, 100))
chose_tab = pygame.image.load("pictures/ChooserBackground.png")
chose_tab = pygame.transform.scale(chose_tab, (800, 100))
peashooter_card = pygame.image.load("pictures/card_peashooter.png")
sunflower_card = pygame.image.load("pictures/card_sunflower.png")
you_lose = pygame.image.load("pictures/img.png")
you_lose = pygame.transform.scale(you_lose, (800, 600))

# rect объекты для картинок
little_sun_rect = pygame.Rect(sunx, suny, 70, 73)


start = ""
settings = ""
authors = ""
Exit = ""

screens = 1

one_or_two_or_three = 1
one_or_two_card = 0


pygame.font.init()  # инициализация модуля для работы со шрифтом
my_font = pygame.font.SysFont('Comic Sans MS', 25)  # создаем шрифт для кнопок
my_little_font = pygame.font.SysFont('Comic Sans MS', 16)

white = (255, 255, 255)
black = (0, 0, 0)

# раздел для создания текста

# раздел для создания кнопок

button_start = pygame.Rect(50, 50, 150, 50)  # создаем прямоугольник для кнопки

button_settings = pygame.Rect(50, 150, 150, 50)

button_authors = pygame.Rect(50, 250, 150, 50)

button_exit = pygame.Rect(50, 350, 150, 50)

button_test = pygame.Rect(150, 50, 150, 50)

logic = False
active = False
card_type = 0 # 2 параметр, для удобного выбора карт без лишнего спама в консоли

active_time_plus_05_sec = pygame.time.get_ticks() + 250 # считаем время следующей анимации


language_choise = "English"

clock = pygame.time.Clock()

# игровой цикл

while logic == False:  # создали бесконечный цикл
    clock.tick(165) # ограничение фпс

    for event in pygame.event.get():  # обработка всех событий
        if event.type == pygame.QUIT:  # если событие - выход
            logic = True

        #проверяем нажатие мыши
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coordinaty_nazhatiya = event.pos
            #print(coordinaty_nazhatiya)
            #print(type(coordinaty_nazhatiya))
            xtap = coordinaty_nazhatiya[0]
            ytap = coordinaty_nazhatiya[1]
            if screens == 1:
                if button_start.collidepoint(coordinaty_nazhatiya): # сделали проверку нажатия с помощью метода collidepoint
                    screens = 2
                sun_fall_time = pygame.time.get_ticks() + 10000 # посчитали во сколько появится солнце
            elif screens == 2:
                if xtap >= 125 and xtap <= 190 and ytap >= 6 and ytap <=71 and active != True and int(kolichestvo_solnc) >= 100:
                    print("вы нажали на карточку горохострела!")
                    card_type = 1
                    active = True
                elif xtap >=190 and xtap <=254 and ytap >= 6 and ytap <=71 and active != True and int(kolichestvo_solnc) >= 50:
                    print("вы нажали на карточку подсонуха!")
                    card_type = 2
                    active = True
                elif little_sun_rect.collidepoint(coordinaty_nazhatiya):
                    sunx = -100
                    kolichestvo_solnc = int(kolichestvo_solnc)
                    kolichestvo_solnc += 25
                    kolichestvo_solnc = str(kolichestvo_solnc)
                    print("вы нажали на солнце")

                # проверяем каждую клетку из списка клеток
                for cell_click in setka_kol_vo_ravno_1.cells_list:
                    # проверяем было ли нажатие по клетке и занята ли она
                    if cell_click[0].collidepoint(coordinaty_nazhatiya) and cell_click[1] == False:
                        if card_type == 1:
                            newplant = Plants(5, 0, 'peashooter', 100, False, True, cell_click[0].x, cell_click[0].y)
                            peashooter_list.append(newplant)
                            cell_click[1] = True
                            kolichestvo_solnc = int(kolichestvo_solnc)
                            kolichestvo_solnc -= 100
                            kolichestvo_solnc = str(kolichestvo_solnc)
                            card_type = 0
                            active = False
                        elif card_type == 2:
                            newplant = Plants(3, 0, 'sunflower', 50, True, False, cell_click[0].x, cell_click[0].y)
                            sunflower_list.append(newplant)
                            cell_click[1] = True
                            kolichestvo_solnc = int(kolichestvo_solnc)
                            kolichestvo_solnc -= 50
                            kolichestvo_solnc = str(kolichestvo_solnc)
                            card_type = 0
                            active = False
        # если событие = нажатие клавиши
        elif event.type == pygame.KEYDOWN and active == True:
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

        text_solnca = my_little_font.render(kolichestvo_solnc, True, black)

        setka_kol_vo_ravno_1.draw_square(screen)
        # Работа со временем (считаем паузу)
        active_time = pygame.time.get_ticks()  # текущее время с начала работы приложения
        if active_time >= sun_fall_time: # если после нажатия кнопки играть прошло 20 секунд/появление солнца раз в 20 секунд
            sun_fall_time += 8000 # считаем, во сколько будет следующее появление солнца
            sunx = random.randint(50, 700)
            suny = random.randint(50, 500)
            little_sun_rect.x = sunx
            little_sun_rect.y = suny
        screen.blit(little_sun, (sunx, suny))
        screen.blit(chose_tab, (0, 0))
        kolichestvo_solnc = int(kolichestvo_solnc)
        if kolichestvo_solnc <=9:
            kolichestvo_solnc = str(kolichestvo_solnc)
            screen.blit(text_solnca, (55, 75))
        elif kolichestvo_solnc >= 10 and kolichestvo_solnc <=99:
            kolichestvo_solnc = str(kolichestvo_solnc)
            screen.blit(text_solnca, (50, 75))
        elif kolichestvo_solnc >= 100 and kolichestvo_solnc <=999:
            kolichestvo_solnc = str(kolichestvo_solnc)
            screen.blit(text_solnca, (45, 75))
        elif kolichestvo_solnc >= 1000:
            kolichestvo_solnc = str(kolichestvo_solnc)
            screen.blit(text_solnca, (40, 75))
        screen.blit(peashooter_card, (125, 6))
        screen.blit(sunflower_card, (190, 6))
        for cell, plant in cell_active_list:
            plant.draw(screen)
        for temp in zombie_list:
            temp.move()
            temp.draw(screen)
            if newzombie.x <= 50:
                screen.blit(you_lose, (0, 0))

        # циклы для отрисовки растений списка
        for GOPOX in peashooter_list:
            GOPOX.draw(screen)
        for CBETOK_COLNCE in sunflower_list:
            CBETOK_COLNCE.draw(screen)

    pygame.display.update() # обновить экран (fps)