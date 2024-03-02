import math

def calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent):
    # Calculate distance using the log-distance path loss model
    distance = reference_distance * 10**((tx_power - rssi) / (10 * path_loss_exponent))
    return distance

# Example values
rssi = -70  # Received Signal Strength Indicator
tx_power = -50  # Transmit power
reference_distance = 1.0  # Reference distance (e.g., 1 meter)
path_loss_exponent = 2.0  # Path loss exponent

distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent)
print("Estimated distance:", distance, "meters")
