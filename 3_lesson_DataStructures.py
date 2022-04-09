# people = ["Yuri", "Vasya", "Masha", "Yulia", "Joe"]
# # for person in people:
# #     print(person)

# people2 = []
# people3 = []
# # Вывести только тех людей, имя которых начинается на Y
# for person in people:
#     if person[0] == "Y":
#         people2.append(person)
#     if len(person) < 5:
#         people3.append(person)

# print(people2)
# print(people3)

# person1 = "Yuri Andrienko 123456" Не годится
# person1 = ["Yuri", "Andrienko", 1233456]
# НАписать код, который выведет: "Y.Andrienko has salary 123456"
# personname = person1[0]
# print(f'{personname[0]}.{person1[1]} has salary {person1[2]}')

# people = [
#     ["Yuri", "Andrienko", 123456],
#     ["Vasya", "Pupkin", 77777],
#     ["Masha", "Mashkina", 300000]
# ]

# # for person in people:
# #     personname = person[0]
# #     print(f'{personname[0]}.{person[1]} has salary {person[2]}')

# # Найти и вывести фамилию самого высокооплачиваемого сотрудника
# max_lastname = people[1][1]
# max = people[1][2]
# for person in people:
#     if person[2] > max:
#         max = person[2]
#         max_lastname = person[1]

# print(f'{max_lastname} has salary {max}')

# Представление сущности в виде словаря

# person = {
#     "firstname": "Yuri",
#     "lastname":"Andrienko", 
#     "salary":123456
# }
        
# print(f'{person["firstname"][0]}.{person["lastname"]} has salary {person["salary"]}')

# Список словарей
people = [
    {
        "firstname":"Yuri",
        "lastname":"Andrienko",
        "salary":123456
    },
    {
        "firstname":"Vasya",
        "lastname":"Pupkin",
        "salary":77777
    },
    {
        "firstname":"Masha",
        "lastname":"Mashkina",
        "salary":300000
    }

]

for person in people:
    print(f'{person["firstname"][0]}.{person["lastname"]} has salary {person["salary"]}')
