import sys
from random import randint as ri


def run_dictionary(num):
    sentence = []
    numwords = num
    with open("/usr/share/dict/words", "r") as f:
        words = f.readlines()
        le = len(words)
        for i in range(0, numwords):
            sentence.append(words[ri(0, le)].replace("\n", ""))
        return sentence


if __name__ == "__main__":
    li = run_dictionary(int(sys.argv[1]))
    str = " "
    print(str.join(li))
