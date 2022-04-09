# Не совсем типичный класс. Для такого класса,
# бессмысленно понятие объекта
# статический класс

class MyGeometry:

    # Это называется поле класса (свойство класса)
    noneuqluid = 1.0

    # Это метод класса
    def hypot(a,b):
        c = (a*a + b*b)**0.5 * MyGeometry.noneuqluid
        return c
            
    def square(a,b):
        return a*b/2 * MyGeometry.noneuqluid

if __name__ == "__main__":
    print(MyGeometry.hypot(3,4))
    print(MyGeometry.square(3,4))
    MyGeometry.noneuqluid = 1.1
    print(MyGeometry.hypot(3,4))
    print(MyGeometry.square(3,4))
   