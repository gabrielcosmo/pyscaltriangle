from .mathFormules import binomio
from .exceptions import TriangleException
#from modules.equationReturn import Equation


def triangle_term(a, b, n, p):
    """
    Implementation of the formula of the Newton's Binomio.
    :param a: Binomio's first term
    :param b: Binomio's second term
    :param n: Pow's Number
    :param p: Term's Position
    :return: Pascal's Triangle term. Type: int
    """
    p -= 1
    t = binomio(n, p) * a ** (n - binomio(n, p)) * b ** binomio(n, p)
    return t

def pascal_line(n):
    """
    Calcule of Line's terms n. Column and Lines are counts initializing of 0.
    :param n: Line's Number.
    :return: Terms of line. Type: list
    """
    r = []
    for p in range(0, n):
        r.append(binomio(n, p))
    r.append(1)
    return r

def sum_line_terms(n):
    """
    Sum of terms of line n. Column and Lines are counts initializing of 0.
    :param n: Line's Number.
    :return: Line's terms sum. Type: int
    """
    return  2**n

def sum_column_terms(col, lines):
    """
    Calculate the sum of all terms of the column 'col'. Column and Lines are counts initializing of 0.
    :param col: Column's number
    :param lines: Line's number limit
    :return: Column's terms sum. Type: int
    """
    return triangle_term(col+1, lines+1)

def sum_diagonal_terms(col,line):
    """
    a soma dos numeros de uma dignonal é igual ao número abaixo do último termo dessa diagonal considerada.
    :param col: Column's number
    :param line: Line's number
    :return: Diagonal's terms sum. Type: int
    """
    #por corrigir!
    if col == 0 or col == line: return line + 1
    else: return triangle_term(col, line+1)

def triangle_term(c,l):
    """
    Identifies the specific term of the Pascal Triangle, using the column number and the line number. (count from 0).
    Exemple:
        Line 3: 1, 2, 1
        triangle_term(2,3) return 1
    :param c: Collumn's number.
    :param l: Line's number.
    :return: Pascal's Triangle term, know your position in triangle. Type: int
    """
    line = pascal_line(l)
    return line[c]

def in_triangle(n):
    pass #se o termo n existe no triangulo

def fibonacci_sequence(l):
    pass # soma dos números das diagonais direita-esquerda (0,1,1,2,3,5,8...)

def line_string(l, string=False):
    """
    The lines' number, join, are powers of 11 base and expoent l.
    :param l: Line's number
    :param string: if True the return is formated as string
    :return: Line's term formated as int or string, depend of string's value. Type: int || string
    """
    if string: return f"{11**l}"
    else: return 11*l

def diagonal_triangle(n):
    """
    The number of column 2 are perfect triangles
    :param n: Line's number, of where want the  perfect triangle
    :return: The number of column 2, Type: int
    """
    return pascal_line(n)[2]

def diagonal_tetrahedron(n):
    """
    The number of column 3 are perfect tetrahedron
    :param n: Line's number, of where want the  perfect tetrahedron
    :return: The number of column 3, Type: int
    """
    return pascal_line(n)[3]


def sierpinski_triangle(r, n):
    pass # todos os numeros divisiveis por n se destacados formam fractais no triangulo

#Obs: nomes das funções devem ser em letra minuscula e separadas pos _
"""
+Example of Pascal's Triangle :
column: 0 1 2 3 4 5
line 0: 1
line 1: 1 1
line 2: 1 2 1
line 3: 1 3 3 1
line 4: 1 4 6 4 1
line 5: 1 5 10 10 1
"""