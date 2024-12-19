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
# FOCAL LENGTH
# LENS POWER
# NUMERICAL APERTURE

def calculate_power_1(index, rad1):
    """
    calculates power from first surface of the lens

    @param index: Refractive index of lens material
    @param rad1: Radius of curvative of the first surface (in mm)
    @return: Power of first surface (in 1\mm)
    """
    return (index-1)/rad1

def calculate_power_2(index, rad2):
    """
    calculates power from second surface of the lens

    @param index: Refractive index of lens material
    @param rad1: Radius of curvative of the second surface (in mm)
    @return: Power of second surface (in 1\mm)
    """
    return (1-index)/rad2

def calculate_total_power(thickness, index, power1, power2):
    """
    calculates total power of the lens

    @param thickness: Thickness of lens (in mm)
    @param index: Refractive index of the lens material at an arbitrary wavelength
    @param power1: Power of first surface (in 1/mm)
    @param power2: Power of second surface (in 1/mm)

    @return total power of lens (in 1/mm)
    """
    return power1 + power2 - ((thickness/index)*power1*power2)

def calculate_numerical_aperture(diameter, efl):
    """
    calculates numerial aperature (NA) of lens

    @param diameter: Diameter of lens (in mm)
    @param ef1: Effective focal length (in mm)
    
    @return Numerical aperture (dimensionless)
    """
    return diameter/(2*efl)

def main():
    index = float(input('Refractive Index: '))
    rad1 = float(input('Radius of First Surface: '))
    rad2 = float(input('Radius of Second Surface: '))
    thickness = float(input('Thickness: '))
    diameter = float(input('Diameter: ' ))

    power1 = calculate_power_1(index, rad1)
    power2 = calculate_power_2(index, rad2)
    powertotal = calculate_total_power(thickness, index, power1, power2)
    efl = 1/powertotal
    NA = calculate_numerical_aperture(diameter, efl)
    print(f'Total Power of Lens: {powertotal: .3f} 1/mm')
    print(f'Effective Focal Length: {efl: .2f} mm')
    print(f'Numerical Aperture: {NA: .3f}')

# main guard
if __name__ == "__main__":
    main()