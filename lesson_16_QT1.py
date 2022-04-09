from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

class HelloWindow(QWidget):
    def __init__(self):
        # супер - отсылка к предку
        # Вызов конструктора класса предка (QWidget)
        super().__init__()
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        self.setWindowTitle("Hello")

        # не маркер, а указание родительсокошо элемента
        self.btn1 = QPushButton(self)
        self.btn1.setGeometry(210,110,60,40)
        self.btn1.setText("+")
        self.btn1.clicked.connect(self.btn_click1)

        self.btn2 = QPushButton(self)
        self.btn2.setGeometry(10,110,60,40)
        self.btn2.setText("-")
        self.btn2.clicked.connect(self.btn_click2)

        self.led1 = QLineEdit(self)
        self.led1.setGeometry(10,30,280,40)

        self.led2 = QLineEdit(self)
        self.led2.setGeometry(10,70,280,40)

        self.led3 = QLineEdit(self)
        self.led3.setGeometry(10,200,280,40)

        self.show()

    def btn_click1(self):
        # print("Hello, World!")
        # self.setWindowTitle("Hello World")
        # self.btn.setText(f"Hellooooooo, {self.led.text()}")
        ans = int(self.led1.text()) + int(self.led2.text()) 
        self.led3.setText(f"{ans}")
        self.btn2.setStyleSheet("background-color: red")

    def btn_click2(self):
        # print("Hello, World!")
        # self.setWindowTitle("Hello World")
        # self.btn.setText(f"Hellooooooo, {self.led.text()}")
        ans = int(self.led1.text()) - int(self.led2.text()) 
        self.led3.setText(f"{ans}")
        self.btn2.setStyleSheet("background-color: red")


if __name__ == '__main__':
    print("Текст")
    app = QApplication([])
    window = HelloWindow()
    # btn = QPushButton(window)
    app.exec()

