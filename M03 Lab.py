class Vehicle:
    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


type = input("What type of vehicle is the model :")
year = input("What is the year of the vehicle? :")
make = input("What company manufactured the vehicle? :")
model = input("Enter the model :")
doors = input("How many doors? (2 or 4) :")
roof = input("Solid or sunroof :")
B = Automobile(type, year, make, model, doors, roof)

print("\nVehicle Type :"+B.type)
print("\nYear the car was made:"+B.year)
print("\nVehicle make :"+B.make)
print("\nModel :"+B.model)
print("\n# of Doors :"+B.doors)
print("\nSolid or Sunroof :"+B.roof)
