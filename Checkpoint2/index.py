import sys
import json
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication, QDialog

class Student:
    def __init__(self, name, scores, title=None):
        self.name = name
        self.scores = scores
        self.title = title

    def calculate_title(self):
        total_score = (self.scores[0] + self.scores[1] + self.scores[2]) + (self.scores[3] + self.scores[4]) * 2 + self.scores[5] * 3
        total_score /= 10

        if total_score > 8 and total_score <= 10:
            self.title = "Giỏi"
        elif total_score > 6.5:
            self.title = "Khá"
        elif total_score > 4:
            self.title = "Trung bình"
        else:
            self.title = "Không xác định"

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def load_data_from_json(self, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            for student_data in data:
                student = Student(student_data['name'], student_data['scores'])
                self.add_student(student)
    
    def save_data_to_json(self, file_path):
        data = []
        for student in self.students:
            data.append({
                'name': student.name,
                'scores': student.scores,
                'title': student.title
            })
        with open(file_path, 'w') as file:
            json.dump(data, file)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("dialog.ui", self)
        self.setWindowTitle("Danh sách học sinh")
        # Tạo danh sách học sinh
        student_list = StudentList()
        # Đọc dữ liệu từ file JSON
        student_list.load_data_from_json("student.json")
        for student in student_list.students:
            student.calculate_title()
            student_list.save_data_to_json("student.json")
        for student in student_list.students:
            self.ui.listWidget_1.addItem(student.name)
            self.ui.listWidget_2.addItem(student.title)
        self.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
