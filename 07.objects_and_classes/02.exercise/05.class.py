class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        average = sum(self.grades) / len(self.grades)
        return float(f"{average:.2f}")

    def __repr__(self):
        average = self.get_average_grade()
        return (f"The students in {self.name}: {', '.join(self.students)}."
                f" Average grade: {average}")
