# -*- coding: utf8 -*-
from random import *

def is_valid(num):
    return num.isdigit() and 1 <= int(num) < 100


new_123 = "да"
while new_123 == "да".lower():
    a = randint(1, 100)
    answer = 0
    print('Угадвайте число от 0 до 100')
    i = 0
    while answer != a:
        answer = input()
        if is_valid(answer):
            answer = int(answer)
            i = i + 1
            if answer == a:
                print("верно! ВЫ победитель вы угадали за ", i, "попыток", end = ' ')
                if i < 7:
                    print('это большая редкость вы победитель по жизни)')
                print('Если ты хочешь сыграть ещё раз напиши "да" если не хочешь "нет" ')
                new_123 = input().lower()
                if new_123 != "да":
                    print(" Спасибо за игру, до встречи")
                else:
                    print("Отлчно!))")
            if answer < a:
                print("Слишком мало, попробуйте еще раз")
            elif answer > a:
                print("Слишком много, попробуйте еще раз")
            if i % 10 == 0 and i != 1:
                print("Напоминаю вам, введите число от 1 до 100 включительно. И найтиде загаданное. Можно действовать исключая промежутки. ")
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
