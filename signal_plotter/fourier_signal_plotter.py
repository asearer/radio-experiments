import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plot_frequency_spectrum():
    # Clear previous plot
    plt.clf()
    
    # Define parameters
    frequency = float(frequency_entry.get())  # Frequency of the signal in Hz
    amplitude = float(amplitude_entry.get())  # Amplitude of the signal
    sampling_rate = 10000  # Sampling rate in samples per second
    duration = float(duration_entry.get())  # Duration of the signal in seconds

    # Generate time array
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)

    # Generate the radio signal (in this case, a sine wave)
    radio_signal = amplitude * np.sin(2 * np.pi * frequency * t)

    # Compute the Fourier transform
    freq_spectrum = np.fft.fft(radio_signal)
    freqs = np.fft.fftfreq(len(radio_signal), d=1/sampling_rate)

    # Plot the frequency spectrum
    plt.plot(freqs, np.abs(freq_spectrum))
    plt.title('Frequency Spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.tight_layout()
    
    # Update canvas
    canvas.draw()

# Create GUI
root = Tk()
root.title("Frequency Spectrum")

# Frequency Entry
Label(root, text="Frequency (Hz):").grid(row=0, column=0)
frequency_entry = Entry(root)
frequency_entry.grid(row=0, column=1)
frequency_entry.insert(0, "1000")  # Default frequency

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
plot_button = Button(root, text="Plot Spectrum", command=plot_frequency_spectrum)
plot_button.grid(row=3, columnspan=2)

# Matplotlib Figure
fig = plt.figure(figsize=(10, 4))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=4, columnspan=2)

# Start GUI main loop
root.mainloop()
