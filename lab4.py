class FlightData:
    def __init__(self):
        self.data = {
            "AI161E90": ("BLR", "BOM", 5600),
            "BR161F91": ("BOM", "BBI", 6750),
            "AI161F99": ("BBI", "BLR", 8210),
            "VS171E20": ("JLR", "BBI", 5500),
            "AS171G30": ("HYD", "JLR", 4400),
            "AI131F49": ("HYD", "BOM", 3499)
        }

    def search_by_city(self, city):
        result = []
        for flight_id, (from_city, to_city, price) in self.data.items():
            if city in (from_city, to_city):
                result.append((flight_id, from_city, to_city, price))
        return result

    def search_by_from_city(self, from_city):
        result = []
        for flight_id, (from_city_, to_city, price) in self.data.items():
            if from_city == from_city_:
                result.append((flight_id, from_city_, to_city, price))
        return result

    def search_by_cities(self, from_city, to_city):
        result = []
        for flight_id, (from_city_, to_city_, price) in self.data.items():
            if from_city == from_city_ and to_city == to_city_:
                result.append((flight_id, from_city_, to_city_, price))
        return result

    def display_flights(self, flights):
        if not flights:
            print("No flights found.")
            return

        print("{:<10} {:<10} {:<10} {:<10}".format("Flight ID", "From", "To", "Price"))
        print("=" * 40)
        for flight in flights:
            print("{:<10} {:<10} {:<10} {:<10}".format(*flight))

if __name__ == "__main__":
    flight_data = FlightData()

    while True:
        print("\nSearch Options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            flights = flight_data.search_by_city(city)
            flight_data.display_flights(flights)
        elif choice == "2":
            from_city = input("Enter source city name: ")
            flights = flight_data.search_by_from_city(from_city)
            flight_data.display_flights(flights)
        elif choice == "3":
            from_city = input("Enter source city name: ")
            to_city = input("Enter destination city name: ")
            flights = flight_data.search_by_cities(from_city, to_city)
            flight_data.display_flights(flights)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")
