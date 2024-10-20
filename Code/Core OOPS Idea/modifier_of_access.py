class Employee:
    def __init__(self, name, employeeId, salary):
        self.name = name  # making Employee name public
        self._empID = employeeId  # making Employee ID protected
        self.__salary = salary  # making Employee salary private

    def getSalary(self):
        print(f"The salary of the Employee is {self.__salary}")


employee1 = Employee("Ryan", "21234", "$15000")
print(f"The Employee's name is {employee1.name}")
print(f"The Employee's Id is {employee1._empID}")
employee1.getSalary()
