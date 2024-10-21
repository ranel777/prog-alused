def sum_and_difference(num_a: int, num_b: int) -> tuple:
    """Return the sum and difference of given variables num_a and num_b."""
    sum = num_a + num_b
    difference = num_a - num_b
    return sum, difference

print(sum_and_difference(5,2))
print(sum_and_difference(7,3))

def float_division(num_a: int, num_b: int) -> float:
    """Divide given variables num_a and num_b and return the result."""
    division = num_a / num_b
    return division
print(float_division(4,4))

def integer_division(num_a: int, num_b: int) -> int:
    """Divide given variables num_a and num_b and return the result rounded down."""
    division = num_a / num_b
    return division
print(integer_division(8,8))

def powerful_operations(num_a: int, num_b: int) -> tuple:
    """Return the product of given variables, num_a to the power of num_b and the remainder of division of variables."""
    multiply_numbers = num_a * num_b
    power = num_a ** num_b
    remainder = num_a / num_b
    return multiply_numbers, power, remainder
print(powerful_operations(8,4))

def find_average(num_a: int, num_b: int) -> float:
    """Return the average of given variables."""
    average = (num_a * num_b) / 2 
    return average
print(find_average(8,6))

import math

def area_of_a_circle(radius: float) -> float:
    """Calculate and return the area of a circle."""
    circle_area = math.pi * (radius ** 2)
    return circle_area
print(area_of_a_circle(9))

import math

def area_of_an_equilateral_triangle(side_length: float) -> int:
    """Calculate and return the area of an equilateral triangle."""
    triangle_area = round((math_sqrt(3) * side_length ** 2) / 4)
    return triangle_area
print(area_of_an_equilateral_triangle)

def calculate_discriminant(a: int, b: int, c: int) -> int:
    """Calculate discriminant with given variables and return the result."""
    discriminant = (b ** 2) - (4 * a * c)
    return discriminant
print(calculate_discriminant(5,5,8))

def calculate_hypotenuse_length(a: int, b: int) -> float:
    """Return the length of hypotenuse when the lengths of the catheti are given."""
    c = a**2 + b**2
    return c
print(calculate_hypotenuse_length(5,5))

def calculate_cathetus_length(a: int, c: int) -> float:
    """Return the length of cathetus when the lengths of the second cathetus and hypotenuse are given."""
    b = c * a
    return b
print(calculate_cathetus_length(5,9))