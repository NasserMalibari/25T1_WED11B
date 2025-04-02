#!/usr/bin/env python3


# Looping over a collection 

colors = ['red', 'green', 'blue', 'yellow']

n = len(colors)
# for i in range(n):
    # print(colors[i])

# for color in colors:
    # print(color)


# ####################


# Looping backwards

colors = ['red', 'green', 'blue', 'yellow']

# Looping with index
n = len(colors)
# for i in range(n -1 , -1, -1):
    # print(colors[i])

# for color in reversed(colors):
    # print(color)
#######################

colors = ['red', 'green', 'blue', 'yellow']

# for i, thing in enumerate(colors):
#     print(i, thing)


names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# n = min(len(names), len(colors))
# for i in range(n):
#     print (names[i], '--->', colors[i])

# for i,j in zip(names,colors):
#     print(f"{i} --> {j}")


colors = ['red', 'green', 'blue', 'yellow']

# # Forward sorted order
# for color in sorted(colors):
    # print(color)


# # Backwards sorted order
# for color in sorted(colors, reverse=True):
    # print(color)

# # Multiple exit points in a loop

def find(seq, target):

    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

    # found = False
    # for i, value in enumerate(seq):
    #     if value == target:
    #         found = True
    #         break
    # if not found:
    #     return -1
    # return i

# list1 = [1, 3, 5]
# target = 3
# print(find(list1, target))

# if 2 == 2:
    # a = 1
# print(a)


# ###### DICTIONARIES ##############################

d = {'a': 1, 'b': 2, 'c': 3}
d['d'] = 400
# a = (1,2)
# loop through keys


# for key in d:
    # print(key, d[key])

# loop through item (pairs)
# for key, value in d.items():
#     print(key, value)



# # construct from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

pair_dic = dict(zip(names, colors))

# # COUNTING WITH DICTIONARIES

my_list = ['a', 'b', 'c', 'a', 'c', 'a']
# {'a': 3, 'b': 1, 'c': 2}

count = {}
for letter in my_list:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print(count)
    # count[letter] = count.get(letter, 0) + 1



# from collections import default_dict, Counter
# counter = Counter(my_list)