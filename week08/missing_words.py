import sys

def collect_words_set(filename):
    """ 
    desc

    Args

    Outputs

    Example
    """
    with open(filename) as f:
        word_set = set()
        for line in f:
            line = line.strip()
            word_set.add(line)
    
    return word_set



# open file1 and store words
# print(collect_words_set(sys.argv[1]))

words1 = collect_words_set(sys.argv[1])
words2 = collect_words_set(sys.argv[2])

res = sorted(words1.difference(words2))
if not res:
    print("no output")

for word in sorted(res):
    print(word)

# open file2 and store words