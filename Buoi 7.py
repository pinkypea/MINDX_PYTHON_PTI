import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("listWidget.ui", self)
        self.ls = ["Dog", "Cat", "Duck"]
        self.ui.listWidget.addItems(self.ls)
        self.ui.listWidget.addItem("Lion")  # them phan tu vao cuoi danh sach
        self.ui.listWidget.insertItem(
            0, "Tiger"
        )  # them phan tu vao vi tri bat ky trong danh sach
        self.ui.listWidget.takeItem(3)  # xoa phan tu tai vi tri bat ky
        matched_items = self.ui.listWidget.findItems("Dog", Qt.MatchFlag.MatchContains)
        for i in range(self.ui.listWidget.count()):
            it = self.ui.listWidget.item(i)
            it.setHidden(it not in matched_items)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


