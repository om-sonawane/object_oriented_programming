class person:
    country = "india"

    def __init__(self):
        print("Initializing person...\n")

    def takebreath(self):
        print("i am breathing..")


class Employee (person):
    company = "honda"
    
    def __init__(self):
        #super().__init__()
        print("Initializing person...\n")
    
    def Getsalary(self):
        print(f"salary is {self.salary}")

    def takebreath(self):
        print("i am an Employee so iam luckily breathing..")


class programmer(Employee):
    company = "fiverr"

    def __init__(self):
        #super().__init__()
        print("Initializing programmer...\n")

    def getSalary(self):
        print(f"No salary to programmer")

    def takebreath(self):
        super().takebreath()
        print("i am an programmer so iam breathing++..")

p = programmer()
p.takebreath()

e= Employee()
e.takebreath()

pr= programmer()
pr.takebreath()





