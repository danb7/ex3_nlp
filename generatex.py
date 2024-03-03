"""
Usage:
    generate.py <grammer_file> [-n NUMBER] [-t] [-d]

Options:
    -n NUMBER  Number of sentences to generate [default: 1]
    -t  generate the tree structures that generates the sentences
    -d  debug. print also Pre-terminal along side each word
"""


from collections import defaultdict
import random
import re
from docopt import docopt

class PCFG(object):
    def __init__(self):
        self._rules = defaultdict(list)
        self._sums = defaultdict(float)

    def add_rule(self, lhs, rhs, weight):
        assert(isinstance(lhs, str))
        assert(isinstance(rhs, list))
        self._rules[lhs].append((rhs, weight))
        self._sums[lhs] += weight

    @classmethod
    def from_file(cls, filename):
        grammar = PCFG()
        with open(filename) as fh:
            for line in fh:
                line = line.split("#")[0].strip()
                if not line: continue
                w,l,r = line.split(None, 2)
                r = r.split()
                w = float(w)
                grammar.add_rule(l,r,w)
        return grammar

    def is_terminal(self, symbol): return symbol not in self._rules

    def gen(self, symbol, gen_tree=False, debug=False, father=None):
        if self.is_terminal(symbol): 
            if debug:
                return f'({father}, {symbol})'
            else:
                return symbol
        else:
            expansion = self.random_expansion(symbol)
            result = " ".join(self.gen(s,gen_tree, debug, symbol) for s in expansion)
            if gen_tree:
                result = f'({symbol} {result})'
            
            
            return result

    def random_sent(self, gen_tree=False, debug=False):
        '''
        we modify this function.

        now the generated sentence from the original function serve as an internal version of the sentence.
        then we run it through a post-processor for external representation.

        we run the sentence through post-processor just if we pass default (or -n) parameters.
        if we want the tree (-t) or debug (-d) we generate the basic sentence without post-process.
        '''
        if not(gen_tree or debug):
            internal_s = self.gen("ROOT", gen_tree, debug)
            return self.post_process(internal_s)
        else:
            return self.gen("ROOT", gen_tree, debug)
        
    def post_process(self, sentence):
        '''
        NEW!
        post processor for basic sentences.
        steps:
        1. "a" vs "an"
        2. capitalization
        3. handling unnecessaries commas and whitespaces (consequence of appositives)
        '''
        processed_sentence = sentence

        # replace "a" to "an" if start with vowels
        processed_sentence = re.sub(r'\ba(?=\s+[aeiou])', 'an', processed_sentence)

        # Capitalization
        capital_index = next((i for i, char in enumerate(sentence) if char.isalpha()), -1)
        if capital_index>-1:
            processed_sentence = processed_sentence[:capital_index] + processed_sentence[capital_index].upper() + processed_sentence[capital_index + 1:]

        # remove duplicates commas
        processed_sentence = re.sub(r'(, )+', ', ', processed_sentence)
        # remove unnecessary commas (at end of sentence or before that) [consequence of naive appositive]
        processed_sentence = re.sub(r',(?= [!?.])', '', processed_sentence)
        processed_sentence = re.sub(r', that', 'that', processed_sentence)
        # remove leading withspaces in quotes
        processed_sentence = f'"{processed_sentence[1:].strip()}' if processed_sentence.startswith('"') else processed_sentence.strip()
        # remove leading and trailing withspaces for period
        processed_sentence = re.sub(r' \.\s*', '.', processed_sentence)
        # remove whitespaces at end of sentence
        processed_sentence = re.sub(r'\s+(?=[!?.])', '', processed_sentence)
        # remove whitespaces before comma
        processed_sentence = re.sub(r' ,', ',', processed_sentence)

        return processed_sentence

    def random_expansion(self, symbol):
        """
        Generates a random RHS for symbol, in proportion to the weights.
        """
        p = random.random() * self._sums[symbol]
        for r,w in self._rules[symbol]:
            p = p - w
            if p < 0: return r
        return r


if __name__ == '__main__':

    import sys
    args = docopt(__doc__)
    # args = {'<grammer_file>': 'grammar2', '-n': 3, '-t': True, '-d': False}
    pcfg = PCFG.from_file(args['<grammer_file>'])
    num_of_sentences = int(args['-n'])
    gen_tree = args['-t']
    debug = args['-d']
    sentences = '\n'.join(pcfg.random_sent(gen_tree, debug) for i in range(num_of_sentences))
    print(sentences)
