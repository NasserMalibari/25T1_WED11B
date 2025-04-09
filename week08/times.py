
import sys
# TODO ARG Checking

try:
    numRows = int(sys.argv[1])
    numCols = int(sys.argv[2])
    width = int(sys.argv[3])
except Exception as e:
    pass
    print("a nice usage messsage")
    sys.exit(1)

for i in range(1, numRows + 1):
    for j in range(1, numCols + 1):
        print(f"{i * j:>{width}}", end='')
    print()
# print(numCols)
