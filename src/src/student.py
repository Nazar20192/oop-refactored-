from person import Person

class Student(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.group = None
        self.grades = []
        self.scholarship = 0

    def add_grade(self, subject, grade):
        self.grades.append({"subject": subject, "grade": grade})

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(g["grade"] for g in self.grades) / len(self.grades)

    def set_scholarship(self, amount):
        self.scholarship = amount
