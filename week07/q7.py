import sys

if len(sys.argv) == 1:
    sys.argv.append("-")

count = 1
for filename in sys.argv[1:]:
    try:
        if filename == "-":
            stream = sys.stdin
        else:
            stream = open(filename)

        for line_num, line in enumerate(stream, start=count):
            count += 1
            line = line.strip()
            print(f"{line_num:6} {line}")

        if stream != sys.stdin:
            stream.close()

    except IOError as e:
        print(f"{sys.argv[0]}: can not open: {e.filename}: {e.strerror}")



# with open(filename) as f:
#     for line in f:
#         pass