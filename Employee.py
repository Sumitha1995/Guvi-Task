#create Base Class Employee

class Employee :

    # constructor to initialize common attributes

    def __init__(self,name,salary):

        self.name=name
        self.salary=salary
    
    # Common method

    def calculate_salary(self) :

        print(self.salary)

# Child class Regular Employee inherited from Parent Class Employee

class RegularEmployee (Employee):

    def calculate_salary(self):
        print("Salary for Regular Employee is",self.salary)

# Child class Contract Employee inherited from Parent Class Employee

class ContractEmployee (Employee):

    def calculate_salary(self):
        print("Salary for Contract Employee is",self.salary)

# Child class Manager inherited from Parent Class Employee

class Manager (Employee):

    def calculate_salary(self):
        print("Salary for Manager is",self.salary)

# creating objects for child classess

e1=RegularEmployee("Anil",35000)
e2=ContractEmployee("Karthik",20000)
e3=Manager("Vignesh",70000)

# calling methods using objects

e1.calculate_salary()
e2.calculate_salary()
e3.calculate_salary()