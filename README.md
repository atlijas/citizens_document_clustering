# Citizens Document Clustering

This tool uses document embeddings from Gensim by @RaRe-Technologies
to classify and make clusters from documents.

Icelandic texts are lemmatized using nouns_lemmas_extractions.py, which was built around
Reynir by @mideind. Lemmatization is available for Icelandic and English. As
of now, users need to input a path to files for Icelandic in
nouns_lemmas_extractions.py and provide a file as an arg (flag: -f) for English.

# License
[AGPL](https://en.wikipedia.org/wiki/Affero_General_Public_License)
