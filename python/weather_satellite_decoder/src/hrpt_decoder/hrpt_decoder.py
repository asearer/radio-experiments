import numpy as np
from scipy.signal import medfilt

def decode_hrpt_signal(samples):
    print("Decoding HRPT signal...")
    # Perform median filtering to remove noise
    filtered_samples = medfilt(samples, kernel_size=5)
    
    # Decode the HRPT signal - Example logic
    decoded_data = []
    for sample in filtered_samples:
        # Example decoding logic: assuming thresholding for now
        if sample > 0.5:
            decoded_data.append(1)
        else:
            decoded_data.append(0)
    
    return decoded_data

# Example usage:
# decoded_signal = decode_hrpt_signal(samples)
# print(decoded_signal)

