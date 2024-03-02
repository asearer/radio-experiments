import unittest
from your_script_name import calculate_distance

class TestRFDistanceCalculator(unittest.TestCase):
    def test_log_distance_model(self):
        # Test with log distance model
        rssi = -70
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 2.0
        expected_distance = 10.0
        calculated_distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model='log_distance')
        self.assertAlmostEqual(calculated_distance, expected_distance, places=2)

    def test_free_space_model(self):
        # Test with free space model
        rssi = -70
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 2.0
        expected_distance = 100.0
        calculated_distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model='free_space')
        self.assertAlmostEqual(calculated_distance, expected_distance, places=2)

    def test_invalid_model(self):
        # Test with invalid model
        rssi = -70
        tx_power = -50
        reference_distance = 1.0
        path_loss_exponent = 2.0
        with self.assertRaises(ValueError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model='invalid_model')

    def test_negative_values(self):
        # Test with negative values
        rssi = -70
        tx_power = -50
        reference_distance = -1.0
        path_loss_exponent = -2.0
        with self.assertRaises(ValueError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model='log_distance')

if __name__ == '__main__':
    unittest.main()
