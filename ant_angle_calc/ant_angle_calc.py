import tkinter as tk
from tkinter import messagebox
import math

def calculate_antenna_angle(distance, height):
    """
    Calculate the appropriate antenna angle based on distance and height.
    Args:
    - distance: Distance from the antenna to the target (in meters).
    - height: Height of the antenna above the ground (in meters).
    Returns:
    - The calculated angle in degrees.
    """
    angle_radians = math.atan(height / distance)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

def calculate_angle():
    try:
        distance = float(distance_entry.get())
        height = float(height_entry.get())
        choice = use_case_var.get()
        
        if choice == 1:
            use_case = "Astronomy"
        elif choice == 2:
            use_case = "Radar"
        elif choice == 3:
            use_case = "Wireless Communication"
        elif choice == 4:
            use_case = "Weather Monitoring"

        angle = calculate_antenna_angle(distance, height)
        result_label.config(text=f"The appropriate antenna angle for {use_case} is: {angle:.2f} degrees")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for distance and height.")

# Create main window
root = tk.Tk()
root.title("Antenna Angle Calculator")

# Use case selection
use_case_var = tk.IntVar()
use_case_frame = tk.Frame(root)
use_case_frame.pack()
tk.Label(use_case_frame, text="Select Use Case:").pack(anchor="w")
tk.Radiobutton(use_case_frame, text="Astronomy", variable=use_case_var, value=1).pack(anchor="w")
tk.Radiobutton(use_case_frame, text="Radar", variable=use_case_var, value=2).pack(anchor="w")
tk.Radiobutton(use_case_frame, text="Wireless Communication", variable=use_case_var, value=3).pack(anchor="w")
tk.Radiobutton(use_case_frame, text="Weather Monitoring", variable=use_case_var, value=4).pack(anchor="w")

# Distance input
distance_frame = tk.Frame(root)
distance_frame.pack()
tk.Label(distance_frame, text="Distance to target (meters):").pack(side="left")
distance_entry = tk.Entry(distance_frame)
distance_entry.pack(side="left")

# Height input
height_frame = tk.Frame(root)
height_frame.pack()
tk.Label(height_frame, text="Height of antenna (meters):").pack(side="left")
height_entry = tk.Entry(height_frame)
height_entry.pack(side="left")

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_angle)
calculate_button.pack()

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

# Run the main event loop
root.mainloop()
