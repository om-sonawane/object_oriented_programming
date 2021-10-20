class Train:
    def __init__(self, name, fare, seats):
        self. name = name
        self. fare = fare
        self. seats = seats

    def getstatus(self):
        print("*******************")
        print(f"the name of the train{self.name}")
        print(f"the seats available in the train are {self.seats}")
        print("*******************")

    def fareInfo(self):
        print(f"the price of the ticket is :RS {self.fare}")

    def bookticket(self):
        if (self.seats > 0):
            print(
                f"Your ticket has been boocked ! your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry this train is FULL Kindly try in tatkal")

    def cancelTicket(self):
        pass


intercity = Train("Intercity Express :14015", 90, 300)
intercity.getstatus()
intercity.bookticket()

