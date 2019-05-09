#!/usr/bin/env python3
import fractions 

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __add__(self, other):
        numer = (self.denom * other.numer) + (other.denom * self.numer)
        denom = other.denom * self.denom
        gcd = fractions.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))
    
    def __sub__(self, other):
        numer = (other.denom * self.numer) - (self.denom * other.numer) 
        denom = other.denom * self.denom
        gcd = fractions.gcd(numer, denom)
        return Rational(int(numer/gcd), int(denom/gcd))
    
    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = other.denom * self.denom
        return Rational(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = other.numer * self.denom
        return Rational(numer, denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom    
            
    def __str__(self):
        return "{}/{}".format(self.numer, self.denom)    
        
    def __gt__(self, other):
        return float(self.numer)/self.denom > float(other.numer)/other.denom
     
    def __lt__(self, other):
        return float(self.numer)/self.denom < float(other.numer)/other.denom

def main():
    r1 = Rational(1,4)
    r2 = Rational(1,4)
    r3 = Rational(3,4)

    print(r1 + r2)
    print(r3 - r1)
    print(r3 * r1)
    print(r3 / r1)
    print(r3 == r1)
    print(r2 == r1)
    print(r1 > r3)
    print(r3 > r1)
    print(r3 < r2)
    print(r2 < r3)








if __name__ == "__main__":
    main()
