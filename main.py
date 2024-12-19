"""
Lens Design Efficiency Calculator
Tate Finger, Quang Huynh
"""

import numpy as np


def calculate_power_1(index, rad1):
    """
    calculates power from first surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the first surface (in mm)
    :return: Power of first surface (in 1\mm)
    """
    return (index-1)/rad1

def calculate_power_2(index, rad2):
    """
    calculates power from second surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the second surface (in mm)
    :return: Power of second surface (in 1\mm)
    """
    return (1-index)/rad2

def calculate_total_power(thickness, index, power1, power2):
    """
    calculates total power of the lens

    :param thickness: Thickness of lens (in mm)
    :param index: Refractive index of the lens material at an arbitrary wavelength
    :param power1: Power of first surface (in 1/mm)
    :param power2: Power of second surface (in 1/mm)

    :return total power of lens (in 1/mm)
    """
    return power1 + power2 - ((thickness/index)*power1*power2)

def calculate_efl(powertotal):
    """
    calculates effective focal length (efl) of lens

    :param powertotal: Total power of the lens (in 1/mm)

    :return Effective focal length (in mm)
    """
    return 1/powertotal

def calculate_numerical_aperture(diameter, efl):
    """
    calculates numerial aperature (NA) of lens

    :param diameter: Diameter of lens (in mm)
    :param ef1: Effective focal length (in mm)

    :return Numerical aperture (unitless)
    """
    return diameter/(2*efl)


def lens_calculator(index, rad1, rad2, thickness, diameter):
    """
    calculates and prints total power, effective focal length (EFL) and numerical aperature (NA) of a lens
    based on input parameters

    :param index: Refractive index of the lens material 
    :param rad1: Radius of curvature of the first surface (in mm)
    :param rad2: Radius of curvature of the second surface (in mm)
    :param thickness: Thickness of the lens (in mm) 
    :param diameter: Diameter of the lens (in mm) 
    """
    # Calculates powers, effective focal length, and numerical aperture
    power1 = calculate_power_1(index, rad1)
    power2 = calculate_power_2(index, rad2)
    powertotal = calculate_total_power(thickness, index, power1, power2)
    efl = calculate_efl(powertotal)
    NA = calculate_numerical_aperture(diameter, efl)

    # Prints calculated values
    print(f'Total Power of Lens: {powertotal: .3f} 1/mm')
    print(f'Effective Focal Length: {efl: .2f} mm')
    print(f'Numerical Aperture: {NA: .3f}')

def main():
    """
    Main function
    """
    # Variables
    index = float(input('Refractive Index: '))
    rad1 = float(input('Radius of First Surface: '))
    rad2 = float(input('Radius of Second Surface: '))
    thickness = float(input('Thickness: '))
    diameter = float(input('Diameter: ' ))

    lens_calculator(index, rad1, rad2, thickness, diameter)

# main guard
if __name__ == "__main__":
    main()