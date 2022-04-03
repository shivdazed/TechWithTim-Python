import collections
from collections import Counter

a = Counter("gallad")
print("String input:", a, "\n")

b = Counter(['a', 'a', 'b', 'c', 'c'])
print("List input:", b, "\n")

c = Counter({'a': 1, 'b': 2})
print("Dictionary input:", c, "\n")

d = Counter(cats=4, dogs=7)
print("Keyword input:", d, "\n")

#refernce of a particular item
print("references of cats in d:", d['cats'], "\n")

#useful methods that can be used on Counter object
# listing all elements in Counter object
print("Listing all elements in d with cats and dogs", list(d.elements()), "\n")
#most common element in counter object
e = Counter(['a', 'a', 'b', 'b', 'c', 'c'])
print("Most common elements:", e.most_common(2), "\n")

#adding and subtracting counter objects from non-counter objects
#list,sets, dictionaries, tuples

f = Counter(a=4, b=2, c=0, d=-2)
g = ['a', 'b', 'c', 'd']

f.subtract(g)
print("Subtracting g list from f counter object:", f, "\n")
f.update(g)
print("Adding g list to f counter object:", f, "\n")

#clearing counter object
f.clear()
print("Entries in f after clearing:", f, "\n")

#Useful operations that can be performed on counter objects
#adding and subtracting counter objects with one another
h = Counter(a=4, b=2, c=0, d=-2)
i = Counter(['a', 'b', 'c', 'd'])

print("Adding h and i:", h+i, "\n")
print("Subtracting i from h:", h-i, "\n")

#union and intersection
print("Intersection of h and i:", h & i, "\n")
print("Union of h and i", h | i, "\n")





