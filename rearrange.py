import sys
from random import randint

words = sys.argv[1:]


def rearrange():
    le = len(words)
    for i in range(0, le):
        ind = randint(0, le - 1)
        temp = words[i]
        words[i] = words[ind]
        words[ind] = temp
    return words


if __name__ == "__main__":
    print(rearrange())
