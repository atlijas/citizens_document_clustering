from gensim.models import Word2Vec

# W2V model containing inflected word forms
words_model = Word2Vec.load('/path_to_w2v_model.model')
# List of all inflected word forms
words = words_model.wv.index2entity
# All words ranked by how often they appear
ranked_words = {k:v for (v,k) in enumerate(words)}


# Checks whether a word word has been split in two
# A common spelling mistake in Icelandic
def check_splits(text):
    text = text.split()
    for word in range(len(text)):
        try:
            if text[word]+text[word+1] in ranked_words.keys():
                print(text[word]+text[word+1])
        except IndexError:
            pass


# If Word2Vec model is properly trained this should print "smávægilegt"
check_splits('smá vægilegt')
