from gensim.models.doc2vec import Doc2Vec
from random import sample
from shutil import get_terminal_size
import glob
import os
import regex as re

all_files = glob.glob('posts/*lmms')
model = Doc2Vec.load('lemmas_bin.model')

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)


all_files = natural_sort(all_files)


# Yields a generator of files
def get_files():
    for file in all_files:
        with open(file, 'r', encoding = 'utf-8') as t:
            text = t.read()
            if len(text.split()) > 70:
                yield file


all_files = [w for w in get_files()]



# This prints _ of equal length to your terminal size
# Works as a separator between printed files
term_line = '_' * (get_terminal_size().columns)


# Picks a random file and prints the n_files that are most similar to it
def print_similar(n_files):
    test_file = sample(all_files, 1)[0]
    most_similar = (model.docvecs.most_similar([test_file], topn = n_files))
    print('\n')
    print(test_file)
    os.system(f'cat {test_file[:-4]+"txt"}')
    for file,l in most_similar:
        os.system(f'cat {file[:-4]+"txt"}')
        print('\n', term_line)


print_similar(10)
