#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def center(a):
    return (0,0)   # note the order: (center_y, center_x)
    
def radial_distance(a):
    return np.array([[]])

def scale(a, tmin=0.0, tmax=1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
[tmin,tmax]."""
    return np.array([[]])
    
def radial_mask(a):
    return np.array([[]])
    
def radial_fade(a):
    return np.array([[]])
    
def main():
    
if __name__ == "__main__":
    main()
