from math import *
from decimal import Decimal


def triangle(triangle):
    side_a, side_b, side_c = Decimal(
        input('a: ')), Decimal(input('b: ')), Decimal(input('c: '))
    p = (side_a + side_b + side_c) / 2
    s = sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    print(f'Area : {s}')


def square(square):
    width, height = Decimal(input('width: ')), Decimal(input('height: '))
    print(f'Area: {width * height}')


def circle(circle):
    r = int(input('radius: '))
    print(f'Area: {Decimal(pi)*2*r}')


body_type = input('Enter shape type: ')
if body_type == 'triangle':
    triangle(triangle)
elif body_type == 'square':
    square(square)
elif body_type == 'circle':
    circle(circle)
