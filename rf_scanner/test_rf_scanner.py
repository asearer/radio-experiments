import unittest
import numpy as np
from unittest.mock import patch
from rf_scanner import scan_frequency_range, plot_spectrum, find_peaks, scan_and_list_frequencies

class TestScanFrequencyRange(unittest.TestCase):
    def test_scan_frequency_range(self):
        start_freq = 80e6
        end_freq = 180e6
        num_samples = 1024*256
        sample_rate = 2.4e6
        spectrum = scan_frequency_range(start_freq, end_freq, num_samples, sample_rate)
        
        self.assertEqual(len(spectrum), num_samples)

class TestPlotSpectrum(unittest.TestCase):
    def test_plot_spectrum(self):
        frequencies = np.arange(100)
        spectrum = np.random.rand(100)
        with patch('matplotlib.pyplot.show') as show_mock:
            plot_spectrum(frequencies, spectrum)
            show_mock.assert_called_once()

class TestFindPeaks(unittest.TestCase):
    def test_find_peaks(self):
        frequencies = np.arange(100)
        spectrum = np.random.rand(100)
        threshold = 0.5
        peaks = find_peaks(frequencies, spectrum, threshold)
        
        self.assertIsInstance(peaks, list)

class TestScanAndListFrequencies(unittest.TestCase):
    def test_scan_and_list_frequencies(self):
        start_freq = 80e6
        end_freq = 180e6
        threshold = 20
        with patch('builtins.print') as print_mock:
            scan_and_list_frequencies(start_freq, end_freq, threshold)
            self.assertEqual(print_mock.call_count, 1)

if __name__ == '__main__':
    unittest.main()
