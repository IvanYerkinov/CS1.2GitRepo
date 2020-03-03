from dictogram import Dictogram


class MarkovChain:

    def __init__(self, word_list):

        # The Markov chain will be a dictionary of dictionaries
        # Example: for "one fish two fish red fish blue fish"
        # {"one": {fish:1}, "fish": {"two":1, "red":1, "blue":1}, "two": {"fish":1}, "red": {"fish":1}, "blue": {"fish:1"}}
        self.markov_chain = self.build_markov_queue(word_list)
        self.first_word = list(self.markov_chain.keys())[0]

    def build_markov(self, word_list):
        markov_chain = {}

        for i in range(len(word_list) - 1):
            # get the current word and the word after
            current_word = word_list[i]
            next_word = word_list[i+1]

            if current_word in markov_chain.keys(): #already there
                # get the histogram for that word in the chain
                histogram = markov_chain[current_word]
                # add to count
                histogram.dictionary_histogram[next_word] = histogram.dictionary_histogram.get(next_word, 0) + 1
            else: # first entry
                markov_chain[current_word] = Dictogram([next_word])

        return markov_chain

    def build_markov_queue(self, word_list):
        markov_chain = {}
        curr_q = []
        nex_q = []

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

    def walk(self, num_words):
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
                return " ".join(sentence)

        return " ".join(sentence)
        pass

    def print_chain(self):
        for word, histogram in self.markov_chain.items():
            print(word, histogram.dictionary_histogram)



markov_chain = MarkovChain(["one", "fish", "two", "fish", "red", "fish", "blue", "fish"])
markov_chain.print_chain()
print(markov_chain.walk(10))
