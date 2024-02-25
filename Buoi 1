class Student:
    # Thuộc tính

    name = "Nguyen Van A"
    age = 13
    gender = 'Male'
    school = 'MindX Technology School'

    # Phương thức init
    def __init__(self, name, age, gender, school):
        self.name = name
        self.age = age
        self.gender = gender
        self.school = school

    # Phương thức show
    def show(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Gender = ", self.gender)
        print("School = ", self.school)

hoc_sinh_thu_nhat = Student("Le Van C", 18, "Female", "Ams")
hoc_sinh_thu_nhat.show()

#Viết class truyền vào tham số là 3 cạnh của 1 tam giác, tính chu vi tam giác đó
# Cách thứ nhất: 
class TamGiac1():
    canh1 = 5
    canh2 = 6
    canh3 = 7

tam_giac1 = TamGiac1()
chu_vi = tam_giac1.canh1 + tam_giac1.canh2 + tam_giac1.canh3
print("Chu vi =", chu_vi)

# Cách thứ hai
class TamGiac2():
    def __init__(self, canh1, canh2, canh3):
        self.canh1 = canh1
        self.canh2 = canh2
        self.canh3 = canh3
    def show(self):
        print("Chu vi =", self.canh1 + self.canh2 + self.canh3)

tam_giac_2 = TamGiac2(int(input()), int(input()), int(input()))
tam_giac_2.show()

# Ôn tập PYQT6
# Khởi tạo cửa sổ
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
import sys
app = QApplication(sys.argv)
window = QWidget()
button = QPushButton('Click me', window)
button.setGeometry(100, 100, 100, 30)
window.show()
app.exec()

