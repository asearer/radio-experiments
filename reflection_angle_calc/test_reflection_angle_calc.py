import unittest
from reflection_angle_calc import calculate_reflection_angle

class TestCalculateReflectionAngle(unittest.TestCase):
    def test_omni_parabolic(self):
        self.assertAlmostEqual(calculate_reflection_angle(30, 45, "omnidirectional", "parabolic"), 60, places=2)

    def test_dir_parabolic(self):
        self.assertAlmostEqual(calculate_reflection_angle(45, 30, "directional", "parabolic"), 60, places=2)

    def test_omni_flat(self):
        self.assertAlmostEqual(calculate_reflection_angle(30, 45, "omnidirectional", "flat"), 15, places=2)

    def test_dir_flat(self):
        self.assertAlmostEqual(calculate_reflection_angle(45, 30, "directional", "flat"), -15, places=2)

    def test_invalid_combination(self):
        with self.assertRaises(ValueError):
            calculate_reflection_angle(45, 30, "invalid", "parabolic")

if __name__ == '__main__':
    unittest.main()
