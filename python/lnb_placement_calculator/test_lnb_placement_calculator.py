import unittest
from lnb_placement_calculator import calculate_angles_and_distance

class TestCalculateAnglesAndDistance(unittest.TestCase):
    def test_calculate_angles_and_distance(self):
        # Test case with a dish diameter of 2 meters
        angle_to_center, angle_to_edge, distance_to_center = calculate_angles_and_distance(2)
        self.assertAlmostEqual(angle_to_center, 26.565, places=3)
        self.assertAlmostEqual(angle_to_edge, 14.036, places=3)
        self.assertAlmostEqual(distance_to_center, 2.828, places=3)

        # Test case with a dish diameter of 4 meters
        angle_to_center, angle_to_edge, distance_to_center = calculate_angles_and_distance(4)
        self.assertAlmostEqual(angle_to_center, 26.565, places=3)
        self.assertAlmostEqual(angle_to_edge, 7.125, places=3)
        self.assertAlmostEqual(distance_to_center, 5.657, places=3)

        # Test case with a dish diameter of 8 meters
        angle_to_center, angle_to_edge, distance_to_center = calculate_angles_and_distance(8)
        self.assertAlmostEqual(angle_to_center, 26.565, places=3)
        self.assertAlmostEqual(angle_to_edge, 3.554, places=3)
        self.assertAlmostEqual(distance_to_center, 11.314, places=3)

if __name__ == '__main__':
    unittest.main()
