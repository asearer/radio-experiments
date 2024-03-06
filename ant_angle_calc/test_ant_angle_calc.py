import unittest
from ant_angle_calc import calculate_antenna_angle

class TestCalculateAntennaAngle(unittest.TestCase):
    def test_calculate_antenna_angle(self):
        # Test with known values
        self.assertAlmostEqual(calculate_antenna_angle(100, 10), 5.710593, places=6)
        self.assertAlmostEqual(calculate_antenna_angle(200, 20), 5.710593, places=6)
        self.assertAlmostEqual(calculate_antenna_angle(150, 15), 5.710593, places=6)
    
    def test_calculate_antenna_angle_with_zero_distance(self):
        # Test with zero distance
        self.assertRaises(ZeroDivisionError, calculate_antenna_angle, 0, 10)
    
    def test_calculate_antenna_angle_with_negative_distance(self):
        # Test with negative distance
        self.assertRaises(ValueError, calculate_antenna_angle, -100, 10)
    
    def test_calculate_antenna_angle_with_negative_height(self):
        # Test with negative height
        self.assertRaises(ValueError, calculate_antenna_angle, 100, -10)

if __name__ == '__main__':
    unittest.main()
