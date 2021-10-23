#salaryafterincrement = salary * increment
class employee:
    salary = 1000
    increment = 1.5

    @property
    def salaryafterincrement(self):
        return self.salary*self.increment

    @salaryafterincrement.setter
    def salaryafterincrement(self, sai):
        self.increment = sai / self.salary


e = employee()
print(e.salaryafterincrement)
