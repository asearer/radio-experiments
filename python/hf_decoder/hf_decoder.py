import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
import tkinter as tk
from tkinter import ttk

# Constants
SAMPLE_RATE = 2.4e6  # Sample rate of RTL-SDR
CENTER_FREQ = 7.2e6  # Center frequency for HF bands (e.g., 40 meters)
NUM_SAMPLES = int(2e5)  # Number of samples to capture

def capture_samples(sdr, num_samples, center_freq, sample_rate):
    sdr.sample_rate = sample_rate
    sdr.center_freq = center_freq
    samples = sdr.read_samples(num_samples)
    return samples

def plot_spectrum(samples, sample_rate):
    n = len(samples)
    fft_samples = np.fft.fft(samples)
    freqs = np.fft.fftfreq(n, d=1/sample_rate)
    plt.plot(freqs[:n//2], 20 * np.log10(np.abs(fft_samples[:n//2])))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (dB)')
    plt.title('Frequency Spectrum')
    plt.show()

def start_capture():
    sdr = RtlSdr()
    samples = capture_samples(sdr, NUM_SAMPLES, CENTER_FREQ, SAMPLE_RATE)
    sdr.close()
    plot_spectrum(samples, SAMPLE_RATE)

def main():
    root = tk.Tk()
    root.title("HF Radio Signal Visualization")

    label = ttk.Label(root, text="Click below to start capturing and visualizing HF radio signals:")
    label.pack(pady=10)

    capture_button = ttk.Button(root, text="Start Capture", command=start_capture)
    capture_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
