import unittest
from distance_calculator import calculate_distance

class TestDistanceCalculator(unittest.TestCase):

    def test_log_distance_model(self):
        rssi = -70
        tx_power = -20
        reference_distance = 1
        path_loss_exponent = 2
        model = 'log_distance'
        expected_distance = 10  # Calculated manually
        calculated_distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model)
        self.assertAlmostEqual(calculated_distance, expected_distance, delta=0.01)

    def test_free_space_model(self):
        rssi = -70
        tx_power = -20
        reference_distance = 1
        path_loss_exponent = 2
        model = 'free_space'
        expected_distance = 100  # Calculated manually
        calculated_distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model)
        self.assertAlmostEqual(calculated_distance, expected_distance, delta=0.01)

    def test_invalid_model(self):
        rssi = -70
        tx_power = -20
        reference_distance = 1
        path_loss_exponent = 2
        model = 'invalid_model'
        with self.assertRaises(ValueError):
            calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model)

if __name__ == '__main__':
    unittest.main()
