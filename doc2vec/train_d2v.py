from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import regex as re
import glob
import os


all_files = glob.glob('path/to/lmms/files/*lmms')

# Reads multi-digit numbers in file names as a single number
# Also known as human sorting
# This is not a necessary step but is handy for keeping an
# overview of the files
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
            yield text


data = [w for w in get_files()]


# All filenames as a separate list for tagging with TaggedDocument
# Structure: [[file1], [file2]]
# (I honestly don't know why Doc2Vec only accepts this format as the input)
all_files = [all_files[i:i+1] for i in range(0, len(all_files))]


# Input for build_vocab
tagged_data = [TaggedDocument(words = word_tokenize(d.lower()),
               tags = all_files[i]) for i, d in enumerate(data)]


model = Doc2Vec(vector_size = 300,
                alpha = 0.025,
                min_alpha = 0.00025,
                min_count = 1,
                epochs = 100,
                dm = 0)

model.build_vocab(tagged_data)

model.train(tagged_data,
            total_examples = model.corpus_count,
            epochs = model.epochs)

model.save('name_of_model.model')
print('Model saved')
