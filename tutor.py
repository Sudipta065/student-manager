from student import Student


class Tutor:
    def __init__(self, tutorId, name, unitCode):
        self.tutorId = tutorId
        self.name = name
        self.unitCode = unitCode
        self.students = []

    def enrolStudent(self, studentId, name):
        if self.findStudent(studentId) is not None:
            print(
                f"Error: student ID {studentId} "
                "is already enrolled."
            )
            return False

        student = Student(studentId, name)
        self.students.append(student)

        print(
            f"Student {name} ({studentId}) "
            "enrolled successfully."
        )
        return True

    def findStudent(self, studentId):
        for student in self.students:
            if student.studentId == studentId:
                return student

        return None

    def displayAll(self):
        if not self.students:
            print("No students are enrolled.")
            return

        print(f"\nStudents in {self.unitCode}")
        print("-" * 60)

        for student in self.students:
            print(student.toString())

    def classStatistics(self):
        all_marks = []

        for student in self.students:
            all_marks.extend(student.marks)

        if not all_marks:
            print("No marks have been recorded.")
            return None

        highest = max(all_marks)
        lowest = min(all_marks)
        class_average = sum(all_marks) / len(all_marks)

        print("\nClass statistics")
        print(f"Highest mark: {highest}")
        print(f"Lowest mark: {lowest}")
        print(f"Class average: {class_average:.2f}")

        return highest, lowest, class_average