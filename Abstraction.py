from abc import ABC, abstractmethod

# Abstract class
class Employee(ABC):
    def __init__(self, name, salary):
        self.__name = name        # private attribute
        self.__salary = salary    # private attribute

    def display_info(self):
        print(f"Employee Name: {self.__name}")

    def get_salary(self):
        return self.__salary

    @abstractmethod
    def calculate_salary(self):
        pass


# Full-time employee subclass
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary()


# Part-time employee subclass
class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return self.get_salary() / 2


# Main program
emp1 = FullTimeEmployee("Alice", 5000)
emp2 = PartTimeEmployee("Bob", 5000)

employees = [emp1, emp2]

for emp in employees:
    emp.display_info()
    print("Calculated Salary:", emp.calculate_salary())
    print("-" * 30)
