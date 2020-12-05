#делал не зная регулярные выражения
# В условии было сказно что нужно оставить ' и текст может быть без букв. В таком случае вывести []
#код требует оптимизакции. Но работает.


def top_3_words(text):
    sum_alpha = 0
    for i in text:
        if i.isalpha():
            sum_alpha += 1
    if sum_alpha == 0:
        return []

    text1 = ''
    for i in text:
        if i.isalpha() or i == "'":
            text1 += i
        else:
            text1 += ' '

    list_word = text1.lower().split()
    dict1 = dict()
    for i in list_word:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    s = []
    Dsort = sorted(dict1, key=lambda x: (-dict1[x], x))

    count_answer = min(3, len(dict1))
    for i in range(count_answer):
        s.append(Dsort[i])
    return s


text = ""
print(top_3_words(text))