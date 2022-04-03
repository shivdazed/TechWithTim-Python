import collections
from collections import deque

d = deque("Hello")
print(d)
# applying some methods
d.append('to be')
d.append(5)
print(d)

d.appendleft(3)
print(d)

# removing or popping elements
# removes last element
d.pop()
print(d)
# removes first element
d.popleft()
print(d)

# clearing of deque
d.clear()
print(d)

# adding elements at end or extending deque other than append
d.extend('456')
print(d)
d.extend('Hello')
print(d)
# extends to the left hence adds string in reverse order to deque
d.extendleft('hey')
print(d)

# manipulating elements at the start and end of deque using .rotate()
# -ve number passed as argument rotates to the left
d.rotate(-2)
print(d)
# +ve number passed as argument rotates to the right
d.rotate(3)
print(d)

# using maxlen to predefine maximum length of deque
c = deque('Hello', maxlen=5)
print(c)
# so if .append() is used when maxlen is defined when deque is created the new elements displace the old elements( here 'h' for append)to maintain the maxlen specified
c.append(7)
print(c)
