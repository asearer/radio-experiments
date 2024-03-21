import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import tkinter as tk
from tkinter import ttk

def plot_spectrum(samples, sampling_rate):
    freq = np.fft.fftshift(np.fft.fftfreq(len(samples)) * sampling_rate)
    spectrum = np.fft.fftshift(np.fft.fft(samples))
    plt.plot(freq, 20 * np.log10(np.abs(spectrum)))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude (dB)')
    plt.show()

def identify_data_type(samples, sampling_rate):
    # Calculate power spectral density
    f, Pxx = plt.psd(samples, NFFT=1024, Fs=sampling_rate)

    # Simple classification based on peak frequency
    peak_freq = f[np.argmax(Pxx)]
    result_label.configure(text="Peak Frequency: {:.2f} Hz".format(peak_freq))

    # Check for audio or image data
    content = ""
    if peak_freq > 20e3 and peak_freq < 20e6:  # Audio frequency range
        content = "Audio"
    elif peak_freq > 20e6 and peak_freq < 1e9:  # Image frequency range
        content = "Image"
    else:
        content = "Unknown"
    content_label.configure(text="Content: " + content)

def capture_and_analyze():
    center_freq = float(center_freq_entry.get())
    freq_unit = freq_unit_combobox.get().lower()

    # Convert center frequency to Hz
    if freq_unit == 'khz':
        center_freq *= 1e3
    elif freq_unit == 'mhz':
        center_freq *= 1e6
    elif freq_unit == 'ghz':
        center_freq *= 1e9

    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6  # Hz
    sdr.center_freq = center_freq
    sdr.freq_correction = 60   # PPM
    sdr.gain = 'auto'

    # Capture samples
    num_samples = 1024 * 256
    samples = sdr.read_samples(num_samples)

    # Plot spectrum
    plot_spectrum(samples, sdr.sample_rate)

    # Identify data type
    identify_data_type(samples, sdr.sample_rate)

    # Close device
    sdr.close()

# GUI setup
root = tk.Tk()
root.title("Radio Signal Analyzer")

# Center Frequency Entry
center_freq_label = ttk.Label(root, text="Center Frequency:")
center_freq_label.grid(row=0, column=0)
center_freq_entry = ttk.Entry(root)
center_freq_entry.grid(row=0, column=1)
center_freq_entry.insert(tk.END, "433")  # default value

# Frequency Unit Combobox
freq_unit_label = ttk.Label(root, text="Frequency Unit:")
freq_unit_label.grid(row=1, column=0)
freq_units = ["Hz", "kHz", "MHz", "GHz"]
freq_unit_combobox = ttk.Combobox(root, values=freq_units)
freq_unit_combobox.grid(row=1, column=1)
freq_unit_combobox.current(1)  # set default value to kHz

# Capture Button
capture_button = ttk.Button(root, text="Capture and Analyze", command=capture_and_analyze)
capture_button.grid(row=2, column=0, columnspan=2)

# Result Labels
result_label = ttk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)
content_label = ttk.Label(root, text="")
content_label.grid(row=4, column=0, columnspan=2)

root.mainloop()
