from gensim.models import Word2Vec
import warnings
import nltk
warnings.simplefilter(action='ignore', category=FutureWarning)


file_dir = 'dir/'
file = 'file'

print("Retrieving text")

def get_file(file):
    with open(file, 'r', encoding = 'utf-8') as txt:
        txt = txt.read()
        return txt


text = get_file(file_dir+file+'.txt')
print("Text retrieved")

print("Tokenizing sentences")
all_sentences = nltk.sent_tokenize(text)
print("All sentences ready")

print("Tokenizing words")
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
print("All words ready")

print("Training model")
model1 = Word2Vec(all_words, min_count = 3,
                  size = 100, window = 5, workers = 8)

print("Model trained")
print("Saving model")
model1.save(file+'_w2v.model')
print(f"Model ready: {file}_w2v.model")
