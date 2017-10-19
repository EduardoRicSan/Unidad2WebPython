from math import pi
"""Description: The fucntion_area_cono calculate the area of a cone"""
"""Programmer: Jesús Eduardo Rico Sandoval"""
def area_cono(g: float, R: float, r: float) -> float:
     area = pi * (g * (R + r) + (R**2) + (r**2))
     return area
"""Description: The fucntion_area_cono calculate the volume of a cone"""
"""Programmer: Jesús Eduardo Rico Sandoval"""
def volumen_cono(h: float, R: float, r: float)-> float:
    volumen = 1/3 * ((pi*h)*((R**2) + (r**2) + (R*r)))
    return volumen

