"""
Single Lens Ray Trace Simulator
Tate Finger, Quang Huynh
"""


import numpy as np
from tkinter import messagebox
import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # pip install matplotlib
import matplotlib.pyplot as plt
import pyrayt  # py -m pip install pyrayt
import pyrayt.materials as matl
from tinygfx.g3d.renderers import draw


def calculate_power_1(index, rad1):
    """
    calculates power from first surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the first surface (in mm)
    :return: Power of first surface (in 1/mm)
    """
    return (index - 1) / rad1


def calculate_power_2(index, rad2):
    """
    calculates power from second surface of the lens

    :param index: Refractive index of lens material
    :param rad1: Radius of curvative of the second surface (in mm)
    :return: Power of second surface (in 1/mm)
    """
    return (1 - index) / rad2


def calculate_total_power(thickness, index, power1, power2):
    """
    calculates total power of the lens

    :param thickness: Thickness of lens (in mm)
    :param index: Refractive index of the lens material at an arbitrary wavelength
    :param power1: Power of first surface (in 1/mm)
    :param power2: Power of second surface (in 1/mm)

    :return total power of lens (in 1/mm)
    """
    return power1 + power2 - ((thickness / index) * power1 * power2)


def calculate_efl(powertotal):
    """
    calculates effective focal length (efl) of lens

    :param powertotal: Total power of the lens (in 1/mm)

    :return Effective focal length (in mm)
    """
    return 1 / powertotal


def calculate_numerical_aperture(diameter, efl):
    """
    calculates numerial aperature (NA) of lens

    :param diameter: Diameter of lens (in mm)
    :param ef1: Effective focal length (in mm)

    :return Numerical aperture (unitless)
    """
    return diameter/(2*efl)


def draw_lens_diagram(diameter, thickness, rad1, rad2):
    """
    Draws a thick lens diagram using PyRayT and Matplotlib

    :param diameter: Lens diameter (in mm).
    :param thickness: Lens thickness (in mm).
    :param rad1: Radius of curvature of the first surface (in mm).
    :param rad2: Radius of curvature of the second surface (in mm).
    """
    lens_material = matl.glass["ideal"]  # create the lens with PyRayT
    lens = pyrayt.components.thick_lens(
        r1=rad1,
        r2=rad2,
        thickness=thickness,
        aperture=diameter,
        material=lens_material
    )

    # clear existing plot
    ax.clear()
    
    # draw the lens using PyRayT's draw function
    draw(lens, axis=ax)
    
    # customize plot appearance
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.grid(True)
    canvas.draw()


def calculate_lens():
    """
    Calculates and displays lens parameters based on user input

    Computes the power of each surface, total power, effective focal length (EFL),
    and numerical aperture (NA). Displays results or shows an error for invalid input
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
        result_power.configure(text=f'Total Power of Lens: {powertotal: .3f} (1/mm)')
        result_efl.configure(text=f'Effective Focal Length: {efl: .2f} mm')
        result_na.configure(text=f'Numerical Aperture: {NA: .3f}')

        draw_lens_diagram(diameter, thickness, rad1, rad2)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values")


def main():
    """
    sets up and runs the Ray Trace Simulator GUI

    initializes input fields, calculate button and result display labels
    starts the main app loop
    """
    # create main window
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Ray Trace Simulator")
    app.geometry("400x1100")

    # diagram 
    global ax, canvas
    frame_diagram = ctk.CTkFrame(app)
    frame_diagram.pack(pady=10, fill='both', expand=True)

    # create Matplotlib Figure and Canvas
    fig, ax = plt.subplots(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=frame_diagram)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    # input fields & labels
    global entry_index, entry_rad1, entry_rad2, entry_thickness, entry_diameter
    fields = [
        ("Refractive Index:", "entry_index"),
        ("Radius of First Surface (mm):", "entry_rad1"),
        ("Radius of Second Surface (mm):", "entry_rad2"),
        ("Thickness (mm):", "entry_thickness"),
        ("Diameter (mm):", "entry_diameter")
    ]

    # style configuration
    for label_text, var_name in fields:
        ctk.CTkLabel(app, text=label_text, font=("Helvetica", 14)).pack(pady=5)
        globals()[var_name] = ctk.CTkEntry(app, font=("Helvetica", 14))
        globals()[var_name].pack(pady=5, ipadx=5)

    # button to calculate results
    calc_button = ctk.CTkButton(app, text="Calculate", command=calculate_lens)
    calc_button.pack(pady=20)

    # labels to display results
    global result_power, result_efl, result_na
    result_power = ctk.CTkLabel(app, text="Total Power:", font=("Helvetica", 14))
    result_power.pack(pady=5)

    result_efl = ctk.CTkLabel(app, text="Effective Focal Length:", font=("Helvetica", 14))
    result_efl.pack(pady=5)

    result_na = ctk.CTkLabel(app, text="Numerical Aperture:", font=("Helvetica", 14))
    result_na.pack(pady=5)

    # start the main loop
    app.mainloop()


# main guard
if __name__ == "__main__":
    main()