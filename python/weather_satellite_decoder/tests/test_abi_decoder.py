import unittest
from abi_decoder import abi_decoder

class TestABIDecoder(unittest.TestCase):
    def test_decode_abi_data(self):
        # Test case 1: Decoding valid ABI data
        input_data = "0x1234567890abcdef"
        expected_output = {"key1": "value1", "key2": 12345}
        decoded_data = abi_decoder.decode_abi_data(input_data)
        self.assertEqual(decoded_data, expected_output)

        # Test case 2: Decoding empty ABI data
        input_data = ""
        expected_output = {}
        decoded_data = abi_decoder.decode_abi_data(input_data)
        self.assertEqual(decoded_data, expected_output)

        # Test case 3: Decoding invalid ABI data
        input_data = "0xabcdef"
        with self.assertRaises(Exception):
            abi_decoder.decode_abi_data(input_data)

if __name__ == '__main__':
    unittest.main()

