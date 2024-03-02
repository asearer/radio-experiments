from radio_controller import RadioController

# Initialize radio controller
radio = RadioController()

# Example usage: Searching for a specific frequency
search_frequency = 100.5  # Example frequency
radio.search_frequency(search_frequency)

# Example usage: Selecting a frequency range
start_frequency = 90.0  # Example start frequency
end_frequency = 110.0  # Example end frequency
radio.select_frequency_range(start_frequency, end_frequency)

# Get current frequency or frequency range
current_frequency = radio.get_current_frequency()
print("Current frequency or frequency range:", current_frequency)
