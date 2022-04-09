# Типичный класс. для него валтдно понятия объекта. Для него валидно понятие объекта (экземпляр класса)

class MyGeometry:
    # Конструктор класса
    # он вызывается, когда создается экземпляр класса
    # слово self в заголовоке конструктора - это скорее маркер принадлежности к объекту
    # это скорее маркер принадлежности объекту, чем аргумент функции
    def __init__(self):
        # Это называется поле класса (свойство класса)
        self.noneuqluid = 1.0

    # Это метод [экземпляра] класса
    def hypot(self,a,b):
        c = (a*a + b*b)**0.5 * self.noneuqluid
        return c
            
    def square(self,a,b):
        return a*b/2 * self.noneuqluid

if __name__ == "__main__":
    # создаем экземпляры нужного класса
    g1 = MyGeometry()
    g2 = MyGeometry()
    g2.noneuqluid = 1.1
    g3 = MyGeometry()
    g3.noneuqluid = 0.9
    print(g1.hypot(3,4))
    print(g2.hypot(3,4))
    print(g3.square(3,4))
    