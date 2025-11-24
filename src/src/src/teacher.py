from person import Person

class Teacher(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.department = None
        self.subjects = []
        self.salary = 0
        self.experience_years = 0

    def add_subject(self, subject):
        self.subjects.append(subject)

    def set_salary(self, amount):
        self.salary = amount

    def get_salary_info(self):
        bonus = self.experience_years * 1000
        return f"Salary: {self.salary}, Bonus: {bonus}, Total: {self.salary + bonus}"
