# main.py
from car import Car
from user import User
from rental import Rental



def main():
    rental = Rental()

    while True:
        print("\n1. Add Car")
        print("2. Add User")
        print("3. Rent Car")
        print("4. Return Car")
        print("5. Enquire Car")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            model = input("Enter car model: ")
            price = float(input("Enter car price: "))
            car = Car(model, price)
            rental.add_car(car)
        elif choice == 2:
            name = input("Enter user name: ")
            user = User(name)
            rental.add_user(user)
        elif choice == 3:
            user_name = input("Enter user name: ")
            car_model = input("Enter car model: ")
            for user in rental.users:
                if user.name == user_name:
                    rental.rent_car(user, car_model)
                    break
            else:
                print("User not found")
        elif choice == 4:
            user_name = input("Enter user name: ")
            for user in rental.users:
                if user.name == user_name:
                    rental.return_car(user)
                    break
            else:
                print("User not found")
        elif choice == 5:
            car_model = input("Enter car model: ")
            rental.enquire_car(car_model)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()