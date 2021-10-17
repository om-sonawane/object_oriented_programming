class  programmer:
    company ="Microsoft"

    def __init__(self,name,product):
        self.name= name
        self.product= product 

    def getInfo(self):
        print( f"the name of programmer is {self.name} and the product is {self.product}")


om =programmer ("om","skype")
anna=programmer("anna","Github")
om.getInfo()