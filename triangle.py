import math


def is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return True when the side lengths form a valid triangle."""
    if any(side <= 0 for side in (a, b, c)):
        return False
    return a + b > c and a + c > b and b + c > a


def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a triangle, returning 'Invalid' for impossible triangles."""
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    sides = sorted((a, b, c))

    if (
        math.isclose(sides[0], sides[1], rel_tol=1e-9, abs_tol=1e-9)
        and math.isclose(sides[1], sides[2], rel_tol=1e-9, abs_tol=1e-9)
    ):
        kind = "Equilateral"
    elif (
        math.isclose(sides[0], sides[1], rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(sides[1], sides[2], rel_tol=1e-9, abs_tol=1e-9)
        or math.isclose(sides[0], sides[2], rel_tol=1e-9, abs_tol=1e-9)
    ):
        kind = "Isosceles"
    else:
        kind = "Scalene"

    if math.isclose(
        sides[2] ** 2,
        sides[0] ** 2 + sides[1] ** 2,
        rel_tol=1e-9,
        abs_tol=1e-9,
    ):
        return f"Right {kind}"

    return kind
