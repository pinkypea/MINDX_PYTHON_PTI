class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.title = None

    def add_score(self, score):
        self.scores.append(score)

    def calculate_title(self):
        total_score = (self.scores[0] + self.scores[1] + self.scores[2]) + (self.scores[3] + self.scores[4]) * 2 + self.scores[5] * 3
        total_score /= 10

        if total_score > 8:
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

# Tạo một danh sách học sinh
student_list = StudentList()

# Thêm các học sinh vào danh sách
student1 = Student("Nguyen Van A", [8, 7, 9, 8, 9, 8])
student1.calculate_title()

student2 = Student("Tran Thi B", [6, 7, 5, 8, 7, 8])
student2.calculate_title()

student3 = Student("Hoang Duc C", [5, 6, 6, 4, 7, 8])
student3.calculate_title()

student_list.add_student(student1)
student_list.add_student(student2)
student_list.add_student(student3)

# In thông tin của từng học sinh trong danh sách
for student in student_list.students:
    print(f"Học sinh: {student.name}, Điểm: {student.scores}, Danh hiệu: {student.title}")
