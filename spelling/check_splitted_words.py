from gensim.models import Word2Vec
from reynir.bincompress import BIN_Compressed
bin = BIN_Compressed()


# W2V model containing inflected word forms
words_model = Word2Vec.load('path/to/model')
# List of all inflected word forms
words = words_model.wv.index2entity
# All words ranked by how often they appear
word_freq = {k:v for (v,k) in enumerate(words)}

#print(words_model.most_similar('apaköttur'))

# Checks whether a word word has been split in two
# A common spelling mistake in Icelandic
def check_splits(text):
    text = text.split()
    for word in range(len(text)):
        try:
            compound = text[word].lower()+text[word+1].lower()
            if compound in word_freq.keys() or bool(bin.lookup(compound)):
                return compound
        except IndexError:
            pass


# If Word2Vec model is properly trained this should print "smávægilegt"
print(check_splits('smá vægilegt'))
