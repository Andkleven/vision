# Horizontal field of view 62.2 degrees
# Vertical field of view 48.8 degrees
from math import atan

def field_of_view(length, horizontal=True, vertical=False):
    degrees = 48.8
    if horizontal: degrees = 62.2
    return atan(degrees)*length