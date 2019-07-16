from gensim.models.doc2vec import Doc2Vec
import glob


all_files = glob.glob('path/to/lmms/files/*lmms')
model = Doc2Vec.load('model.model')


# Returns a dict
# Format: {file: similarity_to_all_other_files}
def get_similarity(n_files):
    for file in all_files:
        most_similar = (model.docvecs.most_similar([file], topn = n_files))
        yield {file: most_similar}


similarity = [w for w in get_similarity(len(all_files))]
