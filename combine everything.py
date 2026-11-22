# VICE HEARTS 
money = 5000
garage = []

# 1. CLASS
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# 2. OBJECTS 
porsche = Car("Porsche", 2000)
bmw = Car("BMW", 4000)

# 3. GAME LOOP 
while True:
    print("\n--- VICE HEARTS ---")
    print("Money =", money)
    print("1. Buy Porsche (2000)")
    print("2. Buy BMW (4000)")
    print("3. Show Garage")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        if money >= porsche.price:
            money -= porsche.price
            garage.append(porsche.name)
            print("You bought", porsche.name)
        else:
            print("Not enough money!")
    elif choice == 2:
        if money >= bmw.price:
            money -= bmw.price
            garage.append(bmw.name)
            print("You bought", bmw.name)
        else:
            print("Not enough money!")
    elif choice == 3:
        if len(garage) == 0:
            print("Garage is Empty!")
        else:
            print("Your Garage:")
            for car in garage:
                print("-", car)
    elif choice == 4:
        print("Game Exited. Final Money =", money)
        break
    else:
        print("Invalid choice!")