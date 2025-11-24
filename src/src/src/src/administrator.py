from person import Person

class Administrator(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.position = None
        self.department = None
        self.salary = 0
        self.access_level = 1

    def set_position(self, position):
        self.position = position

    def set_access_level(self, level):
        if 1 <= level <= 5:
            self.access_level = level

    def grant_access(self, resource):
        if self.access_level >= 3:
            return f"{self.name} має доступ до {resource}"
        return f"{self.name} не має достатнього рівня доступу"
