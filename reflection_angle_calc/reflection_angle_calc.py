import math

def calculate_reflection_angle(incident_angle, surface_angle):
    # Convert angles from degrees to radians
    incident_angle_rad = math.radians(incident_angle)
    surface_angle_rad = math.radians(surface_angle)
    
    # Calculate reflection angle using the law of reflection
    reflection_angle_rad = math.pi - incident_angle_rad - surface_angle_rad
    
    # Convert reflection angle from radians to degrees
    reflection_angle_deg = math.degrees(reflection_angle_rad)
    
    return reflection_angle_deg

def main():
    incident_angle = float(input("Enter incident angle (in degrees): "))
    surface_angle = float(input("Enter surface angle (in degrees): "))
    
    reflection_angle = calculate_reflection_angle(incident_angle, surface_angle)
    
    print("Reflection angle:", reflection_angle, "degrees")

if __name__ == "__main__":
    main()
