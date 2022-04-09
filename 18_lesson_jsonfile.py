import json

f = open("data/tickers.json", "r", encoding="UTF-8")
stock = json.load(f)
f.close()

print(stock)
for data in stock:
    print(f'Бумага {data["ticker"]} текущий курс {data["value"]}')

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

f = open("data/peoples.json", "w", encoding="UTF-8")
json.dump(people,f)
f.close()