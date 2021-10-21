class Employee:
    company = "Camel"
    salary=100
    location="delhi"

    def changesalary(self,sal):
        self.__class__.salary =sal
      
    def changesalary(self,sal):
        self.salary =sal

e= Employee
print(e.salary)  
e.changesalary(455)
print(e.salary)
print(Employee.salary)  