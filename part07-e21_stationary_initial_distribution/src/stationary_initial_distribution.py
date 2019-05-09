#!/usr/bin/env python3


class MarkovChain(object):

    def __init__(self, initial, transition, seed=None):
        
    def set_seed(self, seed):
        random.seed(seed)   # Reinitialize random number generator
        
    def generate(self, n):
        return ""
   
def get_stationary_distributions(transition):
    """The function get a transition matrix of degree one Markov chain as parameter.
    It returns a list of stationary distributions, in vector form, for that chain."""
    return []
    
def get_distribution(s, return_vector=False):
    """Gets a DNA sequence as input and computes the nucleotide distribution in a dict form.
    Adds pseudo count 1 to each nucleotide."""
    return {}
    
def kullback_leibler(p, q):
    """Computes Kullback-Leibler divergence between two distributions.
Both p and q must be dictionaries from events to probabilities.
The divergence is defined only when q[event] == 0 implies p[event] == 0.
"""
    return 0.0


def main():
    transition=np.array([[0.3, 0, 0.7, 0],
                         [0, 0.4, 0, 0.6],
                         [0.35, 0, 0.65, 0],
                         [0, 0.2, 0, 0.8]])
    return
    
if __name__ == "__main__":
    main()
