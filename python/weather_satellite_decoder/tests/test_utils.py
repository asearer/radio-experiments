import unittest
from utils import signal_utils

class TestUtils(unittest.TestCase):
    def test_demodulate_signal(self):
        # Test case 1: Demodulating valid signal
        input_signal = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]  # Example input signal
        demodulated_signal = signal_utils.demodulate_signal(input_signal)
        self.assertEqual(demodulated_signal, expected_output)

        # Test case 2: Demodulating invalid signal
        input_signal = [1, 0, 1, 1, 2, 0, 1]  # Invalid input signal
        with self.assertRaises(Exception):
            signal_utils.demodulate_signal(input_signal)

    def test_sync_signal(self):
        # Test case 1: Synchronizing valid signal
        input_signal = [0, 1, 0, 1, 1, 0, 1, 0, 1, 1]  # Example input signal
        synchronized_signal = signal_utils.sync_signal(input_signal)
        self.assertEqual(synchronized_signal, expected_output)

        # Test case 2: Synchronizing invalid signal
        input_signal = [1, 0, 1, 1, 2, 0, 1]  # Invalid input signal
        with self.assertRaises(Exception):
            signal_utils.sync_signal(input_signal)

if __name__ == '__main__':
    unittest.main()
