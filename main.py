"""
Lens Design Efficiency Calculator
Tate Finger, Quang Huynh
"""

import numpy as np

# diameter of lens
# radius 1
# radius 2
# material
# thickness
#
# d = diameter
# f = focal_length
# h=f*tan(f/2d)

def calculate_hfov(diameter_size, focal_length):
    """
    calculates the half field of view at a given diameter size & focal length

    @param diameter_size Size of diameter (in meters)
    @param focal_length Effective focal length of the lens (in meters)

    @return field of view in degrees
    """
    return np.degrees(focal_length / (2 * diameter_size))

def calculate_sensor_size(hfov, focal_length):
    """
    calculates sensor size based on half field of view (HFOV) & focal length

    @param hfov Half field of view in degrees
    @param focal_length Focal length of lens (in whatever units)

    @return radius of sensor size
    """
    return focal_length * np.tan(hfov*np.pi/180)

def main():
    diameter_size = int(input('Diameter: '))
    focal_length = int(input('Focal Length: '))

    hfov = calculate_hfov(diameter_size, focal_length)
    sensor_size = calculate_sensor_size(hfov, focal_length)
    print(f"HOV: {hfov}")
    print(f"Sensor size: {sensor_size}")




# main guard
if __name__ == "__main__":
    main()