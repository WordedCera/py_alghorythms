from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextEdit
from datalayer import Repository

class ProductWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setFixedSize(600,600)
        self.setWindowTitle("Products")

        self.txtFilter = QLineEdit(self)
        self.txtFilter.setGeometry(20,20,560,60)
        self.txtFilter.textChanged.connect(self.ShowProducts)

        self.txtDisplay = QTextEdit(self)
        self.txtDisplay.setGeometry(20,100,560,450)
        self.show()
    
    def ShowProducts(self):
        repository = Repository()
        products = repository.getFilteredProducts(self.txtFilter.text())
        out = ""
        for p in products:
            # print(p["name"])
            out += f'{p["name"]:45}\t{p["price"]}\n'
        self.txtDisplay.setText(out)


if __name__ == "__main__":
    app = QApplication([])
    window = ProductWindow()
    app.exec()
