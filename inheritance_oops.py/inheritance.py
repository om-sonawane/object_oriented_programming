class Employee:
    company = "google"

    def showDetails(self):
        print("this ia an employee")


class programmer (Employee):
    language = "python"

    def getlanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this ia an programmer")


e = Employee()
e.showDetails()
p = programmer()
print(p.company)
