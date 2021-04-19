import math

def print_triangle():
    for e in triangle:
        print(e)


def half_rshift_triange(k):
    for i in range(len(triangle)//2):
        triangle[i] = ' '*(3*2**k)+triangle[i]+' '*(3*2**k)


def add_current_triangle_twice():
    for i in range(len(triangle)):
        triangle.append(triangle[i]*2)


N = int(input())
triangle = ['  *   ', ' * *  ', '***** ']

if N != 3:
    for k in range(int(math.log(N//3, 2))):
        add_current_triangle_twice()
        half_rshift_triange(k)

print_triangle()
