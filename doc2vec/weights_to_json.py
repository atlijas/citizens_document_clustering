from gensim.models.doc2vec import Doc2Vec
import glob
import json


all_files = glob.glob('path/to/lemmas/*lmms')
model = Doc2Vec.load('name_of_model.model')


def get_similarity(n_files):
    for file in all_files:
        most_similar = (model.docvecs.most_similar([file], topn = n_files))
        yield  [file, most_similar]


similarity = [w for w in get_similarity(len(all_files))]


def to_dict():
    for file1, file2 in similarity:
        for f, k in file2:
            x = {'source': file1, 'target': f, 'value': k}
            yield x


weights = [w for w in to_dict()]
#weights = json.dumps({'links': weights})

with open('weights.json', 'w', encoding = 'utf-8') as file:
    json.dump({'links': weights}, file, ensure_ascii = False, indent = 4)
