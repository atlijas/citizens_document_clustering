from gensim.models import Word2Vec
from difflib import get_close_matches

# W2V model containing inflected word forms
words_model = Word2Vec.load('path/to/model')
# List of all inflected word forms
words = words_model.wv.index2entity
# All words ranked by how often they appear
word_freq = {k:v for (v,k) in enumerate(words)}


def word_prob(word):
    return word_freq.get(word, len(words) - 1)


def get_suggestions(text):
    for word in text.split():
        if word_prob(word) > 70_000:
            suggestions = get_close_matches(word, word_freq, cutoff = 0.7)
            for suggestion in suggestions:
                if word_prob(suggestion) < 200_000:
                    yield suggestion


# If Word2Vec is properly trained it should return something close to
# ['maðurinn', 'Miklabraut', 'Melabraut', 'Miklabrautin']

print([w for w in get_suggestions('ég er maðurin á Milkabraut')])
