from gensim.models import Word2Vec
from reynir import Reynir
import ice_lemma_extraction as extract
import regex as re
import glob


# Yields all nouns in every sentences
# Format: [file[sent[nouns]]]
def get_nouns():
    for file in all_files:
        nouns = []
        sents = reynir.parse(file)
        for sent in sents['sentences']:
            try:
                nouns.append(sent.tree.nouns)
            except AttributeError:
                pass
        yield nouns


if __name__ == '__main__':
    all_lemmas_per_text = []
    # For parsing sentences
    reynir = Reynir()
    # All files in dir
    all_files = glob.glob('doc2vec/txts/*txt')
    # All files sorted naturally
    sorted_files = extract.natural_sort(all_files)
    # List created from generator
    all_files = [w for w in extract.read_files()]
    # All lemmas
    # Structure: [file[sent[lemmas]]]
    all_nouns = [l for l in get_nouns()]
    # All lemmas
    # Structure = [file1[lemma1, lemma2], file2[lemma1, lemma2]]
    all_nouns_per_text = [w for w in extract.flatten(all_nouns)]
    # Writes all lemmas til files (ending: .lmms) with space as separator
    extract.write_to_file(all_nouns_per_text, 'nns',', ')
