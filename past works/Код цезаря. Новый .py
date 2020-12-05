# -*- coding: utf8 -*-
def is_valid_ansver():
    #защита. Проверяет ш или д . Выводит True или False
    text = input()
    while text != 'ш' and text != 'д':
        print("пожалуйста введите конкретно, 'ш' или 'д'. Мы хотим вам помочь ")
        text = input().lower()
        continue
    if text.lower() == 'ш':
        return True
    else:
        return False

def is_valid_and_int():
    #защита. Проверяет цифры ли введены. Выводим в int()
    num = input()
    while True:
        if num.isdigit():
            return int(num)   
        else:
            print('Напоминаю нужно ввести простое число')
            num = input()

def again_line(alphabet1, alphabet2, ind_sing, text, shift):        #взять отстаток от деления на 26 и посмотреть будет ли входить
    if text[ind_sing] in alphabet1:
        alphabet = alphabet1
    elif  text[ind_sing] in alphabet2:
        alphabet = alphabet2
    else:
        return text[ind_sing]
        
    if shift >= 0:
        ind_new = alphabet.find(text[ind_sing]) + shift                              #shift при положительном (кодировани)
        while ind_new >= len(alphabet):
            ind_new = ind_new - (len(alphabet))
        return alphabet[ind_new]                     # выводит числа с учетом преобразования. 
    if shift < 0:                                               #shift при отрицательном (декодировани)
        ind_new = alphabet.find(text[ind_sing]) + shift

        while ind_new < 0:
            ind_new = ind_new + (len(alphabet))
        
        return alphabet[ind_new]             


    


eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"



    
print("Привет! Это программа шифрования цезаря")

while True:
    print('Шифрование или дешифрование?, ответте "ш" или "д"')
    code = is_valid_ansver()
    
    print('Русский или Английский ? Ответ записывать в форме "Р" или "А"? ')
    leng = input().lower()

    print("шаг сдвига, ввести простое число")
    shift = is_valid_and_int()

    if not code:
        shift = -shift

    if code:
        print('Ведите текст который будем шифровать'  ) 
    else:
        print('Ведите текст который будем дeшифровать'  )
    text = input()
    
    answer = ""
    for j in range(len(text)):
        if leng == 'р':  
            alphabet1 = rus_lower_alphabet
            alphabet2 = rus_upper_alphabet
            answer += again_line(alphabet1, alphabet2, j, text, shift)
        else:
            leng == 'а'
            alphabet1 = eng_lower_alphabet
            alphabet2 = eng_upper_alphabet
            answer += again_line(alphabet1, alphabet2, j, text, shift)            
        # если русский алфавит.
  
    print(answer)
    print("Нужно расшифровать ещё? Да, нет" )
    text = input().lower()
    if text == "да":
        continue
    else:
        print('спасибо, да прибудет сила')
        break