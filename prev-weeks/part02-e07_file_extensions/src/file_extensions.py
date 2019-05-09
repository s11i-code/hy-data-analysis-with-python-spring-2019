#!/usr/bin/env python3

#!/usr/bin/env python3
import sys
import re

def get_path(filename):
    import sys
    import os
    return os.path.join(os.path.dirname(sys.argv[0]), "..", "src", filename)

def parse(line):
    if('.' in line):
        return re.findall(r'(.+)\.(\w+?)\n', line)[0]
    return (line.strip('\n'), None)

def file_extensions(filename):
    f = open(get_path(filename), 'r')
    lines = f.readlines()
    extensions = {}
    without_extension  = []
    for line in lines:
        parsed = parse(line)
        if parsed[1] == None:
            without_extension.append(parsed[0])
        elif parsed[1] in extensions:
            extensions[parsed[1]].append("%s.%s" % parsed)
        else:
            extensions[parsed[1]] = ["%s.%s" % parsed]
    
    return (without_extension, extensions)

def main():
    without_extension, extensions = file_extensions("filenames.txt")
    print("{} files with no extension".format(len(without_extension)))
    for key, val in sorted(extensions.items()):
        print("{} {} \n".format(key, len(val)))

if __name__ == "__main__":
    main()        