## Car Dealership Lab

class Vehicle:
    def __init__(self, make, miles, price):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False

    def start_engine(self):
        print('Starting engine...')
        self.engine_on = True

    def make_noise(self):
        print('Beep beep!')


class Truck(Vehicle):
    def __init__(self, make, miles, price):
        Vehicle.__init__(self, make, miles, price)
        self.cargo = False

    def load_cargo(self):
        print("Loading the truck bed...")
        self.cargo = True


class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        Vehicle.__init__(self, make, miles, price)
        self.top_speed = top_speed

    def make_noise(self):
        print('Vroom vroom!')
# setting bikes for list
bike1 = Motorcycle("Yamaha", 2000, 10000, 120)
bike2 = Motorcycle("Toyota", 1000, 5000, 80)
bike3 = Motorcycle("Kawasaki", 6000, 9000, 160)

# setting trucks for list
truck1 = Truck("Toyota", 50000, 60000)
truck2 = Truck("Ford", 80000, 90000)
truck3 = Truck("Tesla", 100, 100000)

# lists
bikes = [bike1, bike2, bike3]
trucks = [truck1, truck2, truck3]
vehicles_to_compare = []

#compare function

def compare(choice):
    print('Would you like to compare now? (y/n) ')
    compare_vehicle = input('< ').lower()
    if compare_vehicle == 'y' and choice == 'b':
        print('Which vehicle would you like to compare? ')
        vehicle_index = int(input('< '))
        vehicles_to_compare.append(bikes[vehicle_index-1])
        print(f'{vehicles_to_compare[-1].make} added!')
    elif compare_vehicle == 'y' and choice == 't':
        print('Which vehicle would you like to compare? ')
        vehicle_index = int(input('< '))
        vehicles_to_compare.append(trucks[vehicle_index - 1])
        print(f'{vehicles_to_compare[-1].make} added!')
    elif compare_vehicle != 'y' and compare_vehicle != 'n':
        print('Please enter y or n')
        compare(choice)
    return vehicles_to_compare
## input start

print('Welcome to GC Bikes & Trucks!')
switch = True
while switch == True:

    choice = input('Would you like to view bikes or trucks? (b/t) ').lower()
    if choice == 'b':
        for index, bike in enumerate(bikes):
            print(f'{index+1}: {bikes[index].make} with {bikes[index].miles} miles and a top speed of '
                    f'{bikes[index].top_speed} costs ${bikes[index].price}')
        compare(choice)
    elif choice == 't':
        for index, truck in enumerate(trucks):
            print(f'{index+1}: {trucks[index].make} with {trucks[index].miles} miles costs'
                      f' ${trucks[index].price}')
        compare(choice)
        print('Would you like to compare your vehicles now?')
        compare_select = input('< ').lower()
        if compare_select == 'y':
            for vehicle in vehicles_to_compare:
                print(f'{vehicle.make}: with {vehicle.miles} miles costs'
                      f' ${vehicle.price}')
                vehicle.make_noise()
            print("Thank you and have a nice day! <END PROGRAM>")
            break
    else:
        print('Please enter b or t')

