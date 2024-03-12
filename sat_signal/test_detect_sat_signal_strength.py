import unittest
import numpy as np
from detect_sat_signal_strength import detect_satellite_signal, analyze_peaks

class TestSignalAnalyzer(unittest.TestCase):
    def setUp(self):
        self.signal = np.array([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])
    
    def test_detect_satellite_signal(self):
        peaks = detect_satellite_signal(self.signal, threshold=0.5, peak_distance=1)
        self.assertEqual(len(peaks), 3)  # Assuming 3 peaks in the provided signal
    
    def test_analyze_peaks(self):
        peaks = detect_satellite_signal(self.signal, threshold=0.5, peak_distance=1)
        frequencies, strengths = analyze_peaks(self.signal, peaks, sample_rate=1.0)
        self.assertEqual(len(frequencies), len(peaks))
        self.assertEqual(len(strengths), len(peaks))

if __name__ == '__main__':
    unittest.main()
