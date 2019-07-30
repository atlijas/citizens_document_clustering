from gensim.models.doc2vec import Doc2Vec
import glob
import json


all_files = glob.glob('txts/*lmms')
model = Doc2Vec.load('lmms.model')


def get_similarity(n_files):
    for file in all_files:
        most_similar = (model.docvecs.most_similar([file], topn = n_files))
        for f,s in most_similar:
            yield {'source': file, 'target': f, 'value': s}


weights = [w for w in get_similarity(len(all_files))]


def write_to_json():
        for w in get_similarity(len(all_files)):
                with open('weights.json', 'a', encoding = 'utf-8') as file:
                        json.dump(w, file, ensure_ascii = False, indent = 4)


write_to_json()
