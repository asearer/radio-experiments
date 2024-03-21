import trilateration
import numpy as np

def test_trilaterate():
    # Test case 1: Simple scenario with known solution
    beacons = [(0, 0), (3, 0), (0, 4)]
    distances = [5, 4, 3]
    expected_location = (3.0, 4.0)
    assert np.allclose(trilateration.trilaterate(beacons, distances), expected_location), "Test case 1 failed"

    # Test case 2: Zero distances, expect first beacon location
    beacons = [(0, 0), (3, 0), (0, 4)]
    distances = [0, 0, 0]
    expected_location = (0.0, 0.0)
    assert np.allclose(trilateration.trilaterate(beacons, distances), expected_location), "Test case 2 failed"

    # Test case 3: Different beacon locations
    beacons = [(1, 2), (5, 7), (3, 9)]
    distances = [3, 4, 5]
    expected_location = (-3.5, 6.0)
    assert np.allclose(trilateration.trilaterate(beacons, distances), expected_location), "Test case 3 failed"

    # Test case 4: Large distances
    beacons = [(100, 200), (300, 400), (500, 600)]
    distances = [700, 800, 900]
    expected_location = (0.0, 0.0)
    assert np.allclose(trilateration.trilaterate(beacons, distances), expected_location), "Test case 4 failed"

    print("All unit tests passed successfully.")

if __name__ == "__main__":
    test_trilaterate()