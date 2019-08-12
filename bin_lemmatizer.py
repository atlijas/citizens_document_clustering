from reynir.bincompress import BIN_Compressed
import glob
import regex as re
from nltk.tokenize import sent_tokenize, word_tokenize
bin = BIN_Compressed()


# Reads multi-digit numbers in file names as a single number
# Also known as human sorting
def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([p\D]+)', key)]
    return sorted(l, key=alphanum_key)


# All files in dir
all_files = glob.glob('path/to/txts/*txt')
# All file names sorted naturally
sorted_files = natural_sort(all_files)


# Creates a generator of all files
# Ignores the standard beginning line of files ('Name: Blabla')
def read_files():
    for file in sorted_files:
        with open(file, 'r', encoding = 'utf-8') as f:
            txt = f.readlines()
            txt = ' '.join(txt).replace('\n', ' ')
            txt = sent_tokenize(txt)
            txt = word_tokenize(' '.join(txt))
            yield txt
            for line in f:
                if line.startswith('Name'):
                    pass
                #elif line == '\n':
                #    pass
                else:
                    txt = f.read().replace('\n', ' ')
                    yield line


# List created from generator
all_files = [w for w in read_files()]


def get_lemmas():
    i = 1
    for file in all_files:
        lemmas = []
        print(f'File {i} of {len(sorted_files)}')
        for word in file:
            if bin.lookup(word) != []:
                try:
                    lemmas.append(bin.lookup(word)[0][0])
                except:
                    lemmas.append(bin.lookup(word.lower())[0][0])
            elif bin.lookup(word.lower()) != []:
                try:
                    lemmas.append(bin.lookup(word)[0][0])
                except:
                    lemmas.append(bin.lookup(word.lower())[0][0])

            elif bin.lookup(word) == []:
                lemmas.append(word)
        yield lemmas
        i += 1



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
    #all_lemmas_per_text = [w for w in flatten(all_lemmas)]
    # Writes all lemmas til files (ending: .lmms) with space as separator
    write_to_file(all_lemmas, 'lmms',' ')
