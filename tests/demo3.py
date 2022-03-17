"""
View of Sierpinski's Triangle
"""
import sys
sys.path.insert(1,"../pyscaltriangle")
from pyscaltriangle.operations import pascal_line

try:
    size = int(sys.argv[1])     #triangle's size
    divisor = int(sys.argv[2])  #divisor for number in emphasis
except:
    print("Receive a number\n")
    size = 5
    divisor = 2

line_out = ""
color=False
for x in range(0, size+1):
    line = pascal_line(x)
    size = len(line)

    for i, v in enumerate(line):
        if(i+1 < len(line)):       
            
            if int(v) % divisor == 0:
                line_out += f"\033[1;36m{int(v)}\033[m "
            else:
                line_out += f"{int(v)} "
        else:
            line_out += "1 "
            print(f"{line_out}")
            line_out = ""
print(" ")