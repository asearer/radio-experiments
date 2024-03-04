import math

def calculate_antenna_angle(distance, height):
    """
    Calculate the appropriate antenna angle based on distance and height.
    Args:
    - distance: Distance from the antenna to the target (in meters).
    - height: Height of the antenna above the ground (in meters).
    Returns:
    - The calculated angle in degrees.
    """
    angle_radians = math.atan(height / distance)
    angle_degrees = math.degrees(angle_radians)
    return angle_degrees

def main():
    print("Welcome to the Antenna Angle Calculator!")
    print("Select an option:")
    print("1. Astronomy")
    print("2. Radar")
    print("3. Wireless Communication")
    print("4. Weather Monitoring")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice in [1, 2, 3, 4]:
        distance = float(input("Enter the distance to the target (in meters): "))
        height = float(input("Enter the height of the antenna above the ground (in meters): "))

        if choice == 1:
            print("The appropriate antenna angle for astronomy is:", calculate_antenna_angle(distance, height), "degrees")
        elif choice == 2:
            print("The appropriate antenna angle for radar is:", calculate_antenna_angle(distance, height), "degrees")
        elif choice == 3:
            print("The appropriate antenna angle for wireless communication is:", calculate_antenna_angle(distance, height), "degrees")
        elif choice == 4:
            print("The appropriate antenna angle for weather monitoring is:", calculate_antenna_angle(distance, height), "degrees")

    else:
        print("Invalid choice. Please select either 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
