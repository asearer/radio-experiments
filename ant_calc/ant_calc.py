import numpy as np

def calculate_antenna_size(frequency, frequency_unit):
    # Convert frequency to Hz
    if frequency_unit == 'kHz':
        frequency *= 1e3
    elif frequency_unit == 'MHz':
        frequency *= 1e6
    elif frequency_unit == 'GHz':
        frequency *= 1e9

    # Speed of light in meters per second
    speed_of_light = 3e8

    # Calculate wavelength for the frequency
    wavelength = speed_of_light / frequency

    # Calculate half-wavelength antenna size
    antenna_size = wavelength / 2

    return antenna_size

def main():
    # Get frequency and unit from user
    frequency = float(input("Enter the frequency: "))
    frequency_unit = input("Enter the frequency unit (Hz, kHz, MHz, GHz): ").strip().lower()

    # Calculate antenna size
    size = calculate_antenna_size(frequency, frequency_unit)

    print(f"The appropriate size of the antenna for the specified frequency is {size:.2f} meters.")

if __name__ == "__main__":
    main()
