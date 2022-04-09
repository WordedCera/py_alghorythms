import pymssql

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

print(f"{'id':5}\t{'name':35}\t{'code':10}\t{'price'}")
# print(results)
for product in results:
    id = product[0]
    name = product[1]
    code = product[2]
    price = product[3]
    print(f'{id:5}\t{name:35}\t{code:10}\t{price}')


# Написать код, который сформирует 
# файл в data\expensive.csv, цена которых больше тысячи