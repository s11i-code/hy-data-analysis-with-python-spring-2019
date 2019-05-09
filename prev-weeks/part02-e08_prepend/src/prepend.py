#!/usr/bin/env python3

class Prepend(object):
    # Add the methods of the class here
    def __init__(self, str):
        self.start = str
    
    def write(self, str):
        print(self.start + str)

def main():
    p=Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
