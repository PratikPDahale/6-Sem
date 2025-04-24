class AirlineSchedule:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, departure, destination):
        return [flight for flight in self.flights if flight['departure'] == departure and flight['destination'] == destination]

class CargoSchedule:
    def __init__(self):
        self.cargos = []

    def add_cargo(self, cargo):
        self.cargos.append(cargo)

    def search_cargos(self, origin, destination):
        return [cargo for cargo in self.cargos if cargo['origin'] == origin and cargo['destination'] == destination]

def main():
    airline_schedule = AirlineSchedule()
    cargo_schedule = CargoSchedule()

    # Adding example flights
    airline_schedule.add_flight({'flight_number': "F001", 'departure': "New York", 'destination': "London",
                                 'departure_time': "08:00", 'arrival_time': "14:00"})
    airline_schedule.add_flight({'flight_number': "F002", 'departure': "London", 'destination': "Paris",
                                 'departure_time': "15:30", 'arrival_time': "17:00"})
    airline_schedule.add_flight({'flight_number': "F003", 'departure': "Paris", 'destination': "Rome",
                                 'departure_time': "18:30", 'arrival_time': "20:00"})

    # Adding example cargos
    cargo_schedule.add_cargo({'cargo_id': "C001", 'flight_number': "F001", 'weight': 500,
                              'origin': "New York", 'destination': "London"})
    cargo_schedule.add_cargo({'cargo_id': "C002", 'flight_number': "F002", 'weight': 300,
                              'origin': "London", 'destination': "Paris"})
    cargo_schedule.add_cargo({'cargo_id': "C003", 'flight_number': "F003", 'weight': 700,
                              'origin': "Paris", 'destination': "Rome"})

    while True:
        print("1. Add Flight")
        print("2. Add Cargo")
        print("3. Search Flights")
        print("4. Search Cargos")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            flight = {
                'flight_number': input("Enter flight number: "),
                'departure': input("Enter departure: "),
                'destination': input("Enter destination: "),
                'departure_time': input("Enter departure time: "),
                'arrival_time': input("Enter arrival time: ")
            }
            airline_schedule.add_flight(flight)
            print("Flight added successfully.")

        elif choice == '2':
            cargo = {
                'cargo_id': input("Enter cargo ID: "),
                'flight_number': input("Enter flight number: "),
                'weight': float(input("Enter cargo weight: ")),
                'origin': input("Enter origin: "),
                'destination': input("Enter destination: ")
            }
            cargo_schedule.add_cargo(cargo)
            print("Cargo added successfully.")

        elif choice == '3':
            departure = input("Enter departure: ")
            destination = input("Enter destination: ")
            flights = airline_schedule.search_flights(departure, destination)
            if flights:
                print("Flights found:")
                for flight in flights:
                    print(f"Flight Number: {flight['flight_number']}")
                    print(f"Departure: {flight['departure']}")
                    print(f"Destination: {flight['destination']}")
                    print(f"Departure Time: {flight['departure_time']}")
                    print(f"Arrival Time: {flight['arrival_time']}")
            else:
                print("No flights found for the given departure and destination.")
1
        elif choice == '4':
            origin = input("Enter origin: ")
            destination = input("Enter destination: ")
            cargos = cargo_schedule.search_cargos(origin, destination)
            if cargos:
                print("Cargos found:")
                for cargo in cargos:
                    print(f"Cargo ID: {cargo['cargo_id']}")
                    print(f"Flight Number: {cargo['flight_number']}")
                    print(f"Weight: {cargo['weight']}")
                    print(f"Origin: {cargo['origin']}")
                    print(f"Destination: {cargo['destination']}")
            else:
                print("No cargos found for the given origin and destination.")

        elif choice == '5':
            break

        print()  # Empty line for better readability

if __name__ == '__main__':
    main()
'''
Output :
1. Add Flight
2. Add Cargo
3. Search Flights
4. Search Cargos
5. Exit
Enter your choice: 1
Enter flight number: F004
Enter departure: Mumbai
Enter destination: Chennai
Enter departure time: 16:00
Enter arrival time: 21:00
Flight added successfully.

1. Add Flight
2. Add Cargo
3. Search Flights
4. Search Cargos
5. Exit
Enter your choice: 3
Enter departure: New York
Enter destination: London
Flights found:
Flight Number: F001
Departure: New York
Destination: London
Departure Time: 08:00
Arrival Time: 14:00

1. Add Flight
2. Add Cargo
3. Search Flights
4. Search Cargos
5. Exit
Enter your choice: 2
Enter cargo ID: C004
Enter flight number: F004
Enter cargo weight: 350
Enter origin: Mumbai
Enter destination: Chennai
Cargo added successfully.

1. Add Flight
2. Add Cargo
3. Search Flights
4. Search Cargos
5. Exit
Enter your choice: 4
Enter origin: Paris
Enter destination: Rome
Cargos found:
Cargo ID: C003
Flight Number: F003
Weight: 700
Origin: Paris
Destination: Rome

1. Add Flight
2. Add Cargo
3. Search Flights
4. Search Cargos
5. Exit
Enter your choice: 5

'''
