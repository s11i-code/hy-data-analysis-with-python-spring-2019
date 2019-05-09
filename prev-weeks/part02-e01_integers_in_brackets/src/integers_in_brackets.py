#!/usr/bin/env python3
import re

def integers_in_brackets(s):
    nums = re.findall(r"\[[\s]*([+|-]{0,1}\d+)[\s]*\]", s)
    return [int(num) for num  in nums]

def main():
    print(integers_in_brackets("  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"))
    print(integers_in_brackets(" afd [128+] [47 ] [a34]  [ +-43 ]tt [+12]xx"))

if __name__ == "__main__":
    main()
