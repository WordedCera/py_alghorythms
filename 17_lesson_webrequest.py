from urllib import request
import json
import time

print("My stock bot is on")
previousValue = 0
# Непрерывный цикл опроса юрл адреса
while True:
    # Получение данных (текста) с урл - одна строка
    url = "http://yand.dyndns.org/api/tickers.aspx"
    result = request.urlopen(url).read().decode("UTF-8")
    # print(result)

    stock = json.loads(result) # Десериализация - очень здорово
    # print(stock)
    # for data in stock:
    #     # print(data)
    #     print(f'Бумага {data["ticker"]} текущий курс {data["value"]}')
    # Реализация сторожа, который следит за курсом ценныз бумаг
    level = 1200

    for data in stock:
        if data["ticker"] == "GAZPOM":
            currentValue = data["value"]
            if currentValue > level and previousValue <= level:
                print(f"Текущий уровень {currentValue}")
            if currentValue <= level:
                print(f'ДУМАЙ! Текущий курс {currentValue}')
            previousValue = currentValue
    
    time.sleep(1) # Задержка на одну секунду

