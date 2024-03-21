import tkinter as tk
from tkinter import ttk

import numpy as np

class AntennaSizeCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Antenna Size Calculator")

        self.frequency_var = tk.StringVar()
        self.frequency_unit_var = tk.StringVar(value="Hz")
        self.antenna_size_var = tk.StringVar()

        self.create_widgets()

    def calculate_antenna_size(self):
        frequency = float(self.frequency_var.get())
        frequency_unit = self.frequency_unit_var.get()

        # Convert frequency to Hz
        if frequency_unit == 'kHz':
            frequency *= 1e3
        elif frequency_unit == 'MHz':
            frequency *= 1e6
        elif frequency_unit == 'GHz':
            frequency *= 1e9

        # Speed of light in meters per second
        speed_of_light = 3e8

        # Calculate wavelength for the frequency
        wavelength = speed_of_light / frequency

        # Calculate half-wavelength antenna size
        antenna_size = wavelength / 2

        self.antenna_size_var.set(f"{antenna_size:.2f} meters")

    def create_widgets(self):
        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky=(tk.W, tk.E, tk.N, tk.S))

        frequency_label = ttk.Label(container, text="Frequency:")
        frequency_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        frequency_entry = ttk.Entry(container, textvariable=self.frequency_var)
        frequency_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

        frequency_unit_label = ttk.Label(container, text="Unit:")
        frequency_unit_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        frequency_unit_combobox = ttk.Combobox(container, textvariable=self.frequency_unit_var, values=["Hz", "kHz", "MHz", "GHz"])
        frequency_unit_combobox.grid(row=0, column=3, padx=5, pady=5, sticky=tk.W)

        calculate_button = ttk.Button(container, text="Calculate", command=self.calculate_antenna_size)
        calculate_button.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        result_label = ttk.Label(container, text="Antenna Size:")
        result_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

        antenna_size_label = ttk.Label(container, textvariable=self.antenna_size_var)
        antenna_size_label.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)

if __name__ == "__main__":
    app = AntennaSizeCalculator()
    app.mainloop()
