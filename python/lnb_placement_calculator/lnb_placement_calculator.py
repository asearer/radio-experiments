import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def calculate_angles_and_distance(dish_diameter):
    focal_length = dish_diameter / 2
    angle_to_center = np.arctan(1 / 2)
    angle_to_edge = np.arctan(1 / 2) - np.arctan(1 / (2 * dish_diameter))
    distance_to_center = focal_length / np.cos(angle_to_center)
    return np.degrees(angle_to_center), np.degrees(angle_to_edge), distance_to_center

def visualize_angles_and_distance(dish_diameter):
    angle_to_center, angle_to_edge, distance_to_center = calculate_angles_and_distance(dish_diameter)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)
    ax.set_title('LNB Placement Angles')
    ax.plot([0, np.radians(angle_to_center)], [0, distance_to_center], label='Angle to Center')
    ax.plot([0, np.radians(angle_to_edge)], [0, distance_to_center], label='Angle to Edge')
    ax.set_rlabel_position(-22.5)
    ax.legend(loc='upper right')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=4, columnspan=2)

def calculate():
    try:
        diameter = float(diameter_entry.get())
        angle_to_center, angle_to_edge, distance_to_center = calculate_angles_and_distance(diameter)
        result_label.config(text=f"Angle to Center: {angle_to_center:.2f} degrees\n"
                                 f"Angle to Edge: {angle_to_edge:.2f} degrees\n"
                                 f"Distance to Center: {distance_to_center:.2f} meters")
        visualize_angles_and_distance(diameter)
    except ValueError:
        result_label.config(text="Please enter a valid diameter.")

window = tk.Tk()
window.title("LNB Placement Calculator")

diameter_label = ttk.Label(window, text="Enter dish diameter (meters):")
diameter_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

diameter_entry = ttk.Entry(window)
diameter_entry.grid(row=0, column=1, padx=10, pady=5)

calculate_button = ttk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=1, columnspan=2, padx=10, pady=5)

result_label = ttk.Label(window, text="")
result_label.grid(row=2, columnspan=2, padx=10, pady=5)

window.mainloop()
