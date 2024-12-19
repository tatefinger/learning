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
    return (index-1)/rad1

def calculate_power_2(index, rad2):
    return (1-index)/rad2

def calculate_total_power(thickness, index, power1, power2):
    return power1 + power2 - ((thickness/index)*power1*power2)

def main():
    index = float(input('Refractive Index: '))
    rad1 = float(input('Radius of First Surface: '))
    rad2= float(input('Radius of Second Surface: '))
    thickness = float(input('Thickness: '))

    power1 = calculate_power_1(index, rad1)
    power2 = calculate_power_2(index, rad2)
    powertotal = calculate_total_power(thickness, index, power1, power2)
    efl = 1/powertotal
    print(f'Total Power of Lens: {powertotal: .3f} 1/mm')
    print(f'Effective Focal Length: {efl: .2f} mm')

# main guard
if __name__ == "__main__":
    main()