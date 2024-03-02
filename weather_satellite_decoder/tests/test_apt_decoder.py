import unittest
from apt_decoder import apt_decoder

class TestAPTDecoder(unittest.TestCase):
    def test_decode_apt_signal(self):
        # Test case 1: Decoding valid APT signal
        input_signal = [0, 1, 1, 0] * 100  # Example input signal
        decoded_data = apt_decoder.decode_apt_signal(input_signal)
        self.assertEqual(decoded_data, expected_output)

        # Test case 2: Decoding invalid APT signal
        input_signal = [1, 0, 1] * 50  # Invalid input signal
        with self.assertRaises(Exception):
            apt_decoder.decode_apt_signal(input_signal)

if __name__ == '__main__':
    unittest.main()
