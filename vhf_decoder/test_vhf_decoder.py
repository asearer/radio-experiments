import unittest
import numpy as np
from unittest.mock import MagicMock
from vhf_decoder import capture_samples, plot_spectrum

class TestCaptureSamples(unittest.TestCase):
    def test_capture_samples_returns_array(self):
        sdr = MagicMock()
        num_samples = 100
        center_freq = 100e6
        sample_rate = 2.4e6
        samples = capture_samples(sdr, num_samples, center_freq, sample_rate)
        self.assertIsInstance(samples, np.ndarray)

    def test_capture_samples_correct_length(self):
        sdr = MagicMock()
        num_samples = 100
        center_freq = 100e6
        sample_rate = 2.4e6
        samples = capture_samples(sdr, num_samples, center_freq, sample_rate)
        self.assertEqual(len(samples), num_samples)

class TestPlotSpectrum(unittest.TestCase):
    def test_plot_spectrum(self):
        # Generate sample data for testing
        sample_rate = 1000  # Hz
        duration = 1  # seconds
        num_samples = int(sample_rate * duration)
        freq = 10  # Hz
        t = np.linspace(0, duration, num_samples)
        samples = np.sin(2 * np.pi * freq * t)

        # Call plot_spectrum and suppress showing plot
        plt = MagicMock()
        plot_spectrum(samples, sample_rate)

        # Check if plot function was called with correct arguments
        plt.plot.assert_called_once()
        args, kwargs = plt.plot.call_args
        self.assertIsInstance(args[0], np.ndarray)
        self.assertIsInstance(args[1], np.ndarray)
        self.assertEqual(len(args[0]), num_samples//2)
        self.assertEqual(len(args[1]), num_samples//2)
        self.assertEqual(kwargs['xlabel'], 'Frequency (Hz)')
        self.assertEqual(kwargs['ylabel'], 'Magnitude (dB)')
        self.assertEqual(kwargs['title'], 'Frequency Spectrum')

if __name__ == '__main__':
    unittest.main()
