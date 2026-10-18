import math

from triangle import classify_triangle, is_valid_triangle


def test_side_of_length_zero_is_invalid():
    # A side must be longer than zero.
    assert is_valid_triangle(0, 3, 4) is False
    assert classify_triangle(0, 3, 4) == "Invalid"


def test_negative_side_is_invalid():
    # Negative lengths cannot describe real sides.
    assert classify_triangle(-1, 3, 4) == "Invalid"


def test_degenerate_triangle_is_invalid():
    # 1 + 2 is exactly 3, so these sides do not make a triangle.
    assert is_valid_triangle(1, 2, 3) is False
    assert classify_triangle(1, 2, 3) == "Invalid"


def test_equilateral_triangle():
    # All three sides are the same length.
    result = classify_triangle(5, 5, 5)
    assert result == "Equilateral"


def test_isosceles_triangle():
    # Exactly two sides are the same length.
    result = classify_triangle(3, 3, 4)
    assert result == "Isosceles"


def test_scalene_triangle():
    # All three sides have different lengths.
    result = classify_triangle(4, 5, 6)
    assert result == "Scalene"


def test_right_scalene_triangle():
    # 3 squared + 4 squared equals 5 squared.
    result = classify_triangle(3, 4, 5)
    assert result == "Right Scalene"


def test_right_isosceles_triangle_with_decimal_side():
    # The hypotenuse is 5 times the square root of 2 (about 7.07).
    hypotenuse = 5 * math.sqrt(2)
    result = classify_triangle(5, 5, hypotenuse)
    assert result == "Right Isosceles"
