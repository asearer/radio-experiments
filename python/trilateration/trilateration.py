import numpy as np
import matplotlib.pyplot as plt

def trilaterate(beacons, distances):
    """
    Trilateration function to estimate the location of the target using beacon coordinates and distances.
    
    Args:
    - beacons (list of tuples): Coordinates of beacons in the format [(x1, y1), (x2, y2), ...].
    - distances (list of floats): Distances from the target to each beacon.
    
    Returns:
    - Tuple: Estimated coordinates (x, y) of the target.
    """
    A = np.array([[2 * (beacons[i][0] - beacons[0][0]), 2 * (beacons[i][1] - beacons[0][1])] for i in range(1, len(beacons))])
    b = np.array([distances[0]**2 - distances[i]**2 - beacons[0][0]**2 + beacons[i][0]**2 - beacons[0][1]**2 + beacons[i][1]**2 for i in range(1, len(beacons))])
    solution = np.linalg.solve(A.T @ A, A.T @ b)
    x = solution[0]
    y = solution[1]
    return x, y

def plot_trilateration(beacons, distances, target_location):
    """
    Plot the beacons, target location, and circles representing distances.
    
    Args:
    - beacons (list of tuples): Coordinates of beacons in the format [(x1, y1), (x2, y2), ...].
    - distances (list of floats): Distances from the target to each beacon.
    - target_location (tuple): Estimated coordinates (x, y) of the target.
    """
    plt.figure()
    
    # Plot beacons
    for beacon in beacons:
        plt.plot(beacon[0], beacon[1], 'bo')
    
    # Plot target location
    plt.plot(target_location[0], target_location[1], 'ro', label='Estimated Target Location')
    
    # Plot circles representing distances
    for i in range(len(beacons)):
        circle = plt.Circle(beacons[i], distances[i], color='gray', fill=False, linestyle='dotted')
        plt.gca().add_patch(circle)
    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Trilateration')
    plt.axis('equal')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
beacons = [(0, 0), (3, 0), (0, 4)]  # Coordinates of the beacons
distances = [5, 4, 3]  # Distances from the target to each beacon

target_location = trilaterate(beacons, distances)
print("Estimated target location:", target_location)

plot_trilateration(beacons, distances, target_location)
