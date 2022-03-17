from .mathFormules import binomio
from .exceptions import InexistenceTerm

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
    term = 0
    try:
        term = pascal_line(l)[c]
    except IndexError as ie:
        raise InexistenceTerm(ie)
    else:
        return term

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
    try:
        return pascal_line(n)[3]
    except IndexError as ie:
        raise InexistenceTerm(ie) 


def sierpinski_triangle(d, num_lines):
    """
    :d: divisor
    :lines: number of line
    """
    sier_tri = []
    line = []

    for x in range(0, num_lines): 
        for y in pascal_line(x):
            
            if y % d == 0:
                line.append(y)
                
        sier_tri.append(line.copy())
        line.clear()
    return sier_tri


    #pass  todos os numeros divisiveis por n se destacados formam fractais no triangulo

def in_triangle(n):
    """
    Return True if the number n exists in Triangle.
    :param n: number
    :return: boolean  
    """

    r = False
    for l in range(1, n + 1):       
        if(n in pascal_line(l)):
            r = True

    return r

def fibonacci_sequence(l):
    pass # soma dos números das diagonais direita-esquerda (0,1,1,2,3,5,8...)

def diagonal(col_init, line_init, length=1, to_rigth=True):
    """
    ...
    :param col_init: first term's column of diagonal
    :param l: finish first term's line of diagonal
    :param to_rigth: true if follow to direction rigth-left in the diagonal
    """
    c = col_init
    l = line_init
    loop = l + length
    dgn = []

    while l < loop:
        t = triangle_term(c, l)
        dgn.append(t)

        if to_rigth:
            c += 1
        else:
            if t == 1 and (loop - l < length): #term equals 1 / finish term of line, and this check is not the first of while loop
                break
            else:
                c -= 1
        l += 1    
    
    return dgn

"""
+Example of Pascal's Triangle:
column: 0 1 2 3 4 5
line 0: 1
line 1: 1 1
line 2: 1 2 1
line 3: 1 3 3 1
line 4: 1 4 6 4 1
line 5: 1 5 10 5 1
"""