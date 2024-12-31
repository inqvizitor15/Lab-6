class Vehicle:
    def __init__(self, vehicle_tank_capacity, fuel_consumption, average_speed):
        self.vehicle_tank_capacity = vehicle_tank_capacity
        self.fuel_consumption = fuel_consumption
        self.average_speed = average_speed

    def distance(self):
        if self.average_speed <= 0:
            return 'Средняя скорость автомобиля должна быть больше 0'
        dist = self.vehicle_tank_capacity / self.fuel_consumption
        return f'Расстояние, пройденное автомобилем до полного опустошения бака: {dist:.2f}'

    def __add__(self, other):
        if isinstance(other, Vehicle):
            return Vehicle(
                self.vehicle_tank_capacity + other.vehicle_tank_capacity,
                (self.fuel_consumption + other.fuel_consumption) / 2,
                (self.average_speed + other.average_speed) / 2
            )
        return NotImplemented


class Truck(Vehicle):
    def __init__(self, vehicle_tank_capacity, fuel_consumption, average_speed, max_cargo_weight):
        super().__init__(vehicle_tank_capacity, fuel_consumption, average_speed)
        self.max_cargo_weight = max_cargo_weight

    def cargo_to_fuel_ratio(self, distance=250):
        fuel_needed = (self.fuel_consumption / 100) * distance
        return f'Соотношение веса груза к топливу (250 км): {(self.max_cargo_weight / fuel_needed):.2f}'


class Bus(Vehicle):
    def __init__(self, vehicle_tank_capacity, fuel_consumption, average_speed, passenger_capacity):
        super().__init__(vehicle_tank_capacity, fuel_consumption, average_speed)
        self.passenger_capacity = passenger_capacity

    def passenger_to_fuel_ratio(self, distance=250):
        fuel_needed = (self.fuel_consumption / 100) * distance
        return f'Соотношение пассажиров к топливу (250 км): {(self.passenger_capacity / fuel_needed):.2f}'



if __name__ == "__main__":
    car = Vehicle(50, 8, 120)
    print('-----Vehicle-----')
    print(car.distance())
    print()

    truck = Truck(100, 15, 80, 500)
    print('-----Truck-----')
    print(truck.cargo_to_fuel_ratio())
    print()

    bus = Bus(70, 12, 100, 50)
    print('-----Bus-----')
    print(f'Соотношение пассажиров к топливу (250 км): {bus.passenger_to_fuel_ratio()} чел/л')
    print()

    print('-----Combined vehicle-----')
    combined_vehicle = truck + bus
    print(combined_vehicle.distance())