import sys
from random import randint as ri


def run_dictionary():
    sentence = []
    if len(sys.argv) < 2:
        print("Please input the number of words you want.")
        return
    else:
        numwords = int(sys.argv[1])
        with open("/usr/share/dict/words", "r") as f:
            words = f.readlines()
            le = len(words)
            for i in range(0, numwords):
                sentence.append(words[ri(0, le)].replace("\n", ""))
            return sentence


if __name__ == "__main__":
    li = run_dictionary()
    str = " "
    print(str.join(li))
