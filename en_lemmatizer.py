from spacy import load
from argparse import ArgumentParser
parser = ArgumentParser()
english = load('en_core_web_sm')

parser.add_argument('-f', '--file')
args = parser.parse_args()


def file_to_string():
    with open(args.file, 'r', encoding = 'utf-8') as file:
        file = file.read()
        return file


def lemmatize(sent):
    words = english(sent)
    for token in words:
        if token.lemma_ == '-PRON-':
            yield token
        else:
            yield token.lemma_


if __name__ == '__main__':
    print('File:', args.file)
    sent = [str(l) for l in lemmatize(file_to_string())]
    print('Lemmas:', '\n', ' '.join(sent))
