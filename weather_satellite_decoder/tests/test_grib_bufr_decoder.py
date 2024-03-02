import unittest
from grib_bufr_decoder import grib_decoder, bufr_decoder

class TestGRIBBUFRDecoder(unittest.TestCase):
    def test_decode_grib_data(self):
        # Test case 1: Decoding valid GRIB data
        grib_file_path = "test_data/example.grib"
        decoded_data = grib_decoder.decode_grib_data(grib_file_path)
        self.assertIsNotNone(decoded_data)

        # Test case 2: Decoding invalid GRIB data
        with self.assertRaises(Exception):
            grib_decoder.decode_grib_data("invalid_file.grib")

    def test_decode_bufr_data(self):
        # Test case 1: Decoding valid BUFR data
        bufr_file_path = "test_data/example.bufr"
        decoded_data = bufr_decoder.decode_bufr_data(bufr_file_path)
        self.assertIsNotNone(decoded_data)

        # Test case 2: Decoding invalid BUFR data
        with self.assertRaises(Exception):
            bufr_decoder.decode_bufr_data("invalid_file.bufr")

if __name__ == '__main__':
    unittest.main()
