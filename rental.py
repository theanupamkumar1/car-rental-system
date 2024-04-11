# rental.py
from car import Car
from user import User

class Rental:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_car(self, car):
        self.cars.append(car)

    def add_user(self, user):
        self.users.append(user)

    def rent_car(self, user, car_model):
        for car in self.cars:
            if car.model == car_model and car.availability_status:
                user.rented_car = car
                car.availability_status = False
                print(f"{user.name} has rented {car.model}")
                return
        print("Car not available")

    def return_car(self, user):
        if user.rented_car:
            user.rented_car.availability_status = True
            print(f"{user.name} has returned {user.rented_car.model}")
            user.rented_car = None
        else:
            print(f"{user.name} has no rented car")

    def enquire_car(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                if car.availability_status:
                    print(f"{car.model} is available for rent")
                else:
                    print(f"{car.model} is not available for rent")
                return
        print("Car not found")