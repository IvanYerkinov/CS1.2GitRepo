import sys


def histogram(longstring):
    string = longstring.split(" ")
    di = dict()

    for st in string:
        if st in di:
            di[st] += 1
        else:
            di[st] = 1

    return di


def unique_words(hist):
    i = 0
    for key in hist:
        if hist[key] == 1:
            i += 1
    return i


def frequency(hist, word):
    return hist[word]


def get_file(filename):
    with open(filename, 'r') as f:
        data = f.read().replace("\n", "")
    return data


if __name__ == "__main__":
    his = histogram(get_file(sys.argv[1]))
    print(unique_words(his))
    print(frequency(his, "and"))
