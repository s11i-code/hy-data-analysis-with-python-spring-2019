#!/usr/bin/env python3

import numpy as np


def random_event(dist):
    """Takes as input a dictionary from events to their probabilities.
Return a random event sampled according to the given distribution.
The probabilities must sum to 1.0"""
    # Write your solution here
    return np.random.choice(list(dist.keys()), 1, p=list(dist.values()))[0]

if __name__ == '__main__':
    distribution=dict(zip("ACGT", [0.10, 0.35, 0.15, 0.40]))
    print(random_event(distribution))

