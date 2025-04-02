import sys


n_lines = 10
if len(sys.argv) > 1:
    # process n
    if sys.argv[1][0] == '-':
        # good
        try:
            n_lines = int(sys.argv[1][1:])
        except ValueError as e:
            sys.exit(1)
            pass
    else:
        print("error")
        sys.exit(1)

# print(n_lines)
# input()

# i = 0
for i, line in enumerate(sys.stdin):
    if i == n_lines:
        break
    line = line.strip()
    # i += 1
    print(line)
