import unittest
from oop1 import Car  # assuming oop1.py is in the same directory

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Toyota", "Camry", "blue")

    def test_attributes(self):
        self.assertEqual(self.car.brand, "Toyota")
        self.assertEqual(self.car.model, "Camry")
        self.assertEqual(self.car.color, "blue")

    def test_drive(self):
        self.assertEqual(self.car.drive(), "blue Toyota Camry is driving.")

    def test_modify_color(self):
        self.car.color = "red"
        self.assertEqual(self.car.color, "red")

if __name__ == '__main__':
    unittest.main()