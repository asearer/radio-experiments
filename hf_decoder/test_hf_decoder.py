import unittest
import numpy as np
from hf_decoder import capture_samples, plot_spectrum

# Constants
SAMPLE_RATE = 2.4e6  # Sample rate of RTL-SDR
CENTER_FREQ = 7.2e6  # Center frequency for HF bands (e.g., 40 meters)
NUM_SAMPLES = int(2e5)  # Number of samples to capture

class TestCaptureSamples(unittest.TestCase):
    def setUp(self):
        self.sample_rate = 2.4e6
        self.center_freq = 7.2e6
        self.num_samples = int(2e5)

    def test_capture_samples_returns_array(self):
        sdr = MockRtlSdr()
        samples = capture_samples(sdr, self.num_samples, self.center_freq, self.sample_rate)
        self.assertIsInstance(samples, np.ndarray)

    # Add more test cases as needed

class TestPlotSpectrum(unittest.TestCase):
    def setUp(self):
        self.sample_rate = 2.4e6

    def test_plot_spectrum(self):
        # Generate some fake samples for testing
        num_samples = 1000
        samples = np.sin(2 * np.pi * np.arange(num_samples) * 100 / self.sample_rate)

        # Check if plot_spectrum doesn't raise errors
        try:
            plot_spectrum(samples, self.sample_rate)
        except Exception as e:
            self.fail(f"plot_spectrum raised an exception: {e}")

    # Add more test cases as needed

class MockRtlSdr:
    def __init__(self):
        pass

    def read_samples(self, num_samples):
        # Return some fake samples for testing
        return np.random.rand(num_samples)

if __name__ == '__main__':
    unittest.main()
