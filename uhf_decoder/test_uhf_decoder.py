import unittest
from unittest.mock import MagicMock, patch
from uhf_decoder import capture_samples, plot_spectrum, start_capture

class TestCaptureSamples(unittest.TestCase):
    def setUp(self):
        self.sdr = MagicMock()

    def test_capture_samples(self):
        num_samples = 1000
        center_freq = 900e6
        sample_rate = 2.4e6
        samples = capture_samples(self.sdr, num_samples, center_freq, sample_rate)
        self.assertEqual(len(samples), num_samples)

class TestPlotSpectrum(unittest.TestCase):
    def test_plot_spectrum(self):
        samples = [1, 2, 3, 4, 5]
        sample_rate = 2.4e6
        with patch('matplotlib.pyplot.show') as mock_show:
            plot_spectrum(samples, sample_rate)
            mock_show.assert_called_once()

class TestStartCapture(unittest.TestCase):
    def test_start_capture(self):
        with patch('tkinter.Tk.mainloop') as mock_mainloop:
            start_capture()
            mock_mainloop.assert_called_once()

if __name__ == '__main__':
    unittest.main()
