import unittest
from adsb_decoder import adsb_decoder

class TestADSBDecoder(unittest.TestCase):
    def test_decode_adsb_signal(self):
        # Test case 1: Decoding valid ADS-B signal
        input_signal = [0, 1, 1, 0] * 100  # Example input signal
        decoded_data = adsb_decoder.decode_adsb_signal(input_signal)
        self.assertEqual(decoded_data, expected_output)

        # Test case 2: Decoding invalid ADS-B signal
        input_signal = [1, 0, 1] * 50  # Invalid input signal
        with self.assertRaises(Exception):
            adsb_decoder.decode_adsb_signal(input_signal)

if __name__ == '__main__':
    unittest.main()
