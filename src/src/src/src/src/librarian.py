from person import Person

class Librarian(Person):
    def __init__(self, name, age, person_id, email, phone):
        super().__init__(name, age, person_id, email, phone)
        self.shift = None
        self.books_issued = []
        self.salary = 0

    def issue_book(self, book_title, person_name):
        self.books_issued.append({"book": book_title, "person": person_name})
        return f"Книга '{book_title}' видана для {person_name}"

    def get_issued_books_count(self):
        return len(self.books_issued)
