import collections, sys

counter = collections.Counter()

for line in sys.stdin:
    line = line.strip()
    for character in line:
        if character.isspace():
            continue
        counter[character] += 1


for character, count in sorted(counter.items()):
    # print(item)
    print(f"{character} occured {count} times")
# print(counter)
