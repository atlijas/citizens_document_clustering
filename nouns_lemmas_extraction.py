from gensim.models import Word2Vec
from reynir import Reynir
import regex as re
import glob
import time


# Reads multi-digit numbers in file names as a single number
# Also known as human sorting
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)


# Creates a generator of all files
# Ignores the standard beginning line of files ('Name: Blabla')
def read_files(file):
    for file in sorted_files:
        with open(file, 'r', encoding = 'utf-8') as f:
            for line in f:
                if line.startswith('Name'):
                    pass
                elif line == '\n':
                    pass
                else:
                    yield line


# For parsing sentences
reynir = Reynir()

# All files in dir
all_files = glob.glob('path/to/text/files/*txt')

# All files sorted naturally
sorted_files = natural_sort(all_files)

# List created from generator
all_files = [w for w in read_files()]


# Yields all nouns in every sentences
# Format: [file[sent[nouns]]]
def get_nouns():
    for file in all_files:
        nouns = []
        try:
            sents = reynir.parse(file)
            for sent in sents['sentences']:
                nouns.append(sent.tree.nouns)
        except AttributeError:
            pass
        yield nouns


# Yields all lemmas in every sentences
# Structure: [file[sent[lemmas]]]
def get_lemmas():
    for file in all_files:
        lemmas = []
        try:
            sents = reynir.parse(file)
            for sent in sents['sentences']:
                lemmas.append(sent.tree.lemmas)
        except AttributeError:
            pass
        yield lemmas


all_nouns = [l for l in get_nouns()]
all_lemmas = [l for l in get_lemmas()]


# Flattens structure to [file[lemmas]]
def flatten(lst):
    for sents in lst:
        extr = [e for sent in sents for e in sent]
        yield extr


all_nouns_per_text = [w for w in flatten(all_nouns)]
all_lemmas_per_text = [w for w in flatten(all_lemmas)]


# Write nouns/lemmas to file
# Changes file endings from .txt to .nns (nouns) | .lmms (lemmas)
def write_to_file(lst, ending, separator):
    for (i, l) in enumerate(lst):
        with open(sorted_files[i][:-3]+ending, 'w', encoding = 'utf-8') as file:
            if lst == all_nouns_per_text:
                file.write(separator.join(set(l)))
            else:
                file.write(separator.join(l))


# write_to_file(all_nouns_per_text, 'nns', ', ')
# write_to_file(all_lemmas_per_text, 'lmms',' ')
