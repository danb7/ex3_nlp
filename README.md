# Grammar Engineering
Third Assignment in NLP course.

by: Daniel Bazar 314708181 & Lior Krengel 315850594

## Goal
Understand how Context-Free Grammars (CFGs) work, and how they can be used — sometimes comfortably, sometimes not so much — to describe natural language.

## Submission
All discussion and detailed information are in `ANSWERS.pdf`.

### Part 1 | Weights
* `grammar1` - grammar file for part 1, with comments that motivate our changes.
* `grammar1.gen` - 10 sentences generated via `grammar1`.

### Part 2 | Extending the Grammar
* `grammar2` - grammar file for part 2, with comments that motivate our changes.
* `grammar2.gen` - 20 sentences generated via `grammar2`.

### Part 3 | Tree Structures
* `part3.gen` - 5 sentences in tree format.

### Part 4 | Additional Linguistic Structures
we chosed on this part to extend our grammar with Relative clauses (c) and WH-word questions (d).
* `grammar4` - grammar file for part 4, handling phenomena (c) and (d), with comment that motivate our changes.

### Part 5 | Extra
In this part we extended our grammar in various interseting ways.
* `grammar5` - grammar file for part 5, with comments that motivate our changes.
* `generatex.py` - extended version of `generate.py` for supporting post-processing.

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
