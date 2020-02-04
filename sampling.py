from sourcetext import histogram
from random import randint, uniform


def rand_sample(hist):
    seed = randint(0, len(hist))
    keys = list(hist.keys())
    return keys[seed]


def choice(probval, probdist):
    r = uniform(0, 1)
    s = 0
    for i in range(0, len(probdist)):
        s += probdist[i]
        if s >= r:
            return probval[i]
    return probval


def get_probability(hist):
    lin = 0
    for key in hist:
        lin += hist[key]
    probval = []
    probdist = []
    for key in hist:
        probval.append(key)
        probdist.append(hist[key]/lin)
    return choice(probval, probdist)


if __name__ == "__main__":
    hi = histogram("One fish two fish red fish blue fish")
    print(get_probability(hi))
