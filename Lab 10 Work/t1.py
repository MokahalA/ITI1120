class Point:
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord


def riddle(x, p):
    x=x+7
    return x + p.x + p.y

x = 5
blank = Point(1, 2)
t =riddle(x, blank)
print(x, t, blank.x, blank.y)


# x = 5
# blank stores a value for x and y, x = 1 and y = 2
# riddle(5, blank) ~  12 + 1 + 2 == 15
# t = 15
# So the function prints 5 15 1 2

