# -*- coding: utf8 -*-

def is_valid_and_int(num):                                                         #защита. Проверяет цифры ли введены. Выводим в int()
    while True:
        if num.isdigit():
            return int(num)   
        else:
            print('Напоминаю нужно ввести простое число')
            num = input()
            

def is_valid_ansver(text):                                                         #защита. Проверяет да или нет. Выводит True или False
    while text != 'нет' and text != 'да':
        print("пожалуйста введите конкретно, 'Да' или 'нет'. Мы хотим вам помочь ")
        text = input().lower()
        continue
    if text.lower() == 'да':
        return True
    else:
        return False
    
    
    
print("Привет, я помогу тебе создать пароль. Ответь на вопросы в формате 'Да', 'Нет'")
from random import *
# строки и списки из которых будут составлены пароли. 
digi1 = '0123456789'
Alpha1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha1 = 'abcdefghijklmnopqrstuvwxyz'
sumb1 = '!#$%&*+-=?@^_.'
sing_not1 = 'il1Lo0O'




while True:
    
    print("Введите колличество паролей для генирации.")
    count = input()
    count = is_valid_and_int(count)

    print("Веедите колличество символов в паролях")
    amount = input()
    amount = is_valid_and_int(amount)
    
    print("Включать ли  цифры?")
    digi = input()
    digi = is_valid_ansver(digi)
    
    print('Включать ли прописные буквы')
    Alpha = input()
    Alpha = is_valid_ansver(Alpha)

    print('Включать ли строчные буквы?')
    alpha = input()
    alpha = is_valid_ansver(alpha)    
    
    print('Включать ли символы !#$%&*+-=?@^_?')
    symb = input()
    symb = is_valid_ansver(symb)    
    
    print('Исключать ли неоднозначные символы il1Lo0O ?')
    symb_not = input()
    symb_not = is_valid_ansver(symb_not)   
    
    chars = ''
    # формирование общей строки из которой бдут выбраны данные.
    if digi:
        chars += digi1
    if Alpha:
        chars += Alpha1
    if alpha:
        chars += alpha1
    if symb:
        chars += sumb1
    if symb_not:
        for i in range(len(sing_not1)):
            if sing_not1[i] in chars:
                find1 =  chars.find(sing_not1[i])
                chars = chars[:find1] + chars[find1+1:]     #удаление лишних элементов
    for i in range(count):                                  #создание нужного колличества паролей.
        print(*sample(chars, amount), sep = "")
    print("Нужны ли ещё пароли?")
    end = input()
    end = is_valid_ansver(end)
    if end:
        continue
    else:
        print('До встреч, да прибудет с тобой сила')
        break
        
        
        
        
                