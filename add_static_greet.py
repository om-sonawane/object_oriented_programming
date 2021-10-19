class calculator:
   
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"the value of {self.number} square  is {self.number **2}")

    def squareRoot(self):
         print(f"the value of {self.number} square root  is {self.number **0.5}")
    
    def cube (self):
         print(f"the value of {self.number} cube is {self.number **3}")
    @staticmethod
    def greet():
        print("hello there welcome to the best calculator of the world")     

a= calculator(9)
a.greet()
a.square()
a.squareRoot()
a.cube()  



