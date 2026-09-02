from tutor import Tutor


def readMark():
    while True:
        try:
            return float(
                input("Enter mark (0-100): ")
            )
        except ValueError:
            print("Error: enter a numeric mark.")


def main():
    print("=== Student Marks Manager ===")

    tutorId = input("Enter tutor ID: ")
    tutorName = input("Enter tutor name: ")
    unitCode = input("Enter unit code: ")

    tutor = Tutor(tutorId, tutorName, unitCode)

    while True:
        print("\n1. Enrol student")
        print("2. Record mark")
        print("3. Display all students")
        print("4. Display class statistics")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            studentId = input("Enter student ID: ")
            studentName = input("Enter student name: ")

            tutor.enrolStudent(studentId, studentName)

        elif choice == "2":
            studentId = input("Enter student ID: ")
            mark = readMark()

            tutor.recordMark(studentId, mark)

        elif choice == "3":
            tutor.displayAll()

        elif choice == "4":
            tutor.classStatistics()

        elif choice == "5":
            print("Program closed.")
            break

        else:
            print("Error: choose a number from 1 to 5.")


if __name__ == "__main__":
    main()