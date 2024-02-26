class Employee:
    EmployeeList=[]
    def __init__(self, name: str) -> None:
        self.name = name
        self.salary = 0
        Employee.EmployeeList.append(self)

    def update_salary(self, hours: int) -> None:
        self.salary += (hours * 200)

    def __add__(self, other):
        if isinstance(other, Employee):
            new_employee = Employee("Combined Employee")
            new_employee.salary = self.salary + other.salary
            return new_employee
        elif isinstance(other, int):
            new_employee = Employee("Combined Employee")
            new_employee.salary = self.salary + other
            return new_employee
        else:
            raise TypeError("Unsupported operand type for +: {}".format(type(other)))

class PartTimeEmployee(Employee):  
    def update_salary(self, hours: int) -> None:
        self.salary += (hours * 150)

def emp_input():
    name = input("Enter the name of Employee: ")
    hours = int(input("Enter hours of work: "))
    return name, hours

print("Employee 1:")
name, hours = emp_input()
Emp1 = Employee(name)
Emp1.update_salary(hours)

print("Employee 2:")
name, hours = emp_input()
Emp2 = Employee(name)
Emp2.update_salary(hours)

print("Employee 3:")
name, hours = emp_input()
Emp3 = PartTimeEmployee(name)
Emp3.update_salary(hours)

print("Total No of Employees : ",len(Employee.EmployeeList))

total_salary = 0
for i in Employee.EmployeeList:
    total_salary+=i.salary

print("Total Expense : ",total_salary)

avg = total_salary/len(Employee.EmployeeList)
print("Average Expense per Employee : ",avg)

