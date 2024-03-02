def decode_adsb_signal(samples):
    # This function decodes a list of ADS-B samples into messages.
    print("Decoding ADS-B signal...")
    decoded_messages = []
    
    # Loop through each sample in the list
    for sample in samples:
        # Decode each sample and append the decoded message to the list
        decoded_message = decode_adsb_sample(sample)
        decoded_messages.append(decoded_message)
    
    # Return the list of decoded messages
    return decoded_messages

def decode_adsb_sample(sample):
    # This function decodes a single ADS-B sample into a message.
    # Check if the first element of the sample indicates a valid ADS-B signal
    if sample[0] == 1:
        # If it's a valid signal, construct the message
        return construct_adsb_message(sample)
    else:
        # If it's not a valid signal, return an indication of invalidity
        return "Invalid ADS-B signal"

def construct_adsb_message(sample):
    # This function constructs an ADS-B message using data from the sample.
    # Extract aircraft ID and altitude from the sample
    aircraft_id = sample[1]
    altitude = sample[2]
    
    # Construct the message using the extracted data
    message = f"Aircraft {aircraft_id} at altitude {altitude} feet"
    
    # Return the constructed message
    return message

# Example usage:
# decoded_messages = decode_adsb_signal(samples)
# print(decoded_messages)
