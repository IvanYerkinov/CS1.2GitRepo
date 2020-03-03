import sys
from dictogram import Dictogram
from random import randint


class MarkovChain:

    def __init__(self, filename, chain=1):

        # The Markov chain will be a dictionary of dictionaries
        # Example: for "one fish two fish red fish blue fish"
        # {"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.firstword_list = []
        self.markov_chain = self.start(filename, chain)
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

    def start(self, filename, chain):
        if chain == 1:
            return self.build_markov(self.readFile(filename))
        else:
            return self.build_markov_queue(self.readFile(filename))

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

    def build_markov_queue(self, word_master):
        markov_chain = {}
        curr_q = []
        nex_q = []

        for word_list in word_master:
            if len(word_list) > 1:
                first_q = (word_list[0], word_list[1])
                if first_q not in self.firstword_list:
                    self.firstword_list.append(first_q)

            for i in range(len(word_list) - 1):
                curr_q.append(word_list[i])
                nex_q.append(word_list[i + 1])

                if len(curr_q) == 2:
                    current_q = tuple(curr_q)
                    next_q = tuple(nex_q)
                    curr_q.pop(0)
                    nex_q.pop(0)

                    if current_q in markov_chain.keys():
                        histogram = markov_chain[current_q]
                        histogram.dictionary_histogram[next_q] = histogram.dictionary_histogram.get(next_q, 0) + 1
                    else:
                        markov_chain[current_q] = Dictogram([next_q])
        return markov_chain

    def walk(self, num_words, first_word=None):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = []
        chain = self.markov_chain
        if first_word is None:
            newword = self.first_word
        else:
            newword = first_word
        sentence.append(newword)
        # newword = chain[self.first_word].sample()
        # newword = "".join(newword)
        for i in range(num_words):
            if newword in chain:
                newword = chain[newword].sample()
                sentence.append(newword)
            else:
                newword = list(self.markov_chain.keys())[randint(0, len(self.markov_chain.keys()) - 1)]
                i = i - 1

        return " ".join(sentence)
        pass

    def walk_queue(self, num_words):
        # TODO: generate a sentence num_words long using the markov chain
        sentence = []
        chain = self.markov_chain
        newword = self.first_word
        sentence.append(newword[0])
        # newword = chain[self.first_word].sample()
        # newword = "".join(newword)
        for i in range(num_words):
            if newword in chain:
                newword = chain[newword].sample()
                sentence.append(newword[0])
            else:
                sentence.append(newword[1])
                # sentence.append("\n")
                newword = self.firstword_list[randint(0, len(self.firstword_list) - 1)]
                i = i - 1

        return " ".join(sentence)
        pass

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)

    def print_first_words(self):
        print(", ".join(self.firstword_list))

    def defined_walk(self, num_words, startstring):
        sentence = startstring.split(" ")
        first_word = sentence[-1]
        return " ".join(sentence[:-1]) + " " + self.walk(num_words, first_word)


if __name__ == "__main__":
    bot = MarkovChain(sys.argv[1])

    if(len(sys.argv) > 2):
        if(sys.argv[2] == "-fw"):
            bot.print_first_words()
        if sys.argv == "-c":
            bot.print_chain()
        if(sys.argv[2] == "-d" and len(sys.argv) > 3):
            print(bot.defined_walk(randint(10, 30), sys.argv[3]))
        if sys.argv[2] == "-q":
            bot = MarkovChain(sys.argv[1], 2)
            print(bot.walk_queue(randint(20, 50)))
    else:
        print(bot.walk(randint(10, 30)))
