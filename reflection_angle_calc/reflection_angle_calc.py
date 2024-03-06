import math
import matplotlib.pyplot as plt
from matplotlib.patches import Arrow
import tkinter as tk
from tkinter import messagebox

def calculate_reflection_angle(incident_angle, surface_angle, antenna_setup, dish_style):
    if antenna_setup == "omnidirectional" and dish_style == "parabolic":
        # For omnidirectional antenna and parabolic dish
        reflection_angle_deg = 2 * surface_angle - incident_angle
    elif antenna_setup == "directional" and dish_style == "parabolic":
        # For directional antenna and parabolic dish
        reflection_angle_deg = 2 * surface_angle - incident_angle
    elif antenna_setup == "omnidirectional" and dish_style == "flat":
        # For omnidirectional antenna and flat surface
        reflection_angle_deg = surface_angle - incident_angle
    elif antenna_setup == "directional" and dish_style == "flat":
        # For directional antenna and flat surface
        reflection_angle_deg = surface_angle - incident_angle
    else:
        raise ValueError("Invalid combination of antenna setup and dish style")
    
    return reflection_angle_deg

def visualize_reflection(incident_angle, surface_angle, reflection_angle):
    # Create a figure and axis
    fig, ax = plt.subplots()
    
    # Draw incident ray
    ax.arrow(0, 0, math.cos(math.radians(incident_angle)), math.sin(math.radians(incident_angle)), 
             head_width=0.1, head_length=0.2, fc='blue', ec='blue', label='Incident Ray')
    
    # Draw surface
    ax.plot([0, math.cos(math.radians(surface_angle))], [0, math.sin(math.radians(surface_angle))], 'k--', label='Surface')
    
    # Draw reflection ray
    ax.arrow(0, 0, -math.cos(math.radians(reflection_angle)), math.sin(math.radians(reflection_angle)), 
             head_width=0.1, head_length=0.2, fc='red', ec='red', label='Reflection Ray')
    
    # Set plot limits and aspect ratio
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)
    ax.set_aspect('equal', adjustable='box')
    
    # Set labels and legend
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    
    plt.title('Radio Signal Reflection')
    
    # Show plot
    plt.show()

def calculate_and_visualize():
    try:
        incident_angle = float(incident_entry.get())
        surface_angle = float(surface_entry.get())
        antenna_setup = antenna_setup_var.get()
        dish_style = dish_style_var.get()
        
        reflection_angle = calculate_reflection_angle(incident_angle, surface_angle, antenna_setup, dish_style)
        reflection_angle_label.config(text="Reflection angle: {:.2f} degrees".format(reflection_angle))
        
        visualize_reflection(incident_angle, surface_angle, reflection_angle)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for incident angle and surface angle.")

# Create main window
root = tk.Tk()
root.title("Radio Signal Reflection Calculator")

# Create labels and entry widgets
incident_label = tk.Label(root, text="Incident Angle (degrees):")
incident_label.grid(row=0, column=0, padx=10, pady=5)
incident_entry = tk.Entry(root)
incident_entry.grid(row=0, column=1, padx=10, pady=5)

surface_label = tk.Label(root, text="Surface Angle (degrees):")
surface_label.grid(row=1, column=0, padx=10, pady=5)
surface_entry = tk.Entry(root)
surface_entry.grid(row=1, column=1, padx=10, pady=5)

antenna_setup_label = tk.Label(root, text="Antenna Setup:")
antenna_setup_label.grid(row=2, column=0, padx=10, pady=5)
antenna_setup_var = tk.StringVar()
antenna_setup_var.set("omnidirectional")
antenna_setup_options = ["omnidirectional", "directional"]
antenna_setup_menu = tk.OptionMenu(root, antenna_setup_var, *antenna_setup_options)
antenna_setup_menu.grid(row=2, column=1, padx=10, pady=5)

dish_style_label = tk.Label(root, text="Dish Style:")
dish_style_label.grid(row=3, column=0, padx=10, pady=5)
dish_style_var = tk.StringVar()
dish_style_var.set("parabolic")
dish_style_options = ["parabolic", "flat"]
dish_style_menu = tk.OptionMenu(root, dish_style_var, *dish_style_options)
dish_style_menu.grid(row=3, column=1, padx=10, pady=5)

reflection_angle_label = tk.Label(root, text="")
reflection_angle_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate and Visualize", command=calculate_and_visualize)
calculate_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the GUI loop
root.mainloop()
