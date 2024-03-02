import pybufrkit

def decode_bufr_data(file_path):
    print("Decoding BUFR data...")
    # Read BUFR file
    with open(file_path, 'rb') as f:
        bufr_data = f.read()
    # Decode BUFR data
    decoded_messages = pybufrkit.process_file(file_path, apply_filters=False)
    decoded_data = []
    for message in decoded_messages:
        # Extract relevant data from the decoded message
        data = {}
        for dataset in message.datasets:
            data[dataset.name] = dataset.value
        decoded_data.append(data)
    return decoded_data

# Example usage:
# decoded_data = decode_bufr_data("path/to/your/bufr_file.bufr")
# print(decoded_data)
