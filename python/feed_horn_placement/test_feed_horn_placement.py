import unittest
from unittest.mock import MagicMock
import numpy as np
import tkinter as tk
from feed_horn_placement import FeedHornPlacementApp

class TestFeedHornPlacementApp(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = FeedHornPlacementApp(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_init(self):
        self.assertIsInstance(self.app.master, tk.Tk)
        self.assertEqual(self.root.title(), "Feed Horn Placement App")
        self.assertIsInstance(self.app.focal_length_label, tk.Label)
        self.assertIsInstance(self.app.focal_length_entry, tk.Entry)
        self.assertIsInstance(self.app.calculate_button, tk.Button)
        self.assertIsInstance(self.app.canvas, tk.Canvas)

    def test_calculate(self):
        # Mocking entry value
        self.app.focal_length_entry.get = MagicMock(return_value="10")
        self.app.visualize_dish = MagicMock()

        self.app.calculate()

        self.app.focal_length_entry.get.assert_called_once()
        self.app.visualize_dish.assert_called_once_with(10.0)

    def test_parabolic_reflector(self):
        x = np.array([1, 2, 3])
        y = np.array([4, 5, 6])
        focal_length = 10
        result = self.app.parabolic_reflector(x, y, focal_length)

        expected_result = np.array([0.64, 1.6, 2.88])
        np.testing.assert_array_almost_equal(result, expected_result)

    def test_visualize_dish(self):
        self.app.canvas.delete = MagicMock()
        self.app.parabolic_reflector = MagicMock(return_value=np.zeros((100, 100)))

        self.app.visualize_dish(10)

        self.app.canvas.delete.assert_called_once()
        self.app.parabolic_reflector.assert_called_once()

if __name__ == "__main__":
    unittest.main()
