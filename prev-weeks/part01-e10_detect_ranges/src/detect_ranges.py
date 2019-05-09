#!/usr/bin/env python3

def detect_ranges(L):
    ordered = sorted(L)
    ranges = [ordered[0]]
    for num in ordered[1:len(ordered)]:
        curr_range = ranges[-1]
        if(isinstance(curr_range, int) == 1 or curr_range[1] == num - 1):
            ranges[-1] = curr_range[0], num
        else:
            ranges.append(num, )    


    return []

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)
    
if __name__ == "__main__":
    main()
