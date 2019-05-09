#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def cols_to_zero_3d(array, cols):
    array = array.copy()
    for col in cols:
        array[:, :, col] = 0
    return array

def to_red(img):
    return cols_to_zero_3d(img, [1, 2])

def to_green(img):
    return cols_to_zero_3d(img, [0, 2])

def to_blue(img):
    return cols_to_zero_3d(img, [0, 1])

def to_grayscale(img):
    weighted_rgb = (0.2126, 0.7152, 0.0722) * img
    grayscale = np.sum(weighted_rgb, axis=2)
    return grayscale

def main():
    painting = plt.imread(get_path("painting.png"))
    grayscale = to_grayscale(painting)
    red_comp = to_red(painting)
    blue_comp = to_blue(painting)
    green_comp = to_green(painting)
    plt.imshow(grayscale, cmap='gray')
    plt.show()
    fig, ax = plt.subplots(3, 1)
    ax[0].imshow(red_comp)
    ax[1].imshow(green_comp)
    ax[2].imshow(blue_comp)
    plt.show()


if __name__ == "__main__":
    main()
