"""
Single Lens Ray Trace Simulator
Tate Finger, Quang Huynh
"""

import numpy as np
import tkinter as tk
from tkinter import messagebox


def calculate_power_1(index, rad1):
    """
    calculates power from first surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the first surface (in mm)
    :return: Power of first surface (in 1/mm)
    """
    return (index-1)/rad1

def calculate_power_2(index, rad2):
    """
    calculates power from second surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the second surface (in mm)
    :return: Power of second surface (in 1/mm)
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


def calculate_lens():
    """
    calculates and prints total power, effective focal length (EFL) and numerical aperature (NA) of a lens
    based on input parameters

    :param index: Refractive index of the lens material 
    :param rad1: Radius of curvature of the first surface (in mm)
    :param rad2: Radius of curvature of the second surface (in mm)
    :param thickness: Thickness of the lens (in mm) 
    :param diameter: Diameter of the lens (in mm) 
    """
    try:
        # get values from entry fields
        index = float(entry_index.get())
        rad1 = float(entry_rad1.get())
        rad2 = float(entry_rad2.get())
        thickness = float(entry_thickness.get())
        diameter = float(entry_diameter.get())

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
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values")


# create main window
root = tk.Tk()
root.title("Ray Trace Simulator")
root.geometry("400x400")

# input fields & labels
tk.Label(root, text="Refractive Index: ").pack(pady=5)
entry_index = tk.Entry(root)
entry_index.pack(pady=5)

tk.Label(root, text="Radius of First Surface (mm): ").pack(pady=5)
entry_rad1 = tk.Entry(root)
entry_rad1.pack(pady=5)

tk.Label(root, text="Radius of Second Surface (mm): ").pack(pady=5)
entry_rad2 = tk.Entry(root)
entry_rad2.pack(pady=5)

tk.Label(root, text="Thickness (mm): ").pack(pady=5)
entry_thickness = tk.Entry(root)
entry_thickness.pack(pady=5)

tk.Label(root, text="Diameter (mm): ").pack(pady=5)
entry_diameter = tk.Entry(root)
entry_diameter.pack(pady=5)

# button to calculate results
calc_button = tk.Button(root, text="Calculate", command=calculate_lens)
calc_button.pack(pady=20)

# labels to display results
result_power = tk.Label(root, text="Total Power: ")
result_power.pack(pady=5)

result_efl = tk.Label(root, text="Effective Focal Length: ")
result_efl.pack(pady=5)

result_na = tk.Label(root, text="Numerical Aperature: ")
result_na.pack(pady=5)

# start main loop
root.mainloop()



# main guard
if __name__ == "__main__":
    main()