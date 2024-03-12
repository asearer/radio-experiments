import unittest
from tkinter import TclError
from tkinter import ttk
import tkinter as tk

from ant_calc import AntennaSizeCalculator

class TestAntennaSizeCalculator(unittest.TestCase):
    def setUp(self):
        self.app = AntennaSizeCalculator()

    def test_frequency_conversion(self):
        self.app.frequency_var.set("1")
        self.app.frequency_unit_var.set("kHz")
        self.app.calculate_antenna_size()
        self.assertEqual(self.app.antenna_size_var.get(), "300000.00 meters")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.app.frequency_var.set("not_a_number")
            self.app.calculate_antenna_size()

    def test_tkinter_elements(self):
        # Check if all tkinter elements are created
        self.assertIsInstance(self.app.children['!frame'], ttk.Frame)
        self.assertIsInstance(self.app.children['!entry'], ttk.Entry)
        self.assertIsInstance(self.app.children['!combobox'], ttk.Combobox)
        self.assertIsInstance(self.app.children['!button'], ttk.Button)
        self.assertIsInstance(self.app.children['!label'], ttk.Label)

    def test_calculate_button(self):
        # Trigger button click
        self.app.calculate_antenna_size()
        self.assertEqual(self.app.antenna_size_var.get(), "")

    def test_frequency_unit_combobox(self):
        # Check if the values in frequency_unit_combobox are correct
        self.assertEqual(self.app.children['!combobox']['values'], ('Hz', 'kHz', 'MHz', 'GHz'))

    def tearDown(self):
        try:
            self.app.destroy()
        except TclError:
            # Ignore if already destroyed
            pass

if __name__ == "__main__":
    unittest.main()
