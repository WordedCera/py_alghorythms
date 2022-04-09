# Манипуляции со списком
from re import I, L


data = [5,2,3,1,333,4,2]
data.append(555)
data.pop(1)

# print(data)
# print(data[1])
# print(len(data))

# Перебор всех членов списка: оператор цикла
# Пронумеруем

# i = 1
# for x in data:
#     print(i,x)
#     # i = i + 1
#     i += 1
# И сгенерируем новый список, в котором каждый член равен квадратам старого
# data2 = []
# for x in data:
#     i = x**2
#     data2.append(i)


# l = 1
# for x in data2:
#     print(l,x)
#     # i = i + 1
#     l += 1

# Вывести из списка только те числа, которые больше ста
# for x in data:
#     if x > 100:
#         print(x)

# Вывести из списка только четные числа
# for x in data:
#     if x % 2 == 0:
#         print(x)

# Вывести из списка только числа, которые больше 1000 или текст, что таких нет
# counter = 0
# for x in data:
#     if x > 1000:
#         print(x)
#         counter += 1

# if counter == 0:
#     print("нет таких чисел")

# Сумма всех чисел в списке
# sum = 0
# for x in data:
#     sum += x

# print(sum/len(data))

# Найти минимальное число в списке
min = data[0]
for x in data:
    if x < min:
        min = x

print(min)