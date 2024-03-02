import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

def calculate_distance():
    try:
        rssi = float(rssi_entry.get())
        tx_power = float(tx_power_entry.get())
        reference_distance = float(reference_distance_entry.get())
        path_loss_exponent = float(path_loss_exponent_entry.get())
        model = path_loss_model.get()

        if model == 'Log Distance':
            distance = reference_distance * 10**((tx_power - rssi) / (10 * path_loss_exponent))
        elif model == 'Free Space':
            distance = reference_distance * 10**((tx_power - rssi) / (10 * 2))
        else:
            raise ValueError("Invalid path loss model. Choose either 'Log Distance' or 'Free Space'")

        result_label.config(text="Estimated distance: {:.2f} meters".format(distance))
        
        # Plotting
        num_points = 10
        distances = np.linspace(0.1, 2*distance, num_points)
        plt.figure(figsize=(10, 6))
        
        # Plotting Distance vs. RSSI
        plt.subplot(2, 2, 1)
        rssi_values = tx_power - (10 * path_loss_exponent * np.log10(distances / reference_distance))
        plt.plot(distances, rssi_values)
        plt.title('Distance vs. RSSI')
        plt.xlabel('Distance (m)')
        plt.ylabel('RSSI (dBm)')
        
        # Plotting Distance vs. Path Loss
        plt.subplot(2, 2, 2)
        path_loss_values = tx_power - rssi_values
        plt.plot(distances, path_loss_values)
        plt.title('Distance vs. Path Loss')
        plt.xlabel('Distance (m)')
        plt.ylabel('Path Loss (dB)')
        
        # Plotting RSSI vs. Path Loss
        plt.subplot(2, 2, 3)
        plt.plot(rssi_values, path_loss_values)
        plt.title('RSSI vs. Path Loss')
        plt.xlabel('RSSI (dBm)')
        plt.ylabel('Path Loss (dB)')
        
        plt.tight_layout()
        plt.show()
        
    except ValueError as e:
        result_label.config(text=str(e))

# Create main window
root = tk.Tk()
root.title("RF Distance Calculator")

# Create input fields and labels
rssi_label = ttk.Label(root, text="RSSI (dBm):")
rssi_label.grid(column=0, row=0, padx=5, pady=5)
rssi_entry = ttk.Entry(root)
rssi_entry.grid(column=1, row=0, padx=5, pady=5)

tx_power_label = ttk.Label(root, text="Transmit Power (dBm):")
tx_power_label.grid(column=0, row=1, padx=5, pady=5)
tx_power_entry = ttk.Entry(root)
tx_power_entry.grid(column=1, row=1, padx=5, pady=5)

reference_distance_label = ttk.Label(root, text="Reference Distance (m):")
reference_distance_label.grid(column=0, row=2, padx=5, pady=5)
reference_distance_entry = ttk.Entry(root)
reference_distance_entry.grid(column=1, row=2, padx=5, pady=5)

path_loss_exponent_label = ttk.Label(root, text="Path Loss Exponent:")
path_loss_exponent_label.grid(column=0, row=3, padx=5, pady=5)
path_loss_exponent_entry = ttk.Entry(root)
path_loss_exponent_entry.grid(column=1, row=3, padx=5, pady=5)

path_loss_model_label = ttk.Label(root, text="Path Loss Model:")
path_loss_model_label.grid(column=0, row=4, padx=5, pady=5)
path_loss_model = ttk.Combobox(root, values=["Log Distance", "Free Space"])
path_loss_model.grid(column=1, row=4, padx=5, pady=5)
path_loss_model.current(0)

calculate_button = ttk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.grid(column=0, row=5, columnspan=2, padx=5, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

root.mainloop()
