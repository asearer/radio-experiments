import unittest
from math import isclose
from distance_calculator import calculate_distance

class TestCalculateDistance(unittest.TestCase):

    def test_distance_calculation(self):
        # Test with example values
        rssi = -70
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 2.0
        expected_distance = 10.0  # Expected distance for the given example values
        calculated_distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent)
        self.assertTrue(isclose(expected_distance, calculated_distance, rel_tol=1e-9))

    def test_negative_rssi(self):
        # Test with negative RSSI
        rssi = -80
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 2.0
        with self.assertRaises(ValueError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent)

    def test_zero_reference_distance(self):
        # Test with zero reference distance
        rssi = -70
        tx_power = -50
        reference_distance = 0.0
        path_loss_exponent = 2.0
        with self.assertRaises(ValueError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent)

    def test_zero_path_loss_exponent(self):
        # Test with zero path loss exponent
        rssi = -70
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 0.0
        with self.assertRaises(ZeroDivisionError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent)

if __name__ == '__main__':
    unittest.main()
