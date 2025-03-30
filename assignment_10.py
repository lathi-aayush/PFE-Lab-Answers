# 10. Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are (1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).
import math

xs = []
ys = []

for i in range(0, 3):
    x = int(input(f"Enter Coordinate x{i+1} : "))
    xs.append(x)
    y = int(input(f"Enter Coordinate y{i+1} : "))
    ys.append(y)

# This is the code for calculation of the Length of the diagonal
# if xs[0] != xs[1] and ys[0] != ys[1]:
#     diag_ln = math.sqrt(math.pow(xs[1] - xs[0], 2) + math.pow(ys[1] - ys[0], 2))
#     print("Length of diagonal = ", diag_ln)

# This code condition valids only when correct coordinates of the rectangle is given ,so it cannot check whether the coordinates are of rectangle or not
if xs[0] == xs[1]:
    x = xs[2]
elif xs[0] == xs[2]:
    x = xs[1]
elif xs[1] == xs[2]:
    x = xs[0]

if ys[0] == ys[1]:
    y = ys[2]
elif ys[0] == ys[2]:
    y = ys[1]
elif ys[1] == ys[2]:
    y = ys[0]


print(f"The Unknown Coordinates are : (X, Y) = ({x}, {y})")
