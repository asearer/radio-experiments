import unittest
import numpy as np
from unittest.mock import patch, MagicMock
from detect_sat_signal import detect_satellite_signal, detect_and_plot_signal

class TestSignalDetection(unittest.TestCase):
    
    def setUp(self):
        self.time = np.linspace(0, 10, 1000)
        self.signal = np.sin(2 * np.pi * 2 * self.time) + 0.5 * np.sin(2 * np.pi * 5 * self.time)
    
    def test_detect_satellite_signal(self):
        detected_peaks = detect_satellite_signal(self.signal, threshold=0.5, peak_distance=100)
        self.assertTrue(len(detected_peaks) > 0)
        self.assertIsInstance(detected_peaks, np.ndarray)
    
    @patch('detect_sat_signal.plot_signal_with_peaks')
    def test_detect_and_plot_signal(self, mock_plot_signal):
        # Mocking the plot function
        mock_plot_signal.side_effect = MagicMock()
        
        detect_and_plot_signal()
        
        # Asserting the mock function was called
        mock_plot_signal.assert_called_once()

if __name__ == '__main__':
    unittest.main()
