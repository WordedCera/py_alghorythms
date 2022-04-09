# Вывести все слова русского словаря, которые начинаются на первые три ьуквы имени и подсчитать
pattern = "иго"
file = "data/RusDictionary.txt"
# для файнд вхождение вначале
# есть startswith

def DictSearcherStart(pattern,file):
    dict = []
    d = open(file, "r", encoding="UTF-8")
    text = d.read()
    d.close()
    lines = text.split("\n")
    l = len(pattern)
    for word in lines:
        if word[0:l] == pattern:
            dict.append(word)
    return dict


def DictSearcherExist(pattern,file):
    dict = []
    d = open(file, "r", encoding="UTF-8")
    text = d.read()
    d.close()
    lines = text.split("\n")
    for word in lines:
        if word.find(pattern) >= 0:
            dict.append(word)
    return dict

# print(f'Количество найденных слов {len(DictSearcherExist(pattern,file))}')
# for i in DictSearcherExist(pattern,file):
#     print(i)
# Вывести все слова, которые заканчиваются на "цо"
konetz = "цо"

def DictSearcherEnding(pattern,file):
    dict = []
    d = open(file, "r", encoding="UTF-8")
    text = d.read()
    d.close()
    lines = text.split("\n")
    for word in lines:
        if word.endswith(pattern):
            dict.append(word)
    return dict

# print(len(DictSearcherEnding(konetz,file)))
# for i in DictSearcherEnding(konetz,file):
#     print(i)

# Дано несколько паттернов, из списков. Для каждого из паттернов вывести текст: паттерн: кол-во число начинающихся 
patterns = ["але","иго","юри"]

for p in patterns:
    print(f'Кол-во слов начинающихся с "{p}" = {len(DictSearcherStart(p,file))}')

# Найти самое длинное слово в русском языке

def maxLength(file):
    dict = []
    d = open(file, "r", encoding="UTF-8")
    text = d.read()
    d.close()
    lines = text.split("\n")
    l = len(pattern)
    for word in lines:
        dict.append(word)
    max_word = dict[0]
    word_number = 1
    dict2 = []
    for i in dict:
        word_number += 1
        if len(i) > len(max_word):
            max_word = i
            max_number = word_number
    for e in dict:
        if len(e) == len(max_word):
            dict2.append(e)
    woord = str(max_number) + " " + max_word + " и слова: "
    return woord

s = "qwertyuio"
# первый символ
print(s[1])
# с второго символа до 3 
print(s[1:3])
# c первого символа до начала
print(s[1:])
# второй символ
print(s[1:7:2])
print(s[1::2])
print(s[::2])
print(s[-1])
print(s[:-1])
print(s[::-1])

nums = [1,2,3,4,5,6]
print(nums[1:3])
print(nums[::-1])

# найти в русском словаре слова перевертыши пллаиндромы


def palindrome(file):
    dict = []
    d = open(file, "r", encoding="UTF-8")
    text = d.read()
    d.close()
    lines = text.split("\n")
    for word in lines:
        if word == word[::-1] and len(word)>1:
            dict.append(word)
    return dict

# print("")
# print(palindrome(file))

# Найти слова в русском языке, в которых больше всего букв л

dict = []
d = open(file, "r", encoding="UTF-8")
text = d.read()
d.close()
words = text.split("\n")
for word in words:
    dict.append(word)

def countPattern(word, pattern):
    counter = 0
    for letter in word:
        if letter == pattern:
            counter += 1
    return counter

pattern = "л"

maxPattern = 0
for w in words:
    if countPattern(w,pattern) > maxPattern:
        maxPattern =countPattern(w,pattern)
print(maxPattern)

for w in words:
     if countPattern(w,pattern) == maxPattern:
         print(w)

# Какая буква в каком слове русского языка встречается наибольшее число раз?
abc = 'абвгдежзиклмнопрстуфхцчшщъыьэюя'
bestWord = ""
bestLetter =  abc[0]
for pattern in abc:
    for w in words:
        if countPattern(w,pattern) > countPattern(bestWord, bestLetter):
            bestWord = w
            bestLetter = pattern
print(bestWord, bestLetter, countPattern(bestWord, bestLetter))