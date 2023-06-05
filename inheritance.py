class Vehicle:
    def __init__(self, make, model, weight, year):
        self.make = make
        self.model = model
        self.weight = weight
        self.year = year
    def start_engine(self):
        print("working")
class Car(Vehicle):
    def __init__(self, make, model, weight, year, num_doors, num_passengers):
        super().__init__(make, model, weight, year)
        self.num_doors = num_doors
        self.num_passengers = num_passengers
    def start_engine(self):
        return "The car's engine is starting..."
    def drive(self):
        return 'is going'
V = Vehicle('audi', 'RS7', 1995, 2013)
print(V.start_engine())
C = Car('audi', 'RS7', 1995, 2013, 4, 4)
print(C.start_engine())
print(C.drive())
class Truck(Vehicle):
    def __init__(self, make, model, weight, year, cargo_capacity, towing_capacity):
        super().__init__(make, model, weight, year)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity
    def start_engine(self):
        return "The truck's engine is starting..."
    def haul(self):
        print(f"{self.make}, {self.model}, {self.weight}, {self.year}", \
               f"{self.cargo_capacity}, {self.towing_capacity}")
truck=Truck('Toyota', 'rav4', '1829', 2014, '23', '50')
truck.haul()
print(truck.start_engine())
class Motorcycle(Vehicle):
    def __init__(self, make, model, weight, year, num_wheels, has_sidecar):
        super().__init__(make, model, weight, year)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar
    def start_engine(self):
        return "The motorcycle's engine is starting..."
    def ride(self):
        print( f" {self.make}, {self.model}, {self.weight}, {self.year}", \
               f"{self.num_wheels}, {self.has_sidecar}")
motorcycle=Motorcycle('BMW', 'S1000RR', '183', 2009, '2', '-')
print(motorcycle.start_engine())
motorcycle.ride()
print(C.start_engine())
print(truck.start_engine())
print(motorcycle.start_engine())
print(V.start_engine())