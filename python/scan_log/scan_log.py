import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from rtlsdr import RtlSdr

class SignalDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Radio Signal Detector")

        self.fig, self.ax = plt.subplots(figsize=(8, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.start_button = tk.Button(master, text="Start", command=self.start_detection)
        self.start_button.pack(side=tk.LEFT)

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_detection)
        self.stop_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(master, text="Quit", command=master.quit)
        self.quit_button.pack(side=tk.LEFT)

        self.sdr = None
        self.scan_active = False
        self.detection_threshold = -40

    def start_detection(self):
        if not self.scan_active:
            self.scan_active = True
            self.sdr = RtlSdr()
            self.sdr.sample_rate = 2.4e6
            self.sdr.center_freq = 100e6  # Start scanning from 100 MHz
            self.sdr.gain = 'auto'
            self.scan_spectrum()

    def stop_detection(self):
        if self.scan_active:
            self.scan_active = False
            self.sdr.close()

    def scan_spectrum(self):
        if self.scan_active:
            samples = self.sdr.read_samples(1024)
            spectrum = np.abs(np.fft.fftshift(np.fft.fft(samples))) ** 2
            self.ax.clear()
            self.ax.plot(spectrum)
            self.ax.set_xlabel('Frequency')
            self.ax.set_ylabel('Power')
            self.ax.set_title('Spectrum')
            self.fig.canvas.draw()

            peaks = np.where(spectrum > np.percentile(spectrum, 95))[0]
            detected_signals = []
            for peak in peaks:
                freq = self.sdr.center_freq + (peak - len(samples) / 2) * self.sdr.sample_rate / len(samples)
                power = 10 * np.log10(spectrum[peak])
                if power > self.detection_threshold:
                    detected_signals.append((freq, power))

            if detected_signals:
                print("Detected signals:")
                for signal in detected_signals:
                    print(f"Frequency: {signal[0] / 1e6} MHz, Power: {signal[1]:.2f} dB")

        self.master.after(1000, self.scan_spectrum)

def main():
    root = tk.Tk()
    app = SignalDetectorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
