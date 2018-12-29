class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord


a = Point(-1, 1)
b = Point(3, 3)
a=b
a.x = 1

print(a.x, a.y, b.x, b.y)


# a stores the values x = -1 and y = 1
# b stores the values x = 3 and y = 3
# a = b so now a and b both refer to x = 3 and y = 3
# a.x = 1 changes a and b to: x = 1 and y = 3
# It prints 1 3 1 3
