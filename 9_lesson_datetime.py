import datetime as dt

# now = dt.datetime.now()
# print(now)

# today = dt.date.today()
# print(today)

# Сколько дней осталось до Нового Года?
# today = dt.date.today()
# newyear = dt.date(today.year + 1 , 1,1)
# tillNewYear = newyear - today
# daysLeft = tillNewYear.days
# print(f"До НГ осталось: {daysLeft} дн.")

# Оформите вычисление числа дней до НГ в виде функции

def daysToNYleft():
    today = dt.date.today()
    newyear = dt.date(today.year + 1 , 1,1)
    tillNewYear = newyear - today
    daysLeft = tillNewYear.days
    return daysLeft
    
print(f"До НГ осталось: {daysToNYleft()} дн.")

def daysToNYFromStatusDate(StatusDate = dt.date.today()):
    newyear = dt.date(StatusDate.year + 1 , 1,1)
    tillNewYear = newyear - StatusDate
    daysLeft = tillNewYear.days
    return daysLeft

print(f"До НГ осталось: {daysToNYFromStatusDate(dt.date(2022,1,1))} дн.")
print(f"До НГ осталось: {daysToNYFromStatusDate()} дн.")

