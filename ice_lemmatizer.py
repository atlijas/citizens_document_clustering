from gensim.models import Word2Vec
from reynir import Reynir
import regex as re
import glob


# Reads multi-digit numbers in file names as a single number
# Also known as human sorting
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)




# Creates a generator of all files
# Ignores the standard beginning line of files ('Name: Blabla')
def read_files():
    for file in sorted_files:
        with open(file, 'r', encoding = 'utf-8') as f:
            for line in f:
                if line.startswith('Name'):
                    pass
                elif line == '\n':
                    pass
                else:
                    txt = f.read().replace('\n', '')
                    yield txt


# For parsing sentences
reynir = Reynir()
# All files in dir
all_files = glob.glob('doc2vec/txts/*txt')
# All files sorted naturally
sorted_files = natural_sort(all_files)
# List created from generator
all_files = [w for w in read_files()]

# Yields all lemmas in every sentences
# Structure: [file[sent[lemmas]]]
def get_lemmas():
    for file in all_files:
        lemmas = []
        sents = reynir.parse(file)
        for sent in sents['sentences']:
            try:
                lemmas.append(sent.tree.lemmas)
            except AttributeError:
                pass
        yield lemmas

# Flattens list to [file1[lemma1, lemma2], file2[lemma1, lemma2]]
def flatten(lst):
    for sents in lst:
        extr = [e for sent in sents for e in sent]
        yield extr


def write_to_file(lst, ending, separator):
    for (i, l) in enumerate(lst):
        with open(sorted_files[i][:-3]+ending, 'w', encoding = 'utf-8') as file:
            file.write(separator.join(l))



if __name__ == '__main__':
    # All lemmas
    # Structure: [file[sent[lemmas]]]
    all_lemmas = [l for l in get_lemmas()]
    # All lemmas
    # Structure = [file1[lemma1, lemma2], file2[lemma1, lemma2]]
    all_lemmas_per_text = [w for w in flatten(all_lemmas)]
    # Writes all lemmas til files (ending: .lmms) with space as separator
    write_to_file(all_lemmas_per_text, 'lmms',' ')
