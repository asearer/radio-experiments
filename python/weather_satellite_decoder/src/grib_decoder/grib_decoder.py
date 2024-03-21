import pygrib

def decode_grib_data(file_path):
    print("Decoding GRIB data...")
    # Open the GRIB file
    with open(file_path, 'rb') as f:
        # Read GRIB messages from the file
        grbs = pygrib.open(file_path)
        # Initialize a list to store decoded data
        decoded_data = []
        # Iterate over each GRIB message
        for grb in grbs:
            # Extract relevant information from the GRIB message
            data = {
                'parameter_name': grb.parameterName,
                'parameter_units': grb.parameterUnits,
                'values': grb.values,
                # Add more fields as needed
            }
            # Append the decoded data to the list
            decoded_data.append(data)
    return decoded_data

# Example usage:
# decoded_data = decode_grib_data("path/to/your/grib_file.grib")
# print(decoded_data)
