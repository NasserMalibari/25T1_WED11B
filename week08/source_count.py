
import os
import glob

total = 0
for file in glob.glob('*.[ch]'):
    # print the numbers
    with open(file) as f:
        num_lines = len(f.readlines())
        total += num_lines
        print(f"{num_lines} {file}")
    # print(file)
print(f"total {total}")
# '.*[ch]$'
os.listdir