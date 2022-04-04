#Sample application of pyscaltriangle's functions
import sys
sys.path.insert(1,"../pyscaltriangle")
from pyscaltriangle.operations import *

print("-"*50)
print(f"Pascal's Triangle line 5 is {pascal_line(5)}")
print("-"*50)
print(f"Sum of terms of Pascal's Triangle line 5 is {sum_line_terms(5)}")
print("-"*50)
print(f"The term located in column 2 and line 5 of Pascal's Triangle is{triangle_term(2,5)}")
print("-"*50)
print(f"Sum of terms of column 1 of Pascal's Triangle, stop in line 4, is {sum_column_terms(1,4)}")
print("-"*50)
print(f"Sum of diagonal's terms that finish in term with column 2 and line 6 is {sum_diagonal_terms(2,6)}")
print("-"*50)
print(f"The number of line 4 that is perfect triangle is {perfect_triangle(4)}")
print("-"*50)
print(f"The number of line 4 that is perfect tetrahedron is {perfect_tetrahedron(4)}")
print("-"*50)
