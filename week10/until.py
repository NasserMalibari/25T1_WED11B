import re, sys


def address_matches(line_no, line, address):
    """ Returns True/False """

    # if address is number
    if re.fullmatch(r"[0-9]+", address):
        address = int(address)
        return line_no == address
    pass
    # if address is regex:
    match_obj = re.search(r'/(.*)/', address)
    # print(match_obj.group(1))

    # invalid case: TODO

    regex_part = match_obj.group(1)
    if re.search(regex_part, line):
        return True
    return False

def main():
    for line_no, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        print(line)
        if address_matches(line_no, line, sys.argv[1]):
            sys.exit(0)
    # print(line)

    # if address_matches()
    # get address (argv) + processing
    # read lines
        # print line
        # if line matches address
        # quit

if __name__ == "__main__":
    main()
    