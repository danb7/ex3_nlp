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
                return symbol
            else:
                return f'({father}, {symbol})'
        else:
            expansion = self.random_expansion(symbol)
            result = " ".join(self.gen(s,gen_tree, debug, symbol) for s in expansion)
            if gen_tree:
                result = f'({symbol} {result})'
            
            
            return result

    def random_sent(self, gen_tree=False, debug=False):
        return self.gen("ROOT", gen_tree, debug=False)

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
    # args = {'<grammer_file>': 'grammar2', '-n': 3, '-t': True}
    pcfg = PCFG.from_file(args['<grammer_file>'])
    num_of_sentences = int(args['-n'])
    gen_tree = args['-t']
    debug = args['-d']
    sentences = '\n'.join(pcfg.random_sent(gen_tree, debug) for i in range(num_of_sentences))
    print(sentences)
