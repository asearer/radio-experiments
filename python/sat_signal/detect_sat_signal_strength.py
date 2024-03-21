import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
from scipy.signal import find_peaks
from scipy.fft import fft
import matplotlib.pyplot as plt


def detect_satellite_signal(signal=None, threshold=0.5, peak_distance=100):
    if signal is None:
        # Dummy data
        signal = np.sin(2 * np.pi * np.linspace(0, 10, 1000)) + 0.5 * np.sin(2 * np.pi * 2 * np.linspace(0, 10, 1000))
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)
    return peaks


def analyze_peaks(signal=None, peaks=None, sample_rate=1.0):
    if signal is None or peaks is None:
        return np.array([]), np.array([])
    spectrum = fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sample_rate)
    peak_frequencies = frequencies[peaks]
    peak_strengths = np.abs(spectrum[peaks])
    return peak_frequencies, peak_strengths


class SatelliteSignalAnalyzerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Satellite Signal Analyzer")

        self.signal_label = ttk.Label(master, text="Signal Data:")
        self.signal_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.signal_entry = ttk.Entry(master, width=40)
        self.signal_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        self.load_button = ttk.Button(master, text="Load Signal", command=self.load_signal)
        self.load_button.grid(row=0, column=3, padx=10, pady=5)

        self.analyze_button = ttk.Button(master, text="Analyze", command=self.analyze_signal)
        self.analyze_button.grid(row=1, column=1, padx=10, pady=5)

        self.plot_button = ttk.Button(master, text="Plot", command=self.plot_signal)
        self.plot_button.grid(row=1, column=2, padx=10, pady=5)

        self.frequencies_label = ttk.Label(master, text="Detected Frequencies:")
        self.frequencies_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        self.strengths_label = ttk.Label(master, text="Strengths:")
        self.strengths_label.grid(row=2, column=2, sticky="w", padx=10, pady=5)

        self.frequencies_text = tk.Text(master, height=5, width=30)
        self.frequencies_text.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        self.strengths_text = tk.Text(master, height=5, width=30)
        self.strengths_text.grid(row=3, column=2, columnspan=2, padx=10, pady=5)

        self.signal = None
        self.sample_rate = None
        self.detected_peaks = None

    def load_signal(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                self.signal = np.loadtxt(file_path)
                self.sample_rate = 1 / (self.signal[1] - self.signal[0])
                self.signal_entry.delete(0, "end")
                self.signal_entry.insert(0, file_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load signal: {e}")

    def analyze_signal(self):
        if self.signal is not None and self.sample_rate is not None:
            try:
                self.detected_peaks = detect_satellite_signal(self.signal)
                frequencies, strengths = analyze_peaks(self.signal, self.detected_peaks, self.sample_rate)
                self.frequencies_text.delete(1.0, "end")
                self.strengths_text.delete(1.0, "end")
                for freq, strength in zip(frequencies, strengths):
                    self.frequencies_text.insert("end", f"{freq} Hz\n")
                    self.strengths_text.insert("end", f"{strength}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Analyze error: {e}")
        else:
            messagebox.showerror("Error", "Please load a signal first.")

    def plot_signal(self):
        if self.signal is not None and self.detected_peaks is not None:
            plt.plot(self.signal, label='Signal')
            plt.plot(self.detected_peaks, self.signal[self.detected_peaks], 'x', color='red', label='Detected Peaks')
            plt.xlabel('Time')
            plt.ylabel('Amplitude')
            plt.title('Satellite Signal Detection')
            plt.legend()
            plt.grid(True)
            plt.show()
        else:
            messagebox.showerror("Error", "Please analyze the signal first.")


def main():
    root = tk.Tk()
    app = SatelliteSignalAnalyzerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
