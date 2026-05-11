# Parent Class Vehicle
class Vehicle :                            

    # constructor to initialize common attributes

    def __init__(self,model,rental_rate): 
        self.model=model
        self.rental_rate=rental_rate

    # Common method

    def calculate_rental(self,days):
        print(self.rental_rate*days)

# Child class Car inherited from Parent Class Vehicle
    
class Car(Vehicle):

    # overriding calculate_rental() method    

    def calculate_rental(self,days):
        print("Rental Amount for Car is",self.rental_rate*days)
    

# Child class Bike inherited from Parent Class Vehicle

class Bike(Vehicle):
    
    # overriding calculate_rental() method

    def calculate_rental(self,days):
        print("Rental Amount for Bike is",self.rental_rate*days)

# Child class Truck inherited from Parent Class Vehicle
    
class Truck(Vehicle):
    
     # overriding calculate_rental() method

    def calculate_rental(self,days):
        print("Rental Amount for Truck is",self.rental_rate*days)

# creating objects for child classes

c1=Car("Skoda",5000)
b1=Bike("Duke",500)
t1=Truck("Tata",9000)

# calling methods using objects

c1.calculate_rental(3)
b1.calculate_rental(5)
t1.calculate_rental(2)