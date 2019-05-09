#!/usr/bin/env python3

def triple(arg):
        return arg*3
    
def square(arg):
    return  arg**2

def main(): 
    nums = list(range(1, 11))   
    for num in nums:
        tripled = triple(num)
        squared = square(num)
        if(squared > tripled):
            break
        print("triple({})=={} square({})=={}".format(num, tripled, num, squared)) 
    

if __name__ == "__main__":
    main()
