#!/usr/bin/env python3

import subprocess, re

# subprocess.run(["wget", "-O-", "-q"])
proc = subprocess.run("wget -q -O- 'https://www.unsw.edu.au'", shell=True, capture_output=True, text=True)
lines = proc.stdout
# print(lines)

numbers = re.findall(r"[0-9 -]+", lines)
# remove hyphens and spaces
numbers = [re.sub(r'[- ]', '', number) for number in numbers]
# print(numbers)
# numbers = []
for number in numbers:
    if len(number) >= 8 and len(number) <= 15:
        # print(number)
        pass

# output_nums = set()
nums = [number for number in numbers if len(number) <= 15 and len(number) >= 8]
for num in nums:
    print(num)
