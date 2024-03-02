import numpy as np
from scipy.signal import find_peaks
from scipy.fft import fft

def detect_satellite_signal(signal, threshold=0.5, peak_distance=100):
    """
    Detect satellite signals in a given signal.

    Args:
    - signal (array-like): The input signal.
    - threshold (float): Threshold for peak detection.
    - peak_distance (int): Minimum peak distance.

    Returns:
    - peaks (array): Indices of detected peaks.
    """

    # Find peaks in the signal
    peaks, _ = find_peaks(signal, height=threshold, distance=peak_distance)

    return peaks

def analyze_peaks(signal, peaks, sample_rate):
    """
    Analyze the detected peaks to determine frequency and strength.

    Args:
    - signal (array-like): The input signal.
    - peaks (array-like): Indices of detected peaks.
    - sample_rate (float): Sampling rate of the signal.

    Returns:
    - frequencies (array): Frequencies corresponding to the peaks.
    - strengths (array): Strengths of the detected signals.
    """

    # Calculate the Fourier Transform of the signal
    spectrum = fft(signal)

    # Get frequencies corresponding to each index in the spectrum
    frequencies = np.fft.fftfreq(len(signal), 1 / sample_rate)

    # Extract frequencies and strengths of the peaks
    peak_frequencies = frequencies[peaks]
    peak_strengths = np.abs(spectrum[peaks])

    return peak_frequencies, peak_strengths

# Example usage:
if __name__ == "__main__":
    # Generate a synthetic satellite signal
    time = np.linspace(0, 10, 1000)
    sample_rate = 1 / (time[1] - time[0])
    signal = np.sin(2 * np.pi * 2 * time) + 0.5 * np.sin(2 * np.pi * 5 * time)

    # Add noise to the signal
    noise = np.random.normal(0, 0.2, signal.shape)
    noisy_signal = signal + noise

    # Detect satellite signals
    detected_peaks = detect_satellite_signal(noisy_signal)

    # Analyze detected peaks
    frequencies, strengths = analyze_peaks(noisy_signal, detected_peaks, sample_rate)

    # Plot the original signal, detected peaks, frequencies, and strengths
    import matplotlib.pyplot as plt
    plt.plot(time, noisy_signal, label='Noisy Signal')
    plt.plot(time[detected_peaks], noisy_signal[detected_peaks], 'x', color='red', label='Detected Peaks')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Satellite Signal Detection')
    plt.legend()
    plt.grid(True)
    plt.show()

    # Print the detected frequencies and strengths
    for freq, strength in zip(frequencies, strengths):
        print(f"Frequency: {freq} Hz, Strength: {strength}")
