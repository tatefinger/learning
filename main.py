"""
Single Lens Ray Trace Simulator
Tate Finger, Quang Huynh
"""

import numpy as np
import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

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
        result_power.config(text=f'Total Power of Lens: {powertotal: .3f} (1/mm)')
        result_efl.config(text=f'Effective Focal Length: {efl: .2f} mm')
        result_na.config(text=f'Numerical Aperture: {NA: .3f}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values")


# create main window
root = ThemedTk(theme="plastik")
root.title("Ray Trace Simulator")
root.geometry("400x500")

# style configuration
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12))

# input fields & labels
fields = [
    ("Refractive Index:", "entry_index"),
    ("Radius of First Surface (mm):", "entry_rad1"),
    ("Radius of Second Surface (mm):", "entry_rad2"),
    ("Thickness (mm):", "entry_thickness"),
    ("Diameter (mm):", "entry_diameter")
]

for label_text, var_name in fields:
    ttk.Label(root, text=label_text).pack(pady=5)
    globals()[var_name] = ttk.Entry(root)
    globals()[var_name].pack(pady=5, ipadx=5)

# button to calculate results
calc_button = ttk.Button(root, text="Calculate", command=calculate_lens)
calc_button.pack(pady=20)

# labels to display results
result_power = ttk.Label(root, text="Total Power:")
result_power.pack(pady=5)

result_efl = ttk.Label(root, text="Effective Focal Length:")
result_efl.pack(pady=5)

result_na = ttk.Label(root, text="Numerical Aperture:")
result_na.pack(pady=5)

# start main loop
root.mainloop()
