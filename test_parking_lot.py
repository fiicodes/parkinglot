import unittest
from parkinglot import ParkingLot


class TestParkingLot(unittest.TestCase):

    def test_assign_and_retrieve_parking_spot(self):
        # Create a ParkingLot instance
        parking_lot = ParkingLot()

        # Assign a parking spot to a vehicle
        vehicle_number = "ABC123"
        result = parking_lot.assign_parking_spot(vehicle_number)
        self.assertEqual(result, {"level": "A", "spot": 1})

        # Retrieve the parking spot for the same vehicle
        retrieved_result = parking_lot.retrieve_parking_spot(vehicle_number)
        self.assertEqual(retrieved_result, {"level": "A", "spot": 1})


if __name__ == '__main__':
    unittest.main()
