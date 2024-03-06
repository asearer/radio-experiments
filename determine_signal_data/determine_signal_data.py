import numpy as np
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

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
    if peak_freq < 10e3:
        print("Type of data: Low frequency modulation (e.g., AM)")
    elif 10e3 <= peak_freq < 300e3:
        print("Type of data: Medium frequency modulation (e.g., FM)")
    elif 300e3 <= peak_freq < 1e6:
        print("Type of data: High frequency modulation (e.g., digital modulation)")
    else:
        print("Type of data: Unknown")

    # Check for audio or image data
    if peak_freq > 20e3 and peak_freq < 20e6:  # Audio frequency range
        print("Content: Audio")
    elif peak_freq > 20e6 and peak_freq < 1e9:  # Image frequency range
        print("Content: Image")
    else:
        print("Content: Unknown")

def main():
    # Configure RTL-SDR device
    sdr = RtlSdr()
    freq_unit = input("Enter frequency unit (Hz, kHz, MHz, GHz): ").lower()
    center_freq = float(input("Enter center frequency: "))

    # Convert center frequency to Hz
    if freq_unit == 'khz':
        center_freq *= 1e3
    elif freq_unit == 'mhz':
        center_freq *= 1e6
    elif freq_unit == 'ghz':
        center_freq *= 1e9

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

if __name__ == "__main__":
    main()
