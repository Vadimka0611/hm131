from os import remove


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}. Age: {self.age}. Gender: {self.gender}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book
    def __str__(self):
        return f"{super().__str__()}, Record book: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        student_delete = self.find_student(last_name)
        if student_delete:
            self.group.remove(student_delete)
        else:
            print(f"Student '{last_name}' not found")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        else:
            return None

    def __str__(self):
        if self.group:
            all_students = '\n'.join([str(student) for student in self.group])
        else:
            all_students = "Students not in group"

        return f'Number:{self.number} {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
str(gr.find_student('Jobs'))
gr.find_student('Jobs2')
isinstance(gr.find_student('Jobs'), Student)

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
