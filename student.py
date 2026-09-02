class Student:
    def __init__(self, studentId, name):
        self.studentId = studentId
        self.name = name
        self.marks = []

    def addMark(self, mark):
        self.marks.append(mark)

    def averageMark(self):
        if not self.marks:
            return None

        return sum(self.marks) / len(self.marks)

    def toString(self):
        marks_text = ", ".join(
            str(mark) for mark in self.marks
        )

        average = self.averageMark()

        if average is None:
            average_text = "N/A"
            marks_text = "No marks"
        else:
            average_text = f"{average:.2f}"

        return (
            f"ID: {self.studentId} | "
            f"Name: {self.name} | "
            f"Marks: {marks_text} | "
            f"Average: {average_text}"
        )