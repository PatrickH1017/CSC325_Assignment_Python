# Triangle classifier

This project implements a triangle classifier that checks whether three side lengths form a valid triangle and returns the correct classification.

## Run the tests

1. Install dependencies:
   `py -m pip install -r requirements.txt`
2. Run the tests:
   `py -m pytest -q`

## Copilot Review Log

| Test | Copilot-suggested? | Kept / edited / rejected |
| --- | --- | --- |
| `test_right_isosceles_triangle_uses_tolerance_for_floats` | Yes | Edited: Copilot suggested `==` for the right-triangle check, which fails for floating-point comparisons; it was changed to `math.isclose()` to allow tolerance. |
| `test_scalene_triangle` | Yes | Kept: the generated case was valid and matched the intended classification. |
| `test_invalid_when_triangle_is_degenerate` | Yes | Kept: the suggestion correctly recognized that a triangle with sides `(1, 2, 3)` is not valid because the sum of two sides equals the third. |

An equilateral triangle can never also be right because a right triangle must satisfy `c^2 = a^2 + b^2`, but for an equilateral triangle with equal sides `a = b = c`, that equation becomes `a^2 = a^2 + a^2`, which is impossible for any positive length.

## Acceptance criteria

1. For every input triple of positive side lengths, the function must return either a valid triangle classification or `Invalid` and must not crash.
2. A triangle is valid only if the sum of any two side lengths exceeds the third side; values that are zero, negative, or degenerate are treated as `Invalid`.
3. A right triangle is reported with a leading `Right ` prefix, using a tolerance-based comparison rather than exact equality.

These criteria are checked in `test_acceptance.py`.
