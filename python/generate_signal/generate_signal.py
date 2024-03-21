import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def generate_signal(freq, sample_rate, duration, waveform='sine'):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    if waveform == 'sine':
        signal = np.sin(2 * np.pi * freq * t)
    elif waveform == 'square':
        signal = np.sign(np.sin(2 * np.pi * freq * t))
    elif waveform == 'triangle':
        signal = 2 * np.abs(t * freq - np.floor(t * freq + 0.5)) - 1
    else:
        raise ValueError("Invalid waveform. Choose 'sine', 'square', or 'triangle'.")
    return signal

def add_noise(signal, snr_db):
    power_signal = np.mean(np.abs(signal) ** 2)
    power_noise = power_signal / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(power_noise), len(signal))
    return signal + noise

def plot_signal(signal, signal_with_noise, waveform, snr_db):
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal)
    plt.title('Original Signal ({})'.format(waveform))
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.subplot(2, 1, 2)
    plt.plot(signal_with_noise)
    plt.title('Signal with Noise (SNR = {} dB)'.format(snr_db))
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

def generate_and_visualize():
    # Get values from entries
    frequency_str = frequency_entry.get() or '100'  # Default value: 100 Hz
    sample_rate_str = sample_rate_entry.get() or '10000'  # Default value: 10 kHz
    duration_str = duration_entry.get() or '1'  # Default value: 1 second
    snr_str = snr_entry.get() or '20'  # Default value: 20 dB

    # Validate inputs
    if not frequency_str or not sample_rate_str or not duration_str or not snr_str:
        messagebox.showerror("Error", "All fields must be filled.")
        return

    # Convert input strings to appropriate types
    try:
        frequency = float(frequency_str)  # Frequency in Hz
        sample_rate = float(sample_rate_str)  # Sample rate in Hz
        duration = float(duration_str)  # Duration in seconds
        snr_db = float(snr_str)  # Signal-to-noise ratio in dB
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        return

    waveform = waveform_combobox.get().lower()  # Waveform type

    # Generate signal
    signal = generate_signal(frequency, sample_rate, duration, waveform)
    signal_with_noise = add_noise(signal, snr_db)

    # Plot signals
    plot_signal(signal, signal_with_noise, waveform, snr_db)

# GUI setup
root = tk.Tk()
root.title("Radio Signal Mocking Application")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

# Frequency entry
frequency_label = ttk.Label(main_frame, text="Frequency:")
frequency_label.grid(column=0, row=0, sticky=tk.W)
frequency_entry = ttk.Entry(main_frame, width=10)
frequency_entry.grid(column=1, row=0)
frequency_entry.insert(tk.END, '100')

frequency_unit_combobox = ttk.Combobox(main_frame, values=["Hz", "kHz", "MHz", "GHz"], width=5)
frequency_unit_combobox.grid(column=2, row=0)
frequency_unit_combobox.current(2)

# Sample rate entry
sample_rate_label = ttk.Label(main_frame, text="Sample Rate:")
sample_rate_label.grid(column=0, row=1, sticky=tk.W)
sample_rate_entry = ttk.Entry(main_frame, width=10)
sample_rate_entry.grid(column=1, row=1)
sample_rate_entry.insert(tk.END, '10000')

# Duration entry
duration_label = ttk.Label(main_frame, text="Duration (s):")
duration_label.grid(column=0, row=2, sticky=tk.W)
duration_entry = ttk.Entry(main_frame, width=10)
duration_entry.grid(column=1, row=2)
duration_entry.insert(tk.END, '1')

# SNR entry
snr_label = ttk.Label(main_frame, text="SNR (dB):")
snr_label.grid(column=0, row=3, sticky=tk.W)
snr_entry = ttk.Entry(main_frame, width=10)
snr_entry.grid(column=1, row=3)
snr_entry.insert(tk.END, '20')

# Waveform combobox
waveform_label = ttk.Label(main_frame, text="Waveform:")
waveform_label.grid(column=0, row=4, sticky=tk.W)
waveform_combobox = ttk.Combobox(main_frame, values=["Sine", "Square", "Triangle"], width=10)
waveform_combobox.grid(column=1, row=4)
waveform_combobox.current(0)

# Generate and Visualize button
generate_button = ttk.Button(main_frame, text="Generate and Visualize", command=generate_and_visualize)
generate_button.grid(column=0, row=5, columnspan=2)

root.mainloop()
