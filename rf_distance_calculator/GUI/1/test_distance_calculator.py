import unittest
from unittest.mock import MagicMock
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar
from distance_calculator import RFDistanceCalculator

class TestRFDistanceCalculator(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.app = RFDistanceCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_calculate_distance_log_distance(self):
        self.app.rssi_entry.insert(0, '60')
        self.app.tx_power_entry.insert(0, '20')
        self.app.reference_distance_entry.insert(0, '1')
        self.app.path_loss_exponent_entry.insert(0, '2')
        self.app.path_loss_model.set('Log Distance')

        self.app.calculate_distance()

        self.assertEqual(self.app.result_label.cget('text'), "Estimated distance: 0.10 meters")

    def test_calculate_distance_free_space(self):
        self.app.rssi_entry.insert(0, '60')
        self.app.tx_power_entry.insert(0, '20')
        self.app.reference_distance_entry.insert(0, '1')
        self.app.path_loss_exponent_entry.insert(0, '2')
        self.app.path_loss_model.set('Free Space')

        self.app.calculate_distance()

        self.assertEqual(self.app.result_label.cget('text'), "Estimated distance: 0.10 meters")

    def test_calculate_distance_invalid_model(self):
        self.app.rssi_entry.insert(0, '60')
        self.app.tx_power_entry.insert(0, '20')
        self.app.reference_distance_entry.insert(0, '1')
        self.app.path_loss_exponent_entry.insert(0, '2')
        self.app.path_loss_model.set('Invalid Model')

        self.app.calculate_distance()

        self.assertEqual(self.app.result_label.cget('text'), "Invalid path loss model. Choose either 'Log Distance' or 'Free Space'")

if __name__ == '__main__':
    unittest.main()
