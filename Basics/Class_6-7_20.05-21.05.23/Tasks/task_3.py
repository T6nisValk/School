# Create a class called "Person" with attributes for name and age.
# Add a method to the Person class that prints a greeting message with the person's name.
# Create a subclass of Person called "Student" with an additional attribute for student ID.
# Override the Person class's method in the Student subclass to include the student ID in the greeting message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_greeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def print_greeting(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. My student ID is {self.student_id}.")


person = Person("Tõnis", 31)
person.print_greeting()
student = Student("Tõnis", 31, 123456)
student.print_greeting()
