import pymssql
import os
# Определяем текущее незанятое имя экспортного файла
files = os.listdir("data\\export")
max = 0
for file in files:
    version = int(file.split("_")[1].replace(".csv",""))
    if version > max:
        max = version
max += 1

outputfile = f"data\\export\\expensive_{max}.csv"

PATTERN = input("Введите паттерн поиска и нажмите энтер: ")

connection = pymssql.connect(
    server="yand.dyndns.org",
    database="AdventureWorks",
    user="northwind",
    password="northwind"
    )

sql = f"""
    select TOP 5 ProductID, Name, ProductNumber, ListPrice 
    from Production.Product
    where Name like '%{PATTERN}%'
"""

cursor = connection.cursor()
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()

connection.close()

# print(results)
f = open(outputfile,"w",encoding="UTF-8")
f.write('id;name;code;price\n')
for product in results:
    id = product[0]
    name = product[1]
    code = product[2]
    price = product[3]
    f.write(f'{id};{name};{code};{price}\n')
    # print(f'{id:5}\t{name:35}\t{code:10}\t{price}')

f.close()

os.system(f"start excel {outputfile}")

# Написать код, который сформирует 
# файл в data\expensive.csv, цена которых больше тысячи
