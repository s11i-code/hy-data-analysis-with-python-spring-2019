#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    sqroot_term = math.sqrt(b**2 - 4*a*c)
    denom = 2*a
    solution1 = (-b + sqroot_term)/denom
    solution2 = (-b - sqroot_term)/denom
    return (solution1, solution2)


def main():
    pass
    
if __name__ == "__main__":
    main()