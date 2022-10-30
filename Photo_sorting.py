from pathlib import Path
import os
import shutil
from datetime import datetime
import time

# Делаем поиск дубликатов

p = Path.cwd() # получем путь к папке с фотографиями

backslash_space = '\ '
backslash = backslash_space[:1] # Костыль

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'] # Массив с назвниями месцев
month_number = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] # Месяц в виде чисел
year = [] # Пока что пустой массив с годами

folders_name = [] # Массив для наименования папок
photo_folder = 1 # Гарантирует создание папки "Фотографии"

screenshot_folder = int(input('Нужна ли отдельная папка для скриншота (работает для самсунгов) (1 - да, 0 - нет): '))


print('Вводите года через Enter, а когда закончите введить 0')

number = 1

check = '1234567890'

while number != 0: # Защита от букв и дубликатов
    number = input('Введите год: ')
    if number == '0':
        break
    for i in range(0, len(str(number))):
        if str(number)[i] not in check:
            print('Ошибка. Вы можете использовать только цифры. Попробуйте ещё раз')
            break
        if int(number) not in year:
            year.append(int(number)) # Даём пользователю ввести года, который записывем в массив year


start_time = time.time() # Начинаем измерять время работы программы


video = list(p.glob('*.mp4')) # Массив с видео
if screenshot_folder == 1:
    screenshot = list(p.glob('Screenshot*.jpg'))


if len(video) > 0: # Авто создание папки с видео (проверка)
    video_folder = 1
else:
    video_folder = 0


if photo_folder == 1: # Создаём массив с наименованиями папок
    folders_name.append('Фотографии')
if video_folder == 1:
    folders_name.append('Видео')
if screenshot_folder == 1:
    folders_name.append('Скриншоты')


def folder_create():
    for j in folders_name:
        create_folder = str(str(Path.cwd()) + backslash + j)
        os.makedirs(create_folder)  # Создаём папку

        for f in range(0, len(year)):
            path_year = str(str(Path.cwd()) + backslash + j + backslash + str(year[f]))
            os.makedirs(path_year)  # Создаём папки года

        for g in range(0, len(year)):
            for h in range(0, len(month)):
                newpath = str(str(Path.cwd()) + backslash + j + backslash + str(year[g]))
                path = str(newpath + backslash + str(month[h]) + ' ' + str(year[g]))
                os.makedirs(path)  # Создаём папки с месяцами в папках с годами


def sorting(type, d, list):
    data_full = datetime.utcfromtimestamp(os.path.getmtime(list[d])).strftime('%Y-%m')  # Получение дата и её преобразование
    filedate = str(str(data_full[:4]) + str(data_full[5:7]))
    for file_year in range(0, len(year)):
        if filedate[:4] == str(year[file_year]):
            for file_month in range(0, len(month_number)):
                if filedate[4:] == str(month_number[file_month]):
                    shutil.move(str(list[d]), str(str(Path.cwd()) + backslash + type + backslash + str(year[file_year]) + backslash + str(month[file_month])) + ' ' + str(year[file_year]))


def camera_sort(): # функция сортировки камеры
    for d in range(0, len(photo)):
        sorting(folders_name[0], d, photo)


def video_sort(): # функция сортировки видео
    for d in range(0, len(video)):
        sorting(folders_name[1], d, video)


def screenshot_sort(): # функция сортировки скриншотов
    for d in range(0, len(screenshot)):
        sorting(folders_name[2], d, screenshot)


folder_create() # Создаём папки

if screenshot_folder == 1: # Скриншоты (создание папки + сортировка)
    screenshot_sort()
photo = list(p.glob('*.jpg')) + list(p.glob('*.jpeg')) + list(p.glob('*.png')) + list(p.glob('*.tiff'))# Создаём массив состоящий из путей к фотографиям
camera_sort()
video_sort()

print("Время работы программы: %s секунд" % (time.time() - start_time))