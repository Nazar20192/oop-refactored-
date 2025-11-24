class Person:
    def __init__(self, name, age, person_id, email, phone):
        self.name = name
        self.age = age
        self.person_id = person_id
        self.email = email
        self.phone = phone

    def get_contact_info(self):
        return f"Email: {self.email}, Phone: {self.phone}"

    def get_full_info(self):
        role = self.__class__.__name__
        return f"{role} {self.name}, ID: {self.person_id}, Age: {self.age}"

    def update_email(self, new_email):
        self.email = new_email
        print(f"Email оновлено для {self.name}")

    def update_phone(self, new_phone):
        self.phone = new_phone
        print(f"Телефон оновлено для {self.name}")
