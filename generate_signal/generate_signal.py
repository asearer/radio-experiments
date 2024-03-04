import numpy as np
import matplotlib.pyplot as plt

def generate_signal(freq, sample_rate, duration, waveform='sine'):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    if waveform == 'sine':
        signal = np.sin(2 * np.pi * freq * t)
    elif waveform == 'square':
        signal = np.sign(np.sin(2 * np.pi * freq * t))
    elif waveform == 'triangle':
        signal = 2 * np.abs(t * freq - np.floor(t * freq + 0.5)) - 1
    else:
        raise ValueError("Invalid waveform. Choose 'sine', 'square', or 'triangle'.")
    return signal

def add_noise(signal, snr_db):
    power_signal = np.mean(np.abs(signal) ** 2)
    power_noise = power_signal / (10 ** (snr_db / 10))
    noise = np.random.normal(0, np.sqrt(power_noise), len(signal))
    return signal + noise

def main():
    # User inputs
    frequency = float(input("Enter the frequency: "))  # Frequency in Hz
    frequency_unit = input("Enter the frequency unit (Hz, kHz, MHz, GHz): ").lower()
    sample_rate = float(input("Enter the sample rate: "))  # Sample rate in Hz
    duration = float(input("Enter the duration (in seconds): "))  # Duration in seconds
    snr_db = float(input("Enter the SNR (in dB): "))  # Signal-to-noise ratio in dB
    waveform = input("Enter the waveform (sine, square, triangle): ").lower()

    # Convert frequency to Hz based on user input
    if frequency_unit == 'khz':
        frequency *= 1e3
    elif frequency_unit == 'mhz':
        frequency *= 1e6
    elif frequency_unit == 'ghz':
        frequency *= 1e9

    # Generate signal
    signal = generate_signal(frequency, sample_rate, duration, waveform)
    signal_with_noise = add_noise(signal, snr_db)

    # Plot signals
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(signal)
    plt.title('Original Signal ({})'.format(waveform))
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.subplot(2, 1, 2)
    plt.plot(signal_with_noise)
    plt.title('Signal with Noise (SNR = {} dB)'.format(snr_db))
    plt.xlabel('Samples')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
