# Citizens Document Clustering

- Document clustering for Citizens Foundation.
- Built using document embeddings from Gensim by RaRe-Technologies.
- Our Doc2Vec model assumes lemmas as input, although inflected words work, too.
- Icelandic texts are lemmatized using ice_lemmatizer.py, which is built on Reynir by Mideind.
- English texts are lemmatized using en_lemmatizer.py, which is supported
by spaCy.
- This repository is a work in progress.

## Doc2Vec
### Includes:
- A script to train a Doc2Vec model.
- A script to test a Doc2Vec model.
- A script to get the similarity (float) between all docs in the model.
- A couple of short texts, not suited for training a reliable model.

## Spelling
### Includes:
- A script to see if a word is split in two, a common spelling mistake
in Icelandic.
  - bílakjallari | \*bíla kjallari

### To do:
- Add a script that handles other common spelling mistakes.

# Word2Vec
### Includes:
- A script to train a Word2Vec model.
  - As of now, the model is only used for correction of spelling mistakes.



# License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
