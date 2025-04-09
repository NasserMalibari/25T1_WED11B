
a = [1, 4, 16, 24]
# a.map()
square = [x**2 for x in a]
# print(squares)

names = ["john", "jack", "joannah"]
# capitalizedNames = sorted([ name.capitalize() for name in names])
print(', '.join(sorted([ name.capitalize() for name in names])))

# print(capitalizedNames)

# dict comprehensions: Further reading


c = ['a', 'a', 'a', 'b', 'b', 'c']
import collections
my_counter = collections.Counter(c)
# print(my_counter)
# my_counter['d'] += 1
# print(my_counter)

# defaultdicts