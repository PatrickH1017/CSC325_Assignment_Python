import math

from triangle import classify_triangle


def test_customer_examples():
    # A zero side is not allowed.
    assert classify_triangle(0, 3, 4) == "Invalid"

    # These positive side lengths fail the triangle rule:
    # the two shorter sides must add up to more than the longest side.
    assert classify_triangle(2, 3, 5) == "Invalid"

    # The 3-4-5 triangle is a right triangle with three different sides.
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    # This is an isosceles right triangle.
    hypotenuse = 5 * math.sqrt(2)
    assert classify_triangle(5, 5, hypotenuse) == "Right Isosceles"

    # Equal sides make an equilateral triangle, which is not right.
    assert classify_triangle(5, 5, 5) == "Equilateral"
