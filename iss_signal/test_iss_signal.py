import unittest
import numpy as np
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock
from iss_signal import *

class TestSDR(unittest.TestCase):

    def setUp(self):
        self.sdr = RtlSdr()

    def tearDown(self):
        self.sdr.close()

    def test_set_sample_rate(self):
        self.sdr.sample_rate = 2.4e6
        self.assertEqual(self.sdr.sample_rate, 2.4e6)

    def test_set_center_freq(self):
        self.sdr.center_freq = 137e6
        self.assertEqual(self.sdr.center_freq, 137e6)

    def test_set_gain(self):
        self.sdr.gain = 'auto'
        self.assertEqual(self.sdr.gain, 'auto')

    @patch('iss_signal.open')
    def test_file_write(self, mock_open):
        with patch('builtins.open', mock_open):
            with open(output_file, 'w') as file:
                file.write("Test content")
            mock_open.assert_called_once_with(output_file, 'w')
            file.write.assert_called_once_with("Test content")

    def test_skip_ghz_range(self):
        self.sdr.center_freq = 2.5e9
        self.assertNotIn(2.5e9, range(int(min_freq), int(max_freq)))

    def test_detect_signal(self):
        psd_mock = MagicMock(return_value=np.array([40, 60, 30]))
        freqs_mock = MagicMock(return_value=np.array([1, 2, 3]))
        with patch('matplotlib.pyplot.psd', side_effect=[(psd_mock(), freqs_mock())]):
            signal_detected = detect_signal(50)
            self.assertTrue(signal_detected)

    def test_no_signal_detection(self):
        psd_mock = MagicMock(return_value=np.array([40, 30, 20]))
        freqs_mock = MagicMock(return_value=np.array([1, 2, 3]))
        with patch('matplotlib.pyplot.psd', side_effect=[(psd_mock(), freqs_mock())]):
            signal_detected = detect_signal(50)
            self.assertFalse(signal_detected)

if __name__ == '__main__':
    unittest.main()
