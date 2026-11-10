from headerclass.automobileh import create_car


def main():
    while True:
        print("Enter the type:")
        vehicle_type = input("Type: ")
        print("Enter the maker of the car:")
        make = input("Make: ")
        print("Enter the year of the car:")
        year = int(input("Year: "))
        print("Enter the model of the car:")
        model = input("Model: ")
        print("Enter the number of doors:")
        doors = int(input("Number of doors: "))
        print("Enter the roof type:")
        roof = input("Roof type: ")

        car = create_car(year, make, model, doors, roof)

        print("\nCar Details:")
        print(f"Type: {car.vehicle_type}")
        print(f"Year: {car.year}")
        print(f"Make: {car.make}")
        print(f"Model: {car.model}")
        print(f"Doors: {car.doors}")
        print(f"Roof: {car.roof}")

        cont = input("\nDo you want to enter another car? (yes/no): ").strip().lower()
        if cont != "yes":
            break


if __name__ == "__main__":
    main()
