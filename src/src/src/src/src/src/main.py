from student import Student
from teacher import Teacher
from administrator import Administrator
from librarian import Librarian

student = Student("Оксана Петренко", 19, "S001", "oksana@college.com", "+380501234567")
student.set_scholarship(2000)
student.add_grade("Математика", 95)
student.add_grade("Програмування", 90)

teacher = Teacher("Ігор Коваленко", 45, "T001", "igor@college.com", "+380502345678")
teacher.add_subject("Програмування")
teacher.add_subject("Бази даних")
teacher.set_salary(25000)
teacher.experience_years = 15

admin = Administrator("Марина Сидоренко", 38, "A001", "marina@college.com", "+380503456789")
admin.set_position("Завідувач навчальної частини")
admin.set_access_level(4)

librarian = Librarian("Петро Мельник", 52, "L001", "petro@college.com", "+380504567890")
librarian.shift = "денна"
librarian.issue_book("Python для початківців", "Оксана Петренко")

print(student.get_full_info())
print(student.get_contact_info())
print(f"Середній бал: {student.get_average_grade()}")

print("\n" + teacher.get_full_info())
print(teacher.get_contact_info())
print(teacher.get_salary_info())

print("\n" + admin.get_full_info())
print(admin.grant_access("База даних студентів"))

print("\n" + librarian.get_full_info())
print(f"Видано книг: {librarian.get_issued_books_count()}")
