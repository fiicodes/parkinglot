class ParkingLot:
    def __init__(self):
        # Initialize two levels, each with 20 parking spots
        self.level_A = [None] * 20
        self.level_B = [None] * 20

    def assign_parking_spot(self, vehicle_number):
        # Check if vehicle is already added
        if vehicle_number in self.level_A or vehicle_number in self.level_B:
            return " Your Vehicle is already parked."
        # Finding  an available parking spot and assign it to the vehicle
        for i, spot in enumerate(self.level_A):
            if spot is None:
                self.level_A[i] = vehicle_number
                return {"level": "A", "spot": i + 1}

        for i, spot in enumerate(self.level_B):
            if spot is None:
                self.level_B[i] = vehicle_number
                return {"level": "B", "spot": i + 21}

        return "Parking is full."

    def retrieve_parking_spot(self, vehicle_number):
        # Retrieving the parking spot of a specific vehicle
        for i, spot in enumerate(self.level_A):
            if spot == vehicle_number:
                return {"level": "A", "spot": i + 1}

        for i, spot in enumerate(self.level_B):
            if spot == vehicle_number:
                return {"level": "B", "spot": i + 21}

        return "Vehicle not found."


# Creating a ParkingLot instance
parking_lot = ParkingLot()

while True:
    print("\nOptions:")
    print("1. Assign a parking spot to a new vehicle")
    print("2. Retrieve parking spot for a vehicle")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        vehicle_number = input("Enter vehicle number: ")
        result = parking_lot.assign_parking_spot(vehicle_number)
        print("Assigned parking spot:", result)

    elif choice == "2":
        vehicle_number = input("Enter vehicle number: ")
        result = parking_lot.retrieve_parking_spot(vehicle_number)
        print("Retrieved parking spot:", result)

    elif choice == "3":
        break

    else:
        print("Invalid choice !!!. Please choose a valid option.")
