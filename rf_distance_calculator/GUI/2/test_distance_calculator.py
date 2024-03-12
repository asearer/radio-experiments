import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tkinter import ttk
import numpy as np

# Import the function to be tested
from distance_calculator import calculate_distance

class TestCalculateDistance(unittest.TestCase):

    def setUp(self):
        # Create a mock Tkinter root window
        self.root = tk.Tk()
        self.root.title("RF Distance Calculator")
        
        # Create widgets
        self.rssi_entry = ttk.Entry(self.root)
        self.tx_power_entry = ttk.Entry(self.root)
        self.reference_distance_entry = ttk.Entry(self.root)
        self.path_loss_exponent_entry = ttk.Entry(self.root)
        self.path_loss_model = ttk.Combobox(self.root, values=["Log Distance", "Free Space"])
        self.result_label = ttk.Label(self.root, text="")

    def test_calculate_distance_log_distance(self):
        # Set up values for log distance model
        self.rssi_entry.get = MagicMock(return_value="-60")
        self.tx_power_entry.get = MagicMock(return_value="-50")
        self.reference_distance_entry.get = MagicMock(return_value="1")
        self.path_loss_exponent_entry.get = MagicMock(return_value="2")
        self.path_loss_model.get = MagicMock(return_value="Log Distance")
        
        # Call the function
        calculate_distance()
        
        # Assert the result label text
        self.assertEqual(self.result_label.cget("text"), "Estimated distance: 0.10 meters")

    def test_calculate_distance_free_space(self):
        # Set up values for free space model
        self.rssi_entry.get = MagicMock(return_value="-60")
        self.tx_power_entry.get = MagicMock(return_value="-50")
        self.reference_distance_entry.get = MagicMock(return_value="1")
        self.path_loss_exponent_entry.get = MagicMock(return_value="2")
        self.path_loss_model.get = MagicMock(return_value="Free Space")
        
        # Call the function
        calculate_distance()
        
        # Assert the result label text
        self.assertEqual(self.result_label.cget("text"), "Estimated distance: 1.00 meters")

    def tearDown(self):
        # Destroy the mock Tkinter root window
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()
