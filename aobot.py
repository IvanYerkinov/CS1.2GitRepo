import sys
from dictogram import Dictogram
from random import randint


class MarkovChain:

    def __init__(self, filename):

        # The Markov chain will be a dictionary of dictionaries
        # Example: for "one fish two fish red fish blue fish"
        # {"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.firstword_list = []
        self.markov_chain = self.build_markov(self.readFile(filename))
        self.first_word = self.firstword_list[randint(0, len(self.firstword_list) - 1)]
        # self.firstword_list[randint(0, len(self.firstword_list) - 1)]
        # list(self.markov_chain.keys())[randint(0, len(self.markov_chain.keys()))]

    def readFile(self, filename):
        wordlist = []
        with open(filename, "r") as f:
            for line in f:
                if line == "\n":
                    pass
                else:
                    wordlist.append(line.strip().split())
        return wordlist

    def build_markov(self, word_master):
        markov_chain = {}

        for word_list in word_master:

            if word_list[0] not in self.firstword_list:
                self.firstword_list.append(word_list[0])

            for i in range(len(word_list) - 1):
                # get the current word and the word after
                current_word = word_list[i]
                next_word = word_list[i+1]

                if current_word in markov_chain.keys(): #already there
                    # get the histogram for that word in the chain
                    histogram = markov_chain[current_word]
                    # add to count
                    histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
                else:  # first entry
                    markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def walk(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = []
        chain = self.markov_chain
        newword = self.first_word
        sentence.append(newword)
        # newword = chain[self.first_word].sample()
        # newword = "".join(newword)
        for i in range(num_words):
            if newword in chain:
                newword = chain[newword].sample()
                newword = "".join(newword)
                sentence.append(newword)
            else:
                newword = list(self.markov_chain.keys())[randint(0, len(self.markov_chain.keys()) - 1)]
                i = i - 1

        return " ".join(sentence)
        pass

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)


if __name__ == "__main__":
    bot = MarkovChain(sys.argv[1])
    print(bot.walk(randint(10, 30)))
