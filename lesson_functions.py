# скриптовый стиль
# a = 3
# b = 4

# c = (a*a + b*b) ** 0.5
# print(c)


# Процедурный стиль: то, что используется многократно, оформляется в виде функции

def hypot(a,b):
    c = (a * a + b * b) ** 0.5
    return c

def square(a,b):
    c = (a * b)/2
    return c
# Для исключения действий внутри моделя (если не нудно чтобы, все из этого модул отрабатывало в вдругом файле)
if __name__ == "__main__":

    print(hypot(3,4))
    a = 123
    print(a)
    x1 = 11
    x2 = 13
    s = square(x1,x2)

    print(s)