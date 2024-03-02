import tkinter as tk
from alignment_calculator import AlignmentCalculator

class SatelliteAlignmentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Satellite/Antenna Alignment Tool")

        # Create input fields
        self.satellite_azimuth_label = tk.Label(self, text="Satellite Azimuth:")
        self.satellite_azimuth_label.grid(row=0, column=0)
        self.satellite_azimuth_entry = tk.Entry(self)
        self.satellite_azimuth_entry.grid(row=0, column=1)

        self.satellite_elevation_label = tk.Label(self, text="Satellite Elevation:")
        self.satellite_elevation_label.grid(row=1, column=0)
        self.satellite_elevation_entry = tk.Entry(self)
        self.satellite_elevation_entry.grid(row=1, column=1)

        self.antenna_azimuth_label = tk.Label(self, text="Antenna Azimuth:")
        self.antenna_azimuth_label.grid(row=2, column=0)
        self.antenna_azimuth_entry = tk.Entry(self)
        self.antenna_azimuth_entry.grid(row=2, column=1)

        self.antenna_elevation_label = tk.Label(self, text="Antenna Elevation:")
        self.antenna_elevation_label.grid(row=3, column=0)
        self.antenna_elevation_entry = tk.Entry(self)
        self.antenna_elevation_entry.grid(row=3, column=1)

        # Button to calculate alignment
        self.calculate_button = tk.Button(self, text="Calculate Alignment", command=self.calculate_alignment)
        self.calculate_button.grid(row=4, columnspan=2)

        # Labels to display alignment angles
        self.alignment_azimuth_label = tk.Label(self, text="")
        self.alignment_azimuth_label.grid(row=5, columnspan=2)
        self.alignment_elevation_label = tk.Label(self, text="")
        self.alignment_elevation_label.grid(row=6, columnspan=2)

    def calculate_alignment(self):
        # Get input values from the GUI
        satellite_azimuth = float(self.satellite_azimuth_entry.get())
        satellite_elevation = float(self.satellite_elevation_entry.get())
        antenna_azimuth = float(self.antenna_azimuth_entry.get())
        antenna_elevation = float(self.antenna_elevation_entry.get())

        # Calculate alignment angles
        alignment_azimuth, alignment_elevation = AlignmentCalculator.calculate_alignment(
            satellite_azimuth, satellite_elevation, antenna_azimuth, antenna_elevation)

        # Display alignment angles
        self.alignment_azimuth_label.config(text="Alignment Azimuth: {:.2f}".format(alignment_azimuth))
        self.alignment_elevation_label.config(text="Alignment Elevation: {:.2f}".format(alignment_elevation))

if __name__ == "__main__":
    app = SatelliteAlignmentApp()
    app.mainloop()
