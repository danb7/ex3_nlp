# Grammar Engineering
Third Assignment in NLP course.

by: Daniel Bazar 314708181 & Lior Krengel 315850594

## Part 1 | Weights
* grammar1 - grammar file for part 1, with comment that motivate our changes.
* grammar1.gen - 10 sentences generated via grammar1.

## How to run

The file ``generate.py`` generate sentences based on our basic PCFG rules.  
The file ``generatex.py`` generate sentences after post process.

The files runs in the same way. they both get grammar to work on, and some additional aarguments as described below:  
### Usage
```
Usage:
    generate.py <grammer_file> [-n NUMBER] [-t] [-d]
    generatex.py <grammer_file> [-n NUMBER] [-t] [-d]

Options:
    -n NUMBER  Number of sentences to generate [default: 1]
    -t  generate the tree structures that generates the sentences
    -d  debug. print also Pre-terminal along side each word
```
