import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr
from scipy.signal import decimate
import time

# Set up RTL-SDR
sdr = RtlSdr()

# Configure device
sdr.sample_rate = 2.4e6  # Hz
sdr.center_freq = 137e6   # Start scanning from 137 MHz
sdr.gain = 'auto'

# Define frequency ranges to scan (excluding GHz range)
min_freq = 137e6
max_freq = 1e9  # 1 GHz
ghz_min_freq = 2e9  # Exclude GHz range
step_size = 1e6  # 1 MHz step size

# Frequency usage lookup table (example)
frequency_usage = {
    145800000: "ISS APRS (Automatic Packet Reporting System) downlink",
    145825000: "ISS Packet Radio (Region 1) uplink",
    144490000: "ISS Packet Radio (Region 2) uplink",
    # Add more frequencies and their uses as needed
}

# File to save detected signals
output_file = "detected_signals.txt"

# Frequency scanning loop
current_freq = min_freq
with open(output_file, "w") as file:
    while current_freq < max_freq:
        # Skip GHz range frequencies
        if current_freq >= ghz_min_freq:
            current_freq += step_size
            continue

        # Set center frequency
        sdr.center_freq = current_freq

        # Capture samples
        num_samples = 1024 * 256
        samples = sdr.read_samples(num_samples)

        # Convert samples to numpy array
        samples = np.array(samples, dtype=np.complex64)

        # Downsample for processing
        decimation_factor = 10
        samples = decimate(samples, decimation_factor)

        # Calculate power spectral density (PSD)
        psd, freqs = plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate / decimation_factor)

        # Check if signal present
        max_psd = np.max(psd)
        if max_psd > 50:  # Adjust threshold as needed
            signal_info = f"Signal detected at frequency: {current_freq / 1e6} MHz\n"
            if current_freq in frequency_usage:
                signal_info += f"Possible use: {frequency_usage[current_freq]}\n"
            else:
                signal_info += "No information about the possible use.\n"
            file.write(signal_info)

        # Increment frequency
        current_freq += step_size
        time.sleep(0.1)  # Delay between frequency scans for stability

# Close device
sdr.close()
