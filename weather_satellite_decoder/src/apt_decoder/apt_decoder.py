import numpy as np

def decode_apt_signal(samples):
    print("Decoding APT signal...")
    # Convert samples to binary using thresholding
    threshold = np.mean(samples)
    binary_signal = [1 if sample > threshold else 0 for sample in samples]
    return binary_signal

# Example usage:
# decoded_signal = decode_apt_signal(samples)
# print(decoded_signal)

