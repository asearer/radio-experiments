# radio_controller.py

class RadioController:
    def __init__(self):
        self.current_frequency = None

    def search_frequency(self, frequency):
        print(f"Searching for frequency {frequency}...")
        # Code to search for the specified frequency
        self.current_frequency = frequency
        print(f"Frequency {frequency} found.")

    def select_frequency_range(self, start_frequency, end_frequency):
        print(f"Selecting frequency range from {start_frequency} to {end_frequency}...")
        # Code to select the specified frequency range
        self.current_frequency = (start_frequency, end_frequency)
        print(f"Frequency range {start_frequency} - {end_frequency} selected.")

    def get_current_frequency(self):
        return self.current_frequency
