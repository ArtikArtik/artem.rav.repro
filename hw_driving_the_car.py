import random


class Car:
    def __init__(self, model, color, economy):
        self.mileage = 0
        self.fuel = 100
        self.model = model
        self.color = color
        self.economy = economy

    def drive(self, distance):
        fuel_needed = distance * self.economy / 100
        if fuel_needed > self.fuel:
            print("Помилка: Недостатньо палива!")
        else:
            self.fuel -= fuel_needed
            self.mileage += distance

    def distance_left(self):
        return self.fuel

    def fuel_up(self):
        self.fuel += 20


models = ["Toyota", "Honda", "Ford", "Chevrolet", "Nissan"]
colors = ["Red", "Blue", "Green", "Yellow", "Black", "White"]
cars = []

# Створення 10 машин із випадковими значеннями
for _ in range(10):
    model = random.choice(models)
    color = random.choice(colors)
    economy = random.randint(5, 15)
    car = Car(model, color, economy)
    cars.append(car)

# Кожна машина їде 200 км, заправляється, їде ще 100 км
for car in cars:
    car.drive(200)
    car.fuel_up()
    car.drive(100)

# Знаходження машини з найбільшим запасом палива
max_fuel_car = max(cars, key=lambda car: car.fuel)

# Виведення опису машини з найбільшим запасом палива
print(f"Машина з найбільшим запасом палива: {max_fuel_car.model}, {max_fuel_car.color}")
print(
    f"Залишок палива: {max_fuel_car.distance_left()} л, Дистанція, яку може проїхати: {max_fuel_car.distance_left() * max_fuel_car.economy} км")
