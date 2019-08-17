from spacy import load
language = load('language_pack')

# Available languages (need to be downloaded):
# Language: download (language_pack to load is the last variable, e.g. en_core_web_sm)
# English: python -m spacy download en_core_web_sm
# German: python -m spacy download de_core_news_sm
# French: python -m spacy download fr_core_news_sm
# Spanish: python -m spacy download es_core_news_sm
# Portuguese: python -m spacy download pt_core_news_sm
# Italian: python -m spacy download it_core_news_sm
# Dutch: python -m spacy download nl_core_news_sm
# Greek: python -m spacy download el_core_news_sm


def file_to_string(file):
    with open(file, 'r', encoding = 'utf-8') as file:
        file = file.read()
        return file


def lemmatize(sent):
    words = language(sent)
    for token in words:
        if token.lemma_ == '-PRON-':
            yield token
        else:
            yield token.lemma_


if __name__ == '__main__':
    sent = [str(l) for l in lemmatize(file_to_string('file_to_lemmatize'))]
    # print('Lemmas:', '\n', ' '.join(sent))
