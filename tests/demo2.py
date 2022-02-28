"""
View of Pascal's Triangle
"""
import sys
sys.path.insert(1,"../pyscaltriangle")
from pyscaltriangle.operations import pascal_line

try:
    size = int(sys.argv[1])
except:
    print("Receive a number\n")
    size = 5

line_out = ""
for x in range(0,size+1):
    line = pascal_line(x)
    size = len(line)

    for i, v in enumerate(line):
        if(i+1 < len(line)):
            line_out += f"{int(v)} "
        else:
            line_out += "1 "
            print(f"{line_out}")
            line_out = ""
print(" ")