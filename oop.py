class Vehicle:
    def __init__(self, vin, make, model, mileage):
        self.vin = vin
        self.make = make
        self.model = model
        self.mileage = mileage

    def get_maintenance_cost(self):
        return 50.0

    def display_info(self):
        return f"VIN:{self.vin} , {self.make} , {self.model},{self.mileage}"



class Car(Vehicle):
    def __init__(self, vin, make, model, mileage, passenger_capacity):
        super().__init__(vin, make, model, mileage)
        self.passenger_capacity = passenger_capacity

    
    def get_maintenance_cost(self):
        return 50 + (5 * self.passenger_capacity)


class Truck(Vehicle):
    def __init__(self, vin, make, model, mileage, payload_capacity):

        super().__init__(vin, make, model, mileage)
        self.payload_capacity = payload_capacity

    
    def get_maintenance_cost(self):
        return 100 +(self.mileage *0.01)


class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, mileage, has_sidecar):
        super().__init__(vin, make, model, mileage)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        if self.has_sidecar:
            print("Sidecar Edition")
        else:
            print("No Sidecar")


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def total_maintenance_report(self):
        total = 0

        for vehicle in self.vehicles:
            cost = vehicle.get_maintenance_cost()
            print(vehicle.make, vehicle.model, "Cost:", cost)
            total = total + cost

        print("Grand Total:", total)


car1 = Car("101", "Hyundai", "Elantra", 5200, 5)
truck1 = Truck("102", "Toyota", "Hilux",2487, 1000)
motorcycle1 = Motorcycle("103", "Honda", "CBR", 4500 ,True)

fleet1 = Fleet()

fleet1.add_vehicle(car1)
fleet1.add_vehicle(truck1)
fleet1.add_vehicle(motorcycle1)

motorcycle1.display_info()

fleet1.total_maintenance_report()