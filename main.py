class Student:
    def __init__(self, name):
        self.name = name
        self.scores = {}

    def add_score(self, subject, score):
        self.scores[subject] = score

    def average(self):
        return sum(self.scores.values()) / len(self.scores) if self.scores else 0

    def info(self):
        return f"{self.name} | O‘rtacha: {self.average():.2f}"


class ExamSystem:
    def __init__(self):
        self.students = []

    def add_student(self, s):
        self.students.append(s)

    def show(self):
        for i, s in enumerate(self.students):
            print(i, s.info())


exam = ExamSystem()

while True:
    print("\n1.Talaba 2.Ball 3.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        exam.add_student(Student(input("Ism: ")))
    elif c == "2":
        i = int(input("Index: "))
        exam.students[i].add_score(input("Fan: "), int(input("Ball: ")))
    elif c == "3":
        exam.show()
    elif c == "0":
        break
