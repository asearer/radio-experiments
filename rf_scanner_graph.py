import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

def scan_frequency_range(start_freq, end_freq, num_samples=1024*256, sample_rate=2.4e6):
    sdr = RtlSdr()

    sdr.sample_rate = sample_rate
    sdr.center_freq = (start_freq + end_freq) / 2
    sdr.gain = 'auto'

    samples = sdr.read_samples(num_samples)

    sdr.close()

    spectrum = np.abs(np.fft.fft(samples))
    frequencies = np.fft.fftfreq(len(spectrum)) * (end_freq - start_freq) + start_freq

    return frequencies, spectrum

def plot_spectrum(frequencies, spectrum):
    plt.plot(frequencies, 10 * np.log10(spectrum))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power (dB)')
    plt.title('Frequency Spectrum')
    plt.show()

def find_peaks(frequencies, spectrum, threshold):
    peaks = []
    for i in range(1, len(spectrum) - 1):
        if spectrum[i] > spectrum[i-1] and spectrum[i] > spectrum[i+1] and spectrum[i] > threshold:
            peaks.append(frequencies[i])
    return peaks

def scan_and_list_frequencies(start_freq, end_freq, threshold):
    frequencies, spectrum = scan_frequency_range(start_freq, end_freq)
    plot_spectrum(frequencies, spectrum)
    peaks = find_peaks(frequencies, spectrum, threshold)
    print("Detected frequencies and their bands:")
    for freq in peaks:
        if freq >= 88e6 and freq <= 108e6:
            print(f"FM Band: {freq} Hz")
        elif freq >= 520e3 and freq <= 1710e3:
            print(f"AM Band: {freq} Hz")
        else:
            print(f"Other Band: {freq} Hz")

# Example usage
start_freq = 80e6  # Start frequency (80 MHz)
end_freq = 180e6   # End frequency (180 MHz)
threshold = 20     # Threshold for peak detection (adjust as needed)

scan_and_list_frequencies(start_freq, end_freq, threshold)
