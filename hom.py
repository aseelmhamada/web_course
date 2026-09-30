class Vehicle:
    def __init__(self, vin, make, model, mileage):
        self.vin = vin
        self.make = make
        self.model = model
        self.mileage = mileage

    def get_maintenance_cost(self):
        return 50.0

    def display_info(self):
        return f"{self.make} {self.model} (VIN: {self.vin})"



class Car(Vehicle):
    def __init__(self, vin, make, model, mileage, passenger_capacity):
        super().__init__(vin, make, model, mileage)
        self.passenger_capacity = passenger_capacity

    
    def get_maintenance_cost(self):
        return 50.0 + (5 * self.passenger_capacity)


class Truck(Vehicle):
    def __init__(self, vin, make, model, mileage, payload_capacity):
        super().__init__(vin, make, model, mileage)
        self.payload_capacity = payload_capacity

    
    def get_maintenance_cost(self):
        return 100.0 + (self.mileage * 0.01)


class Motorcycle(Vehicle):
    def __init__(self, vin, make, model, mileage, has_sidecar):
        super().__init__(vin, make, model, mileage)
        self.has_sidecar = has_sidecar

    def display_info(self):
        info = super().display_info()
        if self.has_sidecar:
            info += " - Sidecar Edition"
        return info


class Fleet:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def total_maintenance_report(self):
        total = 0.0
        print(" Fleet Maintenance Report ")
        
        for v in self.vehicles:
            cost = v.get_maintenance_cost()
            total += cost
            print(f"{v.display_info()} -> Cost: {cost:.2f}")

        
        print(f"Total Fleet Cost: {total:.2f}")                
        
        
        
c1 = Car("C1", "Toyota", "Camry", 15000, 4)
t1 = Truck("T1", "Fiat", "F150", 50000, 10)
m1 = Motorcycle("M1", "BMW", "R1250", 8000, True)



fleet = Fleet()
fleet.add_vehicle(c1)
fleet.add_vehicle(t1)
fleet.add_vehicle(m1)

fleet.total_maintenance_report()