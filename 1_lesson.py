# переменная присвоения 
# x = 2
# x = (x+1) * 123 / 456
# print(x)

# конкатенация строк, имена переменных 
# s1 = "Yuri"
# s2 = 'Andrienko'
#s3 = s1 + " " + s2
#f дает возможность подстановки
# s3 = f"{s1} {s2}"
# print(s3)

# firstName = 'Yuri'
# lastName = "Andrienko"
# fullName = f"{firstName} {lastName}"

# Разборка строк + знакомство со списками
fullName = "Yuri Andrienko"
# способ №1
# spacePosition = fullName.find(" ")
# print(spacePosition)
# firstName = fullName[0:spacePosition]
# lastName = fullName[spacePosition+1:]
# print(firstName)
# print(lastName)

#Способ 2
# splitted = fullName.split(" ")
# print(splitted[0])
# print(splitted[1])

# Ветвление, условные операторы
# amount = 123
# if amount < 10:
#     print("Мало")
# if amount >= 10 and amount < 100:
#     print("В самый раз")

# if amount >= 100:
#     print("Многовато!")

# print("Анализ завершен")

# Вдруг нет пробела 
fullName = "Yuriy Andrienko"
spacePosition = fullName.find(" ")
# print(spacePosition)
if spacePosition > 0:
    firstName = fullName[0:spacePosition]
    lastName = fullName[spacePosition+1:]
    print(firstName)
    print(lastName)
else:
    print(f"Не удалось разобрать строку {fullName}")
    print(f"Не удалось разобрать строку {fullName}")