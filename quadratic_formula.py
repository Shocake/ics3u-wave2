import math
a = float(input("What is the value of a?"))
b = float(input("What is the value of b?"))
c = float(input("what is the value of b?"))

disc = (b * b) - (4 * a * c)
roots = 1
if disc > 0:
    discriminantroot = math.sqrt((b * b) - (4 * a * c))
    root1 = str((-1 * b + discriminantroot) / (2 * a))
    root2 = str((-1 * b - discriminantroot) / (2 * a))
    roots == 2
    print("# of roots = 2, value of roots are " + root1 + " and " + root2)
elif disc == 0:
    discriminantroot = math.sqrt((b * b) - (4 * a * c))
    root1 = str((-1 * b + discriminantroot) / (2 * a))
    root2 = str((-1 * b - discriminantroot) / (2 * a))
    roots = 1
    print("# of real roots = 1, value of root is " + root1)
elif disc < 0:
    roots == 0
    print("# of real roots = 0")

