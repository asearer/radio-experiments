import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

def detect_signals():
    # Configure RTL-SDR
    sdr = RtlSdr()
    sdr.sample_rate = 2.4e6
    sdr.center_freq = 100e6  # Start scanning from 100 MHz
    sdr.gain = 'auto'

    # Scan parameters
    num_samples = 1024
    num_scans = 100
    detection_threshold = -40  # Adjust this threshold based on your environment

    # Start scanning
    print("Scanning for radio signals...")
    for _ in range(num_scans):
        samples = sdr.read_samples(num_samples)
        spectrum = np.abs(np.fft.fftshift(np.fft.fft(samples))) ** 2

        # Find peaks in the spectrum
        peaks = np.where(spectrum > np.percentile(spectrum, 95))[0]

        # Log detected signals
        for peak in peaks:
            freq = sdr.center_freq + (peak - len(samples) / 2) * sdr.sample_rate / len(samples)
            power = 10 * np.log10(spectrum[peak])
            if power > detection_threshold:
                print(f"Detected signal at {freq / 1e6} MHz with power {power:.2f} dB")

    sdr.close()

if __name__ == "__main__":
    detect_signals()
