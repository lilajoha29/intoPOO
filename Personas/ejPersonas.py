class Personas:

    def __init__(self, name, last_name, year):
        self.name = name
        self.last_name = last_name
        self.year = year
        self.past = False

    def new_year_person(self, new_year):
        self.year = new_year
        print(f"{self.name} ha cambiado de edad a: {self.year} Feliz Cumpleaños.")

    def past_grade(self):
        self.past = True
        print(f"{self.name} ha ganado")

    def print_personas(self):
        print(self.name, self.last_name, self.year)


#objetos
        
person1 = Personas("pablo", "perez", 20)
print(person1.name, person1.last_name, person1.year)
person2 = Personas("ana", "lopez", 24)
# print(person2.name, person2.last_name, person2.year)
person2.print_personas()

person1.new_year_person(25)

person1.past_grade()

# herencia estudiantes
class estudiantes(Personas):

    def __init__(self, name, last_name, year, course, grade):
        super().__init__(name, last_name, year)
        self.course = course
        self.__grade = grade

    def course_student(self):
        print(f"{self.name} esta en la clase de {self.course}")

    def print_student(self):
        print(self.name, self.last_name, self.year, self.course, self.grade)

    def past_grade(self):
        self.past = False
        print(f"{self.name} tiene que recuperar la clase de {self.course}")
# encapsulamiento
    def get_grade(self):
        return self.__grade
    
    def set_grade(self, grade):
        self.__grade = grade


student1 = estudiantes("pablo", "perez", 20, "matematicas", 5)
student1.print_student()
student1.course_student()
student1.past_grade()

print(student1.get_grade())

student1.set_grade(8)
print(student1.get_grade())
