import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
from scipy.signal import decimate
import time
import threading

class FrequencyScannerApp:
    """
    GUI application for scanning frequencies and detecting signals, targeting ISS frequencies.

    Attributes:
        root (tk.Tk): The root window of the application.
        sdr (RtlSdr): Instance of RtlSdr for interacting with RTL-SDR device.
        current_freq (float): Current frequency being scanned.
        max_freq (float): Maximum frequency to scan.
        frequency_usage (dict): Dictionary mapping frequencies to their usage information.
        output_file (str): File name to save detected signals.
        scan_thread (threading.Thread): Thread for executing frequency scanning process.
    """
    
    def __init__(self, root):
        """
        Initialize the application.

        Parameters:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.root.title("ISS Frequency Scanner")
        
        self.sdr = RtlSdr()
        self.sdr.sample_rate = 2.4e6
        self.sdr.gain = 'auto'
        
        self.current_freq = 145.8e6  # Starting frequency for ISS APRS
        self.max_freq = 146e6        # Ending frequency for ISS APRS
        
        self.frequency_usage = {
            145800000: "ISS APRS (Automatic Packet Reporting System) downlink",
            145825000: "ISS Packet Radio (Region 1) uplink",
            144490000: "ISS Packet Radio (Region 2) uplink",
            # Add more frequencies and their uses as needed
        }
        
        self.output_file = "detected_iss_signals.txt"
        
        self.create_widgets()
        
    def create_widgets(self):
        """
        Create GUI widgets.
        """
        self.start_button = ttk.Button(self.root, text="Start Scanning", command=self.start_scanning)
        self.start_button.pack(pady=10)
        
        self.stop_button = ttk.Button(self.root, text="Stop Scanning", command=self.stop_scanning)
        self.stop_button.pack(pady=10)
        self.stop_button.config(state=tk.DISABLED)
        
        self.progress_label = ttk.Label(self.root, text="")
        self.progress_label.pack(pady=10)
        
        # Create a figure and canvas for plotting PSD
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack()
        
    def start_scanning(self):
        """
        Start the frequency scanning process.
        """
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        
        self.scan_thread = threading.Thread(target=self.scan_frequencies)
        self.scan_thread.start()
        
    def stop_scanning(self):
        """
        Stop the frequency scanning process.
        """
        self.stop_button.config(state=tk.DISABLED)
        self.progress_label.config(text="Stopping...")
        self.root.after(100, self.sdr.close)
        
    def scan_frequencies(self):
        """
        Scan frequencies within the specified range and detect signals.
        """
        with open(self.output_file, "w") as file:
            while self.current_freq < self.max_freq:
                self.sdr.center_freq = self.current_freq
                
                num_samples = 1024 * 256
                samples = self.sdr.read_samples(num_samples)
                samples = np.array(samples, dtype=np.complex64)
                samples = decimate(samples, 10)
                
                # Create PSD plot within the main thread
                self.plot_psd(samples)
                
                max_psd = np.max(psd)
                if max_psd > 50:
                    signal_info = f"Signal detected at frequency: {self.current_freq / 1e6} MHz\n"
                    if self.current_freq in self.frequency_usage:
                        signal_info += f"Possible use: {self.frequency_usage[self.current_freq]}\n"
                    else:
                        signal_info += "No information about the possible use.\n"
                    file.write(signal_info)
                
                self.current_freq += 25e3  # Increment by 25 kHz
                time.sleep(0.1)
                
        messagebox.showinfo("Scanning Complete", "Frequency scanning has completed.")
        self.progress_label.config(text="")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
    
    def plot_psd(self, samples):
        """
        Plot power spectral density (PSD) within the main thread.

        Parameters:
            samples (np.array): Array of signal samples.
        """
        self.ax.clear()  # Clear the previous plot
        psd, _ = plt.psd(samples, NFFT=1024, Fs=self.sdr.sample_rate / 10)
        self.ax.set_title('Power Spectral Density')
        self.ax.set_xlabel('Frequency (Hz)')
        self.ax.set_ylabel('PSD (dB/Hz)')
        self.ax.grid(True)
        self.canvas.draw()  # Redraw the plot

if __name__ == "__main__":
    root = tk.Tk()
    app = FrequencyScannerApp(root)
    root.mainloop()
