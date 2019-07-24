from gensim.models.doc2vec import Doc2Vec
from argparse import ArgumentParser
from shutil import get_terminal_size
from random import sample
import glob
import os

parser = ArgumentParser()
parser.add_argument('-f', '--file')
args = parser.parse_args()

model = Doc2Vec.load('model.model')

# This prints _ of equal length to your terminal size
# Works as a separator between printed files
term_line = '_' * (get_terminal_size().columns)

def infer_print_similar(n_files):
    with open(args.file, 'r', encoding = 'utf-8') as test:
        test = test.read().split()
    test_file = args.file
    test_vector = model.infer_vector(test)

    most_similar = (model.docvecs.most_similar([test_vector], topn = n_files))
    os.system(f'cat {test_file}')
    for file,l in most_similar:
        os.system(f'cat {file}')
        print('\n', term_line)

#infer_print_similar(5)
