import math

def calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model='log_distance'):
    if model == 'log_distance':
        # Log-distance path loss model
        distance = reference_distance * 10**((tx_power - rssi) / (10 * path_loss_exponent))
    elif model == 'free_space':
        # Free space path loss model
        distance = reference_distance * 10**((tx_power - rssi) / (10 * 2))
    else:
        raise ValueError("Invalid path loss model. Choose either 'log_distance' or 'free_space'")
    return distance

# Input parameters
rssi = float(input("Enter RSSI (dBm): "))
tx_power = float(input("Enter transmit power (dBm): "))
reference_distance = float(input("Enter reference distance (meters): "))
path_loss_exponent = float(input("Enter path loss exponent: "))
model = input("Choose path loss model (log_distance or free_space): ").strip().lower()

# Calculate distance
try:
    distance = calculate_distance(rssi, tx_power, reference_distance, path_loss_exponent, model)
    print("Estimated distance:", distance, "meters")
except ValueError as e:
    print(e)
