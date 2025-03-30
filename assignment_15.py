# 15. Program to find the roots of a quadratic equation
import math

print("The Quadratic Equation is of the Format : ax^2 + bx + c")

# (don't give comma, just write by giving space)
a, b, c = map(int, input("Enter the co-efficient of x^2, x, & constant : ").split())

# to check if the roots are imaginary or not
d = ((b * b) - (4 * a * c))
if d >= 0:
    D = math.sqrt(d)
    x1 = (-b + D) / 2 * a
    x2 = (-b - D) / 2 * a
    print(f"The Roots of the Equation {a}x^2 + {b}x + {c} are {x1}, {x2}")
else:
    print(f"The Equation {a}x^2 + {b}x + {c} has Imaginary roots")
