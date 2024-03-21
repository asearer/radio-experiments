import unittest
from hrpt_decoder import hrpt_decoder

class TestHRPTDecoder(unittest.TestCase):
    def test_decode_hrpt_signal(self):
        # Test case 1: Decoding valid HRPT signal
        input_signal = [0, 1, 1, 0] * 100  # Example input signal
        decoded_data = hrpt_decoder.decode_hrpt_signal(input_signal)
        self.assertEqual(decoded_data, expected_output)

        # Test case 2: Decoding invalid HRPT signal
        input_signal = [1, 0, 1] * 50  # Invalid input signal
        with self.assertRaises(Exception):
            hrpt_decoder.decode_hrpt_signal(input_signal)

if __name__ == '__main__':
    unittest.main()
