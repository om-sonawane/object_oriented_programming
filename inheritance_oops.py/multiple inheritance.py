class Employee:
    company= "Visa"

class freelancer :
    company="fiverr"
    level=0

    def Upgradelevel(self):
        self.level=self.level + 1

class programmer (Employee,freelancer):
    name="rohit"

p=programmer()
p.Upgradelevel()
print(p.company)
   