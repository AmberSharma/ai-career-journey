class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


class Wheel:
    def __init__(self, size):
        self.size = size


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine(200)  # Car HAS an engine
        self.wheels = [Wheel(17) for _ in range(4)]  # Car HAS wheels

    def start(self):
        return f"{self.brand}: {self.engine.start()}"


car = Car("Toyota")
print(car.start())  # Toyota: Engine started
print(car.engine.horsepower)  # 200
print(car.wheels)