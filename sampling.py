from sourcetext import histogram
from random import randint, choices


def rand_sample(hist):
    seed = randint(0, len(hist))
    keys = list(hist.keys())
    return keys[seed]


def get_probability(hist):
    lin = len(hist)
    probval = []
    probdist = []
    for key in hist:
        probval.append(key)
        probdist.append(hist[key]/lin)
    return choices(probval, probdist)


if __name__ == "__main__":
    hi = histogram("One fish two fish red fish blue fish")
    print(get_probability(hi))
