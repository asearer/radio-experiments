import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def detect_satellite_signal(signal, threshold=0.5, peak_distance=100):
    """
    Detect satellite signals in a given signal.

    Args:
    - signal (array-like): The input signal.
    - threshold (float): Threshold for peak detection.
    - peak_distance (int): Minimum peak distance.

    Returns:
    - peaks (array): Indices of detected peaks.
    """

    # Find peaks in the signal
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)

    return peaks


def plot_signal_with_peaks(time, signal, detected_peaks):
    plt.plot(time, signal, label='Noisy Signal')
    plt.plot(time[detected_peaks], signal[detected_peaks], 'x', color='red', label='Detected Peaks')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Satellite Signal Detection')
    plt.legend()
    plt.grid(True)
    plt.show()


def detect_and_plot_signal():
    try:
        threshold = float(threshold_entry.get()) if threshold_entry.get() else 0.5
        peak_distance = int(peak_distance_entry.get()) if peak_distance_entry.get() else 100

        time = np.linspace(0, 10, 1000)
        signal = np.sin(2 * np.pi * 2 * time) + 0.5 * np.sin(2 * np.pi * 5 * time)

        noise = np.random.normal(0, 0.2, signal.shape)
        noisy_signal = signal + noise

        detected_peaks = detect_satellite_signal(noisy_signal, threshold, peak_distance)

        plot_signal_with_peaks(time, noisy_signal, detected_peaks)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter valid threshold and peak distance.")


# Create main application window
root = tk.Tk()
root.title("Satellite Signal Detection")

# Create input fields with default values
threshold_label = ttk.Label(root, text="Threshold:")
threshold_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
threshold_entry = ttk.Entry(root)
threshold_entry.insert(0, '0.5')
threshold_entry.grid(row=0, column=1, padx=5, pady=5)

peak_distance_label = ttk.Label(root, text="Peak Distance:")
peak_distance_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
peak_distance_entry = ttk.Entry(root)
peak_distance_entry.insert(0, '100')
peak_distance_entry.grid(row=1, column=1, padx=5, pady=5)

# Create detection button
detect_button = ttk.Button(root, text="Detect and Plot Signal", command=detect_and_plot_signal)
detect_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Run the application
root.mainloop()
