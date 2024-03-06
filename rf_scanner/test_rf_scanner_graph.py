import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import MagicMock, patch
from rf_scanner_graph import scan_frequency_range, plot_spectrum, find_peaks, scan_and_list_frequencies

class TestFunctions(unittest.TestCase):
    
    def test_scan_frequency_range(self):
        # Create a mock RtlSdr object
        sdr_mock = MagicMock()
        sdr_mock.read_samples.return_value = np.random.randn(1024*256) + 1j * np.random.randn(1024*256)
        
        with patch('rf_scanner_graph.RtlSdr', return_value=sdr_mock):
            frequencies, spectrum = scan_frequency_range(80e6, 180e6)
            self.assertEqual(len(frequencies), 1024*256)
            self.assertEqual(len(spectrum), 1024*256)

    def test_plot_spectrum(self):
        frequencies = np.linspace(80e6, 180e6, 1024*256)
        spectrum = np.abs(np.random.randn(1024*256))
        with patch('rf_scanner_graph.plt.show') as show_mock:
            plot_spectrum(frequencies, spectrum)
            show_mock.assert_called_once()

    def test_find_peaks(self):
        frequencies = np.linspace(80e6, 180e6, 1024*256)
        spectrum = np.abs(np.random.randn(1024*256))
        threshold = 1
        peaks = find_peaks(frequencies, spectrum, threshold)
        self.assertTrue(all(spectrum[i] > spectrum[i-1] and spectrum[i] > spectrum[i+1] and spectrum[i] > threshold for i in range(1, len(peaks)-1)))

    def test_scan_and_list_frequencies(self):
        start_freq = 80e6
        end_freq = 180e6
        threshold = 20
        with patch('builtins.print') as print_mock:
            scan_and_list_frequencies(start_freq, end_freq, threshold)
            print_mock.assert_called()
        
if __name__ == '__main__':
    unittest.main()
