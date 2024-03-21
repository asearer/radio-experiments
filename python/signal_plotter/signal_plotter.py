import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_radio_signal():
    # Clear previous plot
    plt.clf()
    
    # Define parameters
    frequencies = [float(f.strip()) for f in frequency_entry.get().split(',')]  # Frequencies of the signals in Hz
    amplitude = float(amplitude_entry.get())  # Amplitude of the signal
    sampling_rate = 10000  # Sampling rate in samples per second
    duration = float(duration_entry.get())  # Duration of the signal in seconds

    # Generate time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Plot the signal for each frequency
    for freq in frequencies:
        radio_signal = amplitude * np.sin(2 * np.pi * freq * t)
        plt.plot(t, radio_signal, label=f'{freq} Hz')

    plt.title('Simulated Radio Signals')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()

    # Update canvas
    canvas.draw()

# Create GUI
root = Tk()
root.title("Simulated Radio Signals")

# Frequency Entry
Label(root, text="Frequencies (Hz):").grid(row=0, column=0)
frequency_entry = Entry(root)
frequency_entry.grid(row=0, column=1)
frequency_entry.insert(0, "1000, 2000, 3000")  # Example frequencies

# Amplitude Entry
Label(root, text="Amplitude:").grid(row=1, column=0)
amplitude_entry = Entry(root)
amplitude_entry.grid(row=1, column=1)
amplitude_entry.insert(0, "1")

# Duration Entry
Label(root, text="Duration (s):").grid(row=2, column=0)
duration_entry = Entry(root)
duration_entry.grid(row=2, column=1)
duration_entry.insert(0, "1")

# Plot Button
plot_button = Button(root, text="Plot Signals", command=plot_radio_signal)
plot_button.grid(row=3, columnspan=2)

# Matplotlib Figure
fig = plt.figure(figsize=(10, 6))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=4, columnspan=2)

# Start GUI main loop
root.mainloop()
