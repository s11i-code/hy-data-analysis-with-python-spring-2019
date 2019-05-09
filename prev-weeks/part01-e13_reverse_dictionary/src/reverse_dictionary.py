#!/usr/bin/env python3

def reverse_dictionary(d):
    reversed = {}
    for key, words in d.items():
        for word in words:
            if word in reversed:
                reversed[word].append(key)
            else:
                reversed[word] = [key]   
    return reversed 

def main():
    print(reverse_dictionary({"move":["liikuttaa"],"keep secret": ["salata"], "hide":["piilottaa", "salata"]}))

if __name__ == "__main__":
    main()
