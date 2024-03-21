from satpy import Scene

def decode_abi_data(file_path):
    print("Decoding ABI data...")
    # Load the ABI data
    scene = Scene(reader='abi_l1b', filenames=file_path)
    # Load the ABI bands
    scene.load(['true_color'])
    # Return the loaded data
    return scene

# Example usage:
# decoded_data = decode_abi_data("path/to/your/abi_file.nc")
# print(decoded_data)
