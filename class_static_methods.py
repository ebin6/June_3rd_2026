'''class Student:

    def __init__(self):
        self.age=20
    


    @staticmethod
    def greet():
        print("Hello")


std=Student()
Student.greet()
'''

class Employee:
    company = "ABC Ltd"

    def __init__(self, name):
        self.name = name

    def instance_method(self):
        return f"{self.name} works at {Employee.company}"

    @classmethod
    def class_method(cls):
        return cls.company

    @staticmethod
    def is_valid_age(age):
        return age >= 18
    
emp = Employee("Alice")
print(emp.instance_method())      # Uses self
print(Employee.class_method())    # Uses cls
print(Employee.is_valid_age(25))  # Uses neither self nor cls