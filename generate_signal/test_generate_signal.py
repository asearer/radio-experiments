import unittest
import numpy as np
from generate_signal import generate_signal, add_noise

class TestSignalFunctions(unittest.TestCase):
    
    def test_generate_signal(self):
        freq = 100
        sample_rate = 10000
        duration = 1
        waveform = 'sine'
        signal = generate_signal(freq, sample_rate, duration, waveform)
        self.assertEqual(len(signal), sample_rate * duration)
        
        # Test for square waveform
        waveform = 'square'
        signal = generate_signal(freq, sample_rate, duration, waveform)
        self.assertEqual(len(signal), sample_rate * duration)
        
        # Test for triangle waveform
        waveform = 'triangle'
        signal = generate_signal(freq, sample_rate, duration, waveform)
        self.assertEqual(len(signal), sample_rate * duration)

    def test_add_noise(self):
        signal = np.array([1, 2, 3, 4, 5])
        snr_db = 20
        noisy_signal = add_noise(signal, snr_db)
        self.assertEqual(len(signal), len(noisy_signal))

if __name__ == '__main__':
    unittest.main()
