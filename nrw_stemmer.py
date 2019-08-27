from nltk.stem import SnowballStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
import regex as re
import glob

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)


# Creates a generator of all files
# Ignores the standard beginning line of files ('Name: Blabla')
def read_files():
    for file in sorted_files:
        with open(file, 'r', encoding = 'utf-8') as f:
            txt = f.readlines()
            txt = ' '.join(txt).replace('\n', '')
            txt = sent_tokenize(txt)
            yield txt
            for line in f:
                if line.startswith('Name'):
                    pass
                #elif line == '\n':
                #    pass
                else:
                    txt = f.read().replace('\n', '')
                    yield line


# Yields all lemmas in every sentences
# Structure: [file[sent[lemmas]]]
def get_stems():
    for file in files_to_stem:
        all_stems = []
        for sent in file:
            sent = word_tokenize(sent)
            sent = ' '.join(sent)
            for word in sent.split():
                tokens = stemmer.stem(word)
                all_stems.append(tokens)
        yield all_stems


def write_to_file(lst, ending, separator):
    for (i, l) in enumerate(lst):
        with open(sorted_files[i][:-3]+ending, 'w', encoding = 'utf-8') as file:
            file.write(separator.join(l))


if __name__ == '__main__':
    stemmer = SnowballStemmer('norwegian')
    list_of_files = glob.glob('doc2vec/no/*txt')
    sorted_files = natural_sort(list_of_files)
    files_to_stem = [w for w in read_files()]
    all_stems = [w for w in get_stems()]
    write_to_file(all_stems, 'lmms', ' ')
