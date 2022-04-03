import collections
from collections import namedtuple

Point = namedtuple('Point', 'x y z')

newP = Point(3, 4, 5)
print(newP)
print(newP.x, newP.y, newP.z)
#outputs parameter and variable values in tuple as a dictionary
print(newP._asdict())
#outputs argument variables passed while creation of point object
print(newP._fields)

#replaces a particular argument value
newP = newP._replace(x=6)
print(newP)
#changes the argumnet values of x, y and z
p2 = Point._make(['a', 'b', 'c'])
print(p2)