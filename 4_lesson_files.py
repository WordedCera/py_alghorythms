f = open("data/people.csv", encoding="UTF-8")
text = f.read()
f.close()
lines = text.split("\n")
# print(lines)

#Разберите lines в тексты типа: "Yuri Andrienko has salary 123456"
data2 = []
for names in lines:
    dict = names.split(";")
    data2.append(dict)

max_salary = data2[0][2]
max_name = data2[0][1]
for richest in data2:
    if int(richest[2]) > int(max_salary):
        max_salary = richest[2]
        max_name = (f'{richest[1]} {richest[0]}') 

# print(f'{max_name} has salary {max_salary}')
print(" ")
# добавить еще однонго человек и высислить макс зп нескольких

data2.append(['Vasily','Vasiliev','300000'])
data2.append(['Petya','Petkin','300000'])


max_salary = data2[0][2]
max_name = data2[0][1]
second_max = None
second_name = None
for richest in data2:
    if int(richest[2]) > int(max_salary):
        second_max = max_salary
        second_name = max_name
        max_salary = richest[2]
        max_name = (f'{richest[1]} {richest[0]}')
    elif int(richest[2]) == int(max_salary):
        second_max = richest[2]
        second_name = richest[0] + ' ' + richest[1]

print(f'{max_name} has salary {max_salary}')
print(f'{second_name} has salary {second_max}')
print(" ")

maxsalary = 0
for person in data2:
    if int(person[2]) > int(maxsalary):
        maxsalary = person[2]

print("Максимальная зарплата: " + maxsalary)
print("Список людей с максимальной зарплатой")
for person in data2:
    if int(person[2]) == int(maxsalary):
        print(f'{person[0]} {person[1]}')

# Вывести информацию о людях в другой файл в формате: Имя, табуляция, фамилия, зарплата

f = open("data/people1.csv", "w", encoding="UTF-8")
for person in data2:
    f.write(f"{person[1]}\t{person[0]}\t{person[2]}\n")
f.close()


f = open("data/people_rich.csv", "w", encoding="UTF-8")
f.write("Максимальная зарплата: " + maxsalary + "\n")
f.write("Список людей с максимальной зарплатой \n")
for person in data2:
    if int(person[2]) == int(maxsalary):
        f.write(f'{person[0]} {person[1]} \n')

f.close()